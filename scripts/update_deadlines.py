#!/usr/bin/env python3
"""
_data/deadlines.yml 자동 갱신 스크립트.

세 가지 소스에서 학회 마감일을 모아 Jekyll이 읽는 _data/deadlines.yml 형식으로 저장합니다.

  1) TRACKED_BY_TITLE : ccfddl 통합 데이터(allconf.yml)에서 title로 검색해서 가져옴 (가장 간편)
  2) TRACKED_BY_PATH  : allconf.yml에 없는 학회를, ccf-deadlines 저장소의 개별 yml 파일
                        경로를 직접 지정해서 가져옴
                        (https://github.com/ccfddl/ccf-deadlines/tree/main/conference 에서
                         카테고리 폴더를 열어 원하는 학회의 .yml 경로를 확인하세요.
                         예: "conference/AI/emnlp.yml")
  3) MANUAL_ENTRIES   : ccfddl에 아예 없는 학회를 완전히 수동으로 등록 (자동 갱신 대상 아님,
                        직접 날짜를 관리해야 함)

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
# 1) allconf.yml(통합 데이터)에서 title로 찾을 학회들.
#    title 은 allconf.yml 안의 "title" 필드와 정확히 일치해야 합니다 (대소문자 구분).
# ---------------------------------------------------------------------------
TRACKED_BY_TITLE = [
    {"title": "NeurIPS", "tag": ["ML", "AI"]},
    {"title": "ICML", "tag": "ML"},
    {"title": "ICLR", "tag": "ML"},
    {"title": "AAAI", "tag": "AI"},
    {"title": "IJCAI", "tag": "AI"},
    {"title": "MICCAI", "tag": ["BIO", "AI"]},
    # 태그를 2개 이상 주고 싶으면 이렇게 리스트로 감싸주세요:
    {"title": "SIGKDD", "tag": ["ML", "DB"]},
    {"title": "WWW", "tag": ["AI", "MX"]},
    {"title": "ICCV", "tag": ["CV", "AI"]},
    {"title": "AISTATS", "tag": ["STAT", "AI"]},
    {"title": "CVPR", "tag": ["CV", "AI"]},
    {"title": "ICPR", "tag": ["ML", "AI"]},
    {"title": "CogSci", "tag": ["MX", "AI"]},
    {"title": "UAI", "tag": ["STAT", "AI"]},
    {"title": "ECCV", "tag": ["CV", "AI"]},
    {"title": "BMVC", "tag": ["CV", "AI"]},
    {"title": "ICDM", "tag": ["ML", "DB"]},
    {"title": "ACCV", "tag": ["CV", "AI"]},
    {"title": "ACML", "tag": "ML"},
    {"title": "ICASSP", "tag": ["SP", "AI"]},
    {"title": "ECIR", "tag": ["ML", "AI"]},
    {"title": "ICDE", "tag": ["DB", "AI"]},
    {"title": "WSDM", "tag": ["DB", "AI"]},
    {"title": "WACV", "tag": ["CV", "AI"]},
    {"title": "COLT", "tag": "ML"},
]

# ---------------------------------------------------------------------------
# 2) allconf.yml에는 없지만 ccf-deadlines 저장소엔 개별 파일로 존재하는 학회.
#    path는 https://github.com/ccfddl/ccf-deadlines/tree/main/conference 에서
#    직접 찾아서 "conference/카테고리/파일명.yml" 형태로 적어주세요.
# ---------------------------------------------------------------------------
TRACKED_BY_PATH = [
    # 예시:
    # {"path": "conference/AI/emnlp.yml", "tag": "AI"},
    # {"path": "conference/HI/chi.yml", "tag": "AI"},
]

# ---------------------------------------------------------------------------
# 3) ccfddl 데이터베이스에 아예 없는 학회 (완전 수동 등록).
#    이 목록은 자동 갱신되지 않으므로, 매해 직접 날짜를 갱신해야 합니다.
# ---------------------------------------------------------------------------
MANUAL_ENTRIES = [
    {
      "name": "EMBC",
      "full_name": "International Conference of the IEEE Engineering in Medicine and Biology Society",
      "link": "https://embc.embs.org/2027/welcome/",
      "date": "July 11 - July 15, 2027",
      "place": "Singapore",
      "deadline_utc": "TBD",
      "tag": "BIO"
    },
   {
     "name": "ISBI",
     "full_name": "IEEE International Symposium on Biomedical Imaging",
     "link": "https://signalprocessingsociety.org/events/2027-ieee-24th-international-symposium-biomedical-imaging-isbi",
     "date": "May 25 - May 28, 2027",
     "place": "Lausanne, Switzerland",
     "deadline_utc": "TBD",
     "tag": "BIO"
   },
   {
     "name": "MVA",
     "full_name": "International Conference on Machine Vision Applications",
     "link": "https://www.mva-org.jp/mva2027/",
     "date": "May 12 - May 14, 2027",
     "place": "Kyushu University, Fukuoka, Japan",
     "deadline_utc": "2027-01-15T11:59:59",
     "tag": ["CV", "AI"]
   },
    # 예시:
    # {
    #     "name": "IEEE BCI",
    #     "full_name": "International Winter Conference on Brain-Computer Interface",
    #     "link": "https://example.com",
    #     "date": "February 2027",
    #     "place": "TBD",
    #     "deadline_utc": "2026-11-01T14:59:00Z",
    #     "conf_end_utc": "2027-02-20T23:59:59Z",  # 생략 가능: 없으면 deadline_utc와 동일하게 취급
    #     "tag": "BIO",
    # },
]

ALLCONF_URL = (
    "https://raw.githubusercontent.com/ccfddl/ccfddl.github.io/"
    "page/conference/allconf.yml"
)

# 개별 학회 yml 파일은 ccf-deadlines 원본 저장소(main 브랜치)에서 직접 가져옵니다.
CCF_DEADLINES_RAW_BASE = "https://raw.githubusercontent.com/ccfddl/ccf-deadlines/main"

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


MONTH_NAMES = {
    "jan": 1, "january": 1,
    "feb": 2, "february": 2,
    "mar": 3, "march": 3,
    "apr": 4, "april": 4,
    "may": 5,
    "jun": 6, "june": 6,
    "jul": 7, "july": 7,
    "aug": 8, "august": 8,
    "sep": 9, "sept": 9, "september": 9,
    "oct": 10, "october": 10,
    "nov": 11, "november": 11,
    "dec": 12, "december": 12,
}

# 축약형 -> 완전한 이름. 이미 완전한 형태(예: "may", "june")는 넣지 않아도 됨
# (아래 expand_month_abbreviations가 매핑에 없는 단어는 그대로 둠).
MONTH_ABBR_TO_FULL = {
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "sept": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December",
}


def expand_month_abbreviations(date_str: str) -> str:
    """"Oct 8-13, 2026" -> "October 8-13, 2026" 처럼, 표시용 date 문자열 안의
    축약형 월 이름을 완전한 이름으로 통일. (allconf.yml 소스마다 표기가 제각각이라
    카드에 그대로 노출될 때 들쭉날쭉해 보이는 것을 방지)"""
    if not date_str:
        return date_str

    def repl(m: "re.Match") -> str:
        word = m.group(0)
        full = MONTH_ABBR_TO_FULL.get(word.lower())
        return full if full else word

    return re.sub(r"[A-Za-z]+", repl, date_str)


def parse_conf_end_date(date_str: str) -> str | None:
    """"September 8 - 13, 2026" 같은 표시용 날짜 문자열에서 '학회 마지막 날'을
    best-effort로 추출해 UTC ISO 문자열로 반환. 파싱에 실패하면 None."""
    if not date_str:
        return None
    s = date_str.strip()

    years = re.findall(r"20\d{2}", s)
    if not years:
        return None
    year = int(years[-1])

    # 문자열에 등장하는 마지막 '월' 이름과, 그 뒤에 등장하는 마지막 '일' 숫자를 사용
    last_month = None
    last_month_end_idx = None
    for m in re.finditer(r"[A-Za-z]+", s):
        word = m.group(0).lower()
        if word in MONTH_NAMES:
            last_month = MONTH_NAMES[word]
            last_month_end_idx = m.end()

    if not last_month:
        return None

    day_candidates = [
        (m.start(), int(m.group(1)))
        for m in re.finditer(r"\b(\d{1,2})\b", s)
    ]
    if not day_candidates:
        return None

    days_after_month = [d for pos, d in day_candidates if pos >= last_month_end_idx]
    day = days_after_month[-1] if days_after_month else day_candidates[-1][1]
    if not (1 <= day <= 31):
        return None

    try:
        # 그날 자정(23:59:59)까지는 '진행 중'으로 간주
        dt = datetime(year, last_month, day, 23, 59, 59, tzinfo=timezone.utc)
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return None


def normalize_tags(tag) -> list:
    """tag가 "ML"처럼 문자열 하나든, ["CV", "ML"]처럼 리스트든 항상 리스트로 통일."""
    if isinstance(tag, (list, tuple)):
        return list(tag)
    return [tag]


def build_entry(title: str, conf: dict, tag) -> dict | None:
    """ccfddl 스키마의 conf 객체(title/description/confs...) 하나를 사이트용 항목으로 변환."""
    confs_list = conf.get("confs") or []
    picked = pick_latest_upcoming_conf(confs_list)
    if not picked:
        print(f"  ! '{title}' 에 유효한 마감일 정보가 없음")
        return None

    c = picked["conf"]
    date_str = expand_month_abbreviations(c.get("date", "TBD"))
    conf_end_utc = parse_conf_end_date(date_str) or picked["utc_iso"]
    # ↑ 종료일 파싱에 실패하면, 예전과 동일하게 "마감 = 종료"로 취급 (Awaiting Conference 구간 없이 바로 Completed)

    print(f"  ✓ {title}: {picked['utc_iso']}")
    return {
        "name": title,
        "full_name": conf.get("description", title),
        "link": c.get("link", ""),
        "date": date_str,
        "place": c.get("place", "TBD"),
        "deadline_utc": picked["utc_iso"],
        "conf_end_utc": conf_end_utc,
        "tag": normalize_tags(tag),
    }


def fetch_by_title(results: list) -> None:
    if not TRACKED_BY_TITLE:
        return
    print(f"Fetching {ALLCONF_URL} ...")
    resp = requests.get(ALLCONF_URL, timeout=30)
    resp.raise_for_status()
    all_conferences = yaml.safe_load(resp.text)
    by_title = {c.get("title", "").strip(): c for c in all_conferences if c.get("title")}

    for tracked in TRACKED_BY_TITLE:
        title = tracked["title"]
        conf = by_title.get(title)
        if not conf:
            print(f"  ! '{title}' 을(를) allconf.yml에서 찾지 못함 (TRACKED_BY_PATH로 개별 파일을 지정해보세요)")
            continue
        entry = build_entry(title, conf, tracked["tag"])
        if entry:
            results.append(entry)


def fetch_by_path(results: list) -> None:
    for tracked in TRACKED_BY_PATH:
        path = tracked["path"]
        url = f"{CCF_DEADLINES_RAW_BASE}/{path}"
        print(f"Fetching {url} ...")
        try:
            resp = requests.get(url, timeout=30)
            resp.raise_for_status()
        except requests.RequestException as e:
            print(f"  ! '{path}' 가져오기 실패: {e}")
            continue

        data = yaml.safe_load(resp.text)
        # ccf-deadlines의 개별 파일은 보통 "- title: ... confs: [...]" 형태의 리스트(원소 1개)
        conf = data[0] if isinstance(data, list) else data
        if not conf or not conf.get("title"):
            print(f"  ! '{path}' 형식을 인식하지 못함")
            continue

        entry = build_entry(conf["title"], conf, tracked["tag"])
        if entry:
            results.append(entry)


def main():
    results = []
    fetch_by_title(results)
    fetch_by_path(results)

    if MANUAL_ENTRIES:
        print(f"수동 등록 항목 {len(MANUAL_ENTRIES)}개 추가")
        for entry in MANUAL_ENTRIES:
            entry = dict(entry)
            entry["tag"] = normalize_tags(entry.get("tag"))
            entry["date"] = expand_month_abbreviations(entry.get("date", "TBD"))
            entry.setdefault("conf_end_utc", entry.get("deadline_utc"))
            results.append(entry)

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
