from unittest import TestCase

from src.foo import func1

class TestFoo(TestCase):
    def test_func1(self):
        a = 1
        b = -1
        self.assertTrue(func1(a, b) == 0)
