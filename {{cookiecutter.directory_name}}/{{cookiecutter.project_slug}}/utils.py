from time import time
from uuid import uuid4


def get_time(seconds_precision=True):
    """Return current time as Unix/Epoch timestamp, in seconds.
    :param seconds_precision: if True, return with seconds precision as integer (default).
                              If False, return with milliseconds precision as floating point number of seconds.
    """
    return time() if not seconds_precision else int(time())


def get_uuid():
    """Return a UUID4 as string"""
    return str(uuid4())


def snakecase_to_camelcase(string: str) -> str:
    """Convert a snake_case string into camelCase"""
    return ''.join(
        word.capitalize() if i != 0 else word
        for i, word in enumerate(string.split('_'))
    )
