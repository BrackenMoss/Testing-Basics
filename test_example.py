import unittest
from example import fizzbuzz


if __name__ == '__main__':
    unittest.main()


class TestFizzBuzz(unittest.TestCase):

    def test_one(self):
        self.assertEqual(fizzbuzz(1), [1])

    def test_two(self):
        self.assertEqual(fizzbuzz(1), [1,2])