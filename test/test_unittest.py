import unittest
from src import calculator

class TestCalculatorFunctions(unittest.TestCase):

    # Test fun1 (addition)
    def test_fun1(self):
        self.assertEqual(calculator.fun1(5, 3), 8)
        self.assertEqual(calculator.fun1(-2, 7), 5)
        self.assertEqual(calculator.fun1(0, 0), 0)

    # Test fun2 (subtraction)
    def test_fun2(self):
        self.assertEqual(calculator.fun2(10, 4), 6)
        self.assertEqual(calculator.fun2(3, 5), -2)
        self.assertEqual(calculator.fun2(0, 0), 0)

    # Test fun3 (multiplication)
    def test_fun3(self):
        self.assertEqual(calculator.fun3(6, 7), 42)
        self.assertEqual(calculator.fun3(-3, 5), -15)
        self.assertEqual(calculator.fun3(0, 10), 0)

    # Test fun4 (sum of fun1 + fun2 + fun3)
    def test_fun4(self):
        self.assertEqual(calculator.fun4(2, 3), calculator.fun1(2, 3) + calculator.fun2(2, 3) + calculator.fun3(2, 3))
        self.assertEqual(calculator.fun4(-1, 4), calculator.fun1(-1, 4) + calculator.fun2(-1, 4) + calculator.fun3(-1, 4))

    # Test input validation
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            calculator.fun1("a", 2)
        with self.assertRaises(ValueError):
            calculator.fun2(3, None)
        with self.assertRaises(ValueError):
            calculator.fun3([1], 2)
        with self.assertRaises(ValueError):
            calculator.fun4(1, "b")

if __name__ == "__main__":
    unittest.main()
