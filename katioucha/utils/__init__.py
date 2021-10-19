import time
import logging
from functools import wraps


def logwrap(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        logging.info(f"Start {func.__name__}")
        t0 = time.time()
        result = func(*args, **kwargs)
        t1 = time.time()
        logging.info(f"Escaping {func.__name__}. Elapsed time = {t1-t0}s")
        return result

    return with_logging
