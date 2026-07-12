#!/usr/bin/env python3
"""
_data/deadlines.yml 자동 갱신 스크립트.

ccfddl/ccf-deadlines 프로젝트가 관리하는 통합 데이터 파일(allconf.yml)에서
TRACKED_CONFERENCES 에 지정된 학회만 뽑아, 가장 최근(미래) 마감일을 계산해
Jekyll이 읽는 _data/deadlines.yml 형식으로 저장합니다.

GitHub Actions(.github/workflows/update-deadlines.yml)에 의해 매일 자동 실행됩니다.
로컬에서 수동 실행하려면:
    pip install pyyaml requests
    python scripts/update_deadlines.py
"""

import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

import requests
import yaml

# ---------------------------------------------------------------------------
# 1) 추적하고 싶은 학회 목록을 여기서 관리하세요.
#    title 은 allconf.yml 안의 "title" 필드와 정확히 일치해야 합니다 (대소문자 구분).
#    tag 는 사이트 필터 버튼에 표시될 카테고리입니다 (자유롭게 지정 가능).
# ---------------------------------------------------------------------------
TRACKED_CONFERENCES = [
    {"title": "NeurIPS", "tag": "ML"},
    {"title": "ICML", "tag": "ML"},
    {"title": "ICLR", "tag": "ML"},
    {"title": "AAAI", "tag": "AI"},
    {"title": "IJCAI", "tag": "AI"},
    {"title": "MICCAI", "tag": "BIO"},
    {"title": "EMBC", "tag": "BIO"},
    {"title": "ISBI", "tag": "BIO"},
]

ALLCONF_URL = (
    "https://raw.githubusercontent.com/ccfddl/ccfddl.github.io/"
    "page/conference/allconf.yml"
)

OUTPUT_PATH = Path(__file__).resolve().parent.parent / "_data" / "deadlines.yml"

# 자주 쓰이는 timezone 표기 -> UTC와의 시차(시간)
FIXED_OFFSETS = {
    "AOE": -12,  # Anywhere on Earth
}


def parse_utc_offset(tz_str: str) -> int | None:
    """'UTC-12', 'UTC+2', 'AoE' 같은 표기를 시간 단위 정수 오프셋으로 변환."""
    if not tz_str:
        return None
    key = tz_str.strip().upper()
    if key in FIXED_OFFSETS:
        return FIXED_OFFSETS[key]
    m = re.match(r"UTC([+-]\d{1,2})$", key)
    if m:
        return int(m.group(1))
    m = re.match(r"GMT([+-]\d{1,2})$", key)
    if m:
        return int(m.group(1))
    return None


def to_utc_iso(deadline_str: str, tz_str: str) -> str | None:
    """'2026-05-15 11:59:00' + 'UTC-12' -> '2026-05-15T23:59:00Z' 형태로 변환."""
    if not deadline_str:
        return None
    deadline_str = deadline_str.strip()
    try:
        naive = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        try:
            naive = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print(f"  ! 날짜 파싱 실패, 건너뜀: {deadline_str!r}")
            return None

    offset_hours = parse_utc_offset(tz_str)
    if offset_hours is None:
        # 오프셋을 못 찾으면 IANA 타임존 이름일 수 있음 -> zoneinfo 시도
        try:
            from zoneinfo import ZoneInfo

            local = naive.replace(tzinfo=ZoneInfo(tz_str))
            utc_dt = local.astimezone(timezone.utc)
            return utc_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
        except Exception:
            print(f"  ! 알 수 없는 타임존 '{tz_str}', UTC로 가정")
            offset_hours = 0

    # naive 시각은 "그 타임존의 로컬 시각" -> UTC = local - offset
    utc_dt = naive - timedelta(hours=offset_hours)
    return utc_dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def pick_latest_upcoming_conf(confs: list) -> dict | None:
    """confs(연도별 목록) 중 '가장 이른 미래 마감일'을 가진 연도를 고른다.
    모든 마감일이 지났다면 가장 최근(과거) 것을 반환."""
    now_utc = datetime.now(timezone.utc)
    upcoming = []
    past = []

    for c in confs:
        timeline = c.get("timeline") or []
        if not timeline:
            continue
        # timeline의 마지막 항목을 '본 논문 마감'으로 간주
        last_entry = timeline[-1]
        deadline_raw = last_entry.get("deadline")
        tz = c.get("timezone", "UTC+0")
        utc_iso = to_utc_iso(deadline_raw, tz)
        if not utc_iso:
            continue
        dt = datetime.strptime(utc_iso, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        entry = {"conf": c, "utc_iso": utc_iso, "dt": dt}
        if dt >= now_utc:
            upcoming.append(entry)
        else:
            past.append(entry)

    if upcoming:
        upcoming.sort(key=lambda e: e["dt"])
        return upcoming[0]
    if past:
        past.sort(key=lambda e: e["dt"], reverse=True)
        return past[0]
    return None


def main():
    print(f"Fetching {ALLCONF_URL} ...")
    resp = requests.get(ALLCONF_URL, timeout=30)
    resp.raise_for_status()
    all_conferences = yaml.safe_load(resp.text)

    by_title = {c.get("title", "").strip(): c for c in all_conferences if c.get("title")}

    results = []
    for tracked in TRACKED_CONFERENCES:
        title = tracked["title"]
        conf = by_title.get(title)
        if not conf:
            print(f"  ! '{title}' 을(를) allconf.yml에서 찾지 못함 (제목 철자를 확인하세요)")
            continue

        confs_list = conf.get("confs") or []
        picked = pick_latest_upcoming_conf(confs_list)
        if not picked:
            print(f"  ! '{title}' 에 유효한 마감일 정보가 없음")
            continue

        c = picked["conf"]
        results.append(
            {
                "name": title,
                "full_name": conf.get("description", title),
                "link": c.get("link", ""),
                "date": c.get("date", "TBD"),
                "place": c.get("place", "TBD"),
                "deadline_utc": picked["utc_iso"],
                "tag": tracked["tag"],
            }
        )
        print(f"  ✓ {title}: {picked['utc_iso']}")

    if not results:
        print("갱신할 데이터가 없어 종료합니다 (기존 파일 유지).")
        sys.exit(0)

    # 마감일이 가까운 순으로 정렬
    results.sort(key=lambda r: r["deadline_utc"])

    header = (
        "# _data/deadlines.yml\n"
        "# 이 파일은 scripts/update_deadlines.py 에 의해 자동으로 생성됩니다.\n"
        f"# 마지막 자동 갱신: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n"
        "# 수동으로 편집한 내용은 다음 자동 실행 때 덮어써질 수 있습니다.\n\n"
    )

    yaml_body = yaml.safe_dump(
        results, allow_unicode=True, sort_keys=False, default_flow_style=False
    )

    OUTPUT_PATH.write_text(header + yaml_body, encoding="utf-8")
    print(f"\n{OUTPUT_PATH} 갱신 완료 ({len(results)}개 학회)")


if __name__ == "__main__":
    main()
