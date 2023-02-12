import unittest

def evaluate_expression(expression):
    stack = []
    tokens = expression.split()
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token == '+':
            right = stack.pop()
            left = stack.pop()
            stack.append(left + right)
        elif token == '-':
            right = stack.pop()
            left = stack.pop()
            stack.append(left - right)
        elif token == '*':
            right = stack.pop()
            left = stack.pop()
            stack.append(left * right)
    return stack.pop()

class TestExpressionEvaluation(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(evaluate_expression('2 3 +'), 5)

    def test_subtraction(self):
        self.assertEqual(evaluate_expression('2 3 -'), -1)

    def test_multiplication(self):
        self.assertEqual(evaluate_expression('2 3 *'), 6)

    def test_division(self):
        self.assertEqual(evaluate_expression('6 3 /'), 2)

    def test_multiple_operations(self):
        self.assertEqual(evaluate_expression('2 3 4 + *'), 14)

if __name__ == '__main__':
    unittest.main()
