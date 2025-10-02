import time

def measure_latency(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        latency = time.time() - start
        return result, latency
    return wrapper
