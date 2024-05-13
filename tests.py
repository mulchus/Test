import unittest


def add_numbers(x, y):
    return x + y


def div_numbers(x, y):
    return x/y


class TestAddNumbers(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)
    
    def test_add_mixed_numbers(self):
        self.assertEqual(add_numbers(-2, 3), 1)

    def test_div_zero_numbers(self):
        self.assertRaises(ZeroDivisionError, div_numbers, -2, 0)


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
