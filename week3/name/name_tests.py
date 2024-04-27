import unittest
from name import find_names

class TestFindNames(unittest.TestCase):
    def test_find_names(self):
        # Test with the actual file
        result = find_names(r'C:\py_files\sem2\mp2\pt3\boy_names.txt')
        self.assertEqual(len(result), 3)
        self.assertIsInstance(result[0], set)
        self.assertEqual(len(result[0]), 3)
        self.assertIsInstance(result[1], tuple)
        self.assertEqual(len(result[1]), 2)
        self.assertIsInstance(result[1][0], int)
        self.assertIsInstance(result[1][1], set)
        self.assertIsInstance(result[2], tuple)
        self.assertEqual(len(result[2]), 3)
        self.assertIsInstance(result[2][0], str)
        self.assertIsInstance(result[2][1], int)
        self.assertIsInstance(result[2][2], int)

        # Test with the actual file
        result = find_names(r'C:\py_files\sem2\mp2\pt3\girl_names.txt')
        self.assertEqual(len(result), 3)
        self.assertIsInstance(result[0], set)
        self.assertEqual(len(result[0]), 3)
        self.assertIsInstance(result[1], tuple)
        self.assertEqual(len(result[1]), 2)
        self.assertIsInstance(result[1][0], int)
        self.assertIsInstance(result[1][1], set)
        self.assertIsInstance(result[2], tuple)
        self.assertEqual(len(result[2]), 3)
        self.assertIsInstance(result[2][0], str)
        self.assertIsInstance(result[2][1], int)
        self.assertIsInstance(result[2][2], int)

if __name__ == '__main__':
    unittest.main()