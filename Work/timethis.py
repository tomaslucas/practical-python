# timethis.py
import time

def timethis(func):
    def wrapper(*args, **kargs):
        start = time.time()
        r = func(*args, **kargs)
        end = time.time()
        print(f"{func.__module__}.{func.__name__}: {end-start:2f}")
        return func(*args, **kargs)
    return wrapper