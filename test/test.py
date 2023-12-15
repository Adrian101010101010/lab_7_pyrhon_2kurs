# pylint: skip-file
import unittest
from lab7.src.lab7 import count_paths


class TestCountPaths(unittest.TestCase):

    def test_example_1(self):
        corridor = [
            "aaa",
            "cab",
            "def"
        ]
        result = count_paths(corridor)
        self.assertEqual(result, 5)

    def test_example_2(self):
        corridor = ["abcdefaghi"]
        result = count_paths(corridor)
        self.assertEqual(result, 2)

    def test_example_3(self):
        corridor = [
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
        ]
        result = count_paths(corridor)
        self.assertEqual(result, 201684)


if __name__ == '__main__':
    unittest.main()
