import time


def datetime_to_timestamp(val: str) -> int:
    d_fmt = '%Y/%m/%d %H:%M:%S'
    n_chars = 19
    try:
        return int(time.mktime(time.strptime(val[:n_chars], d_fmt)))
    except Exception:
        return None


def datefmt_to_timestamp(val: str, fmt: str) -> int:
    try:
        return int(time.mktime(time.strptime(val.strip(), fmt)))
    except Exception:
        return None


def uptime_seconds(val: str) -> int:
    lst = val.split(' days, ')
    days = int(lst[0]) if len(lst) > 1 else 0
    seconds = sum(
        a * b
        for a, b in zip((3600, 60, 1), map(int, lst[-1].split(':'))))
    return 86400 * days + seconds


def to_int(val: str) -> int:
    try:
        return int(val)
    except Exception:
        return


def to_bool(val: str) -> bool:
    return True if val == 'True' else False if val == 'False' else None
