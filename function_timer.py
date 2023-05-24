"""
A simple function timer decorator.
"""

import time

def function_timer(func):
    """
    A decorator that times a function.
    """
    def wrapper(*args, **kwargs):
        """
        A wrapper that times a function.
        """
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end - start} seconds to complete.")
    return wrapper