import unittest
from fibannaci import factorial_recursive, factorial_iterative, fibonacci_recursive, fibonacci_iterative

class TestFunctions(unittest.TestCase):
    def test_factorial_recursive(self):
        self.assertEqual(factorial_recursive(9), 362880)
        self.assertEqual(factorial_recursive(0), 1)

    def test_factorial_iterative(self):
        self.assertEqual(factorial_iterative(9), 362880)
        self.assertEqual(factorial_iterative(0), 1)

    def test_fibonacci_recursive(self):
        self.assertEqual(fibonacci_recursive(5), 8)
        self.assertEqual(fibonacci_recursive(0), 1)

    def test_fibonacci_iterative(self):
        self.assertEqual(fibonacci_iterative(5), 8)
        self.assertEqual(fibonacci_iterative(0), 1)

if __name__ == '__main__':
    unittest.main()