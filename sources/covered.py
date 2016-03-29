"""This file is covered by tests."""

def hello(count):
    s = "Hello World!"
    if count == 1:
        return s
    result = [s] * count
    result = tuple(result)
    return result
