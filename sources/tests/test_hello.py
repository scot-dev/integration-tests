import unittest

from sources.covered import hello


class TestHello(unittest.TestCase):
    def test_once(self):
        self.assertEqual(hello(1), "Hello World!")
    def test_multi(self):
        hi = hello(10)
        self.assertEqual(len(hi), 10)
        for h in hi:
            self.assertEqual(h, "Hello World!")
