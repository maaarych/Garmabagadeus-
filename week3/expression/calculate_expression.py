from doctest import testmod

'''calculator'''
def calculate_expression(expression: str)-> int:

    """
    str -> int
    Calculates a math problem, put into a simple expression.
    If an expression contains unsupported math operations, non mathematical
    questions or has a wrong syntax function should return 'Неправильний вираз!'.
    >>> calculate_expression('Скільки буде 8 відняти 3?')
    5
    >>> calculate_expression('Скільки буде 7 додати 3 помножити на 5?')
    50
    >>> calculate_expression('Скільки буде 10 поділити на -2 додати 11 мінус -3?')
    9
    >>> calculate_expression('Скільки буде 3 в кубі?')
    'Неправильний вираз!'
    """

    if isinstance(expression, str):
        if not expression.endswith('?'):
            return 'Неправильний вираз!'
        expression = expression.replace('Скільки буде', '')
        expression = expression.replace('?', '')
        operations = {'поділити на': '/', 'плюс': '+', 'додати': '+',
                      'відняти': '-', 'мінус': '-', 'помножити на': '*'}
        for key, value in operations.items():
            expression = expression.replace(key, value)
        expression = expression.split()
        if len(expression) % 2 == 0 or any(not (part.lstrip('-').isdigit() \
                or part in operations.values()) for part in expression):
            return 'Неправильний вираз!'
        res = int(expression[0])
        for i in range(1, len(expression), 2):
            if expression[i] in operations.values() and \
            expression[i-1].lstrip('-').isdigit() and expression[i+1].lstrip('-').isdigit():
                if expression[i] == '+':
                    res += int(expression[i+1])
                elif expression[i] == '-':
                    res -= int(expression[i+1])
                elif expression[i] == '*':
                    res *= int(expression[i+1])
                elif expression[i] == '/':
                    res /= int(expression[i+1])
            else:
                return 'Неправильний вираз!'
        return int(res)
    else:
        return 'Неправильний вираз!'

import unittest
from target import calculate_expression

class TestCalculateExpression(unittest.TestCase):
    def test_valid_expressions(self):
        test_cases = [
            ("Скільки буде 8 відняти 3?", 5),
            ("Скільки буде 7 додати 3 помножити на 5?", 50),
            ("Скільки буде 10 поділити на -2 додати 11 мінус -3?", 9)
        ]
        for expr, expected in test_cases:
            with self.subTest(expr=expr, expected=expected):
                self.assertEqual(calculate_expression(expr), expected)

    def test_invalid_expressions(self):
        test_cases = [
            ("Скільки буде 3 в кубі?", 'Неправильний вираз!'),
            ("Скільки сезонів в році?", 'Неправильний вираз!'),
            ("Скільки буде 2 2 додати?", 'Неправильний вираз!'),
            ("Скільки буде 8 відняти 3", 'Неправильний вираз!'),
            (123, 'Неправильний вираз!'),
            ("Скільки буде 8 відняти?", 'Неправильний вираз!')
        ]
        for expr, expected in test_cases:
            with self.subTest(expr=expr, expected=expected):
                self.assertEqual(calculate_expression(expr), expected)

if __name__ == '__main__':
    unittest.main()