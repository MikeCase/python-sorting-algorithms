import functools
import time

class MyDecorators:
    def __init__(self):
        pass

    def timer(_func=None, n=1):
        def decorator_repeat(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.perf_counter()
                for i in range(n):
                    value = func(*args, **kwargs)
                end_time = time.perf_counter()
                total_time = end_time-start_time
                print(f'Took a total time of: {total_time} to run {n} time(s)')
                return value
            return wrapper

        if _func is None:
            return decorator_repeat
        else:
            return decorator_repeat(_func)