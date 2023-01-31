import time


def datetime_to_timestamp(val: str) -> int:
    d_fmt = '%Y/%m/%d %H:%M:%S'
    n_chars = 19
    try:
        return int(time.mktime(time.strptime(val[:n_chars], d_fmt)))
    except Exception:
        return None
