import unittest

from sources.covered import hello


class TestHello(unittest.TestCase):
    def test_once(self):
        self.assert_equal(hello(1), "Hello World!")
    def test_multi(self):
        hi = hello(10)
        self.assert_equal(len(hi) == 10)
        for h in hi:
            self.assert_equal(h, "Hello World!")
