import unittest


class TestOnePlusTwo(unittest.TestCase):
    def test_one_plus_two(self):
        x = 1
        y = 2
        z = x + y
        self.assertEqual(z, 3)


if __name__ == "__main__":
    unittest.main()
