from datetime import datetime


def cronometer(func):
    def wrapper(*args, **kwargs):
        now = datetime.now()
        func(*args, **kwargs)
        then = datetime.now()
        print("Cronometer =", then - now)
    return wrapper
