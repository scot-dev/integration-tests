"""This file is covered by tests."""

import time

def hello(count):
    s = "Hello World!"
    if count == 1:
        return s
        
    time.sleep(1)
        
    return [s] * count
