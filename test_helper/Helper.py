import cProfile
import unittest

def do_profile(func):
    def profiled_func(*args, **kwargs):
        pr = cProfile.Profile()
        try:
            pr.enable()
            result = func(*args, **kwargs)
            pr.disable()
            return result
        finally:        
            pr.print_stats()

    return profiled_func

