import time
from functools import wraps

def Timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start=time.time()
        result=func(*args, **kwargs)
        end=time.time()
        print("Excuted in:",end-start)
    return wrapper

@Timer
def Runloop(t):
    for i in range(t):
        print("Running loop")
Runloop(10000)
# Runloop(100000)