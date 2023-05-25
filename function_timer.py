"""
A simple function timer decorator.
"""

import time
from functools import wraps

def function_timer(func):
    """
    A decorator that times a function.
    """
    # @wraps(func)
    def wrapper(*args, **kwargs):
        """
        A wrapper that times a function.
        """
        start = time.time()
        output = func(*args, **kwargs)
        end = time.time()

        print(f"Function {func.__name__} took {end - start:.10f} seconds to complete.")

        return output

    return wrapper
