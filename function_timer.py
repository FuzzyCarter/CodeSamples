"""
A simple function timer decorator.

Author: Fuzzy Carter
"""

import time


def function_timer(func) -> callable:
    """
    A decorator that times a function.
    """

    def wrapper(*args, **kwargs):
        """
        A wrapper that times a function.
        """
        start = time.perf_counter()
        output = func(*args, **kwargs)
        end = time.perf_counter()

        print(f"Function {func.__name__} took {end - start:.10f} seconds to complete.")

        return output

    return wrapper
