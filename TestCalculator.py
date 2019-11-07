import unittest
import Calculator as calculator
class TestCalculator(unittest.TestCase):
    def test_int_add(self):
        self.assertEqual(calculator.add(10, 3), 13)

    def test_int2_add(self):
        self.assertEqual(calculator.add(9, 6), 15)

    def test_float_add(self):
        self.assertEqual(calculator.add(4.2, 3), 7.2)

    def test_int_minus(self):
        self.assertEqual(calculator.minus(9, 1), 8)

    def test_int2_minus(self):
        self.assertEqual(calculator.minus(9, 8), 1)

    def test_float_minus(self):
        self.assertEqual(calculator.minus(4.5, 3.2), 1.3)

    def test_int_times(self):
        self.assertEqual(calculator.times(9, 3), 27)

    def test_int2_times(self):
        self.assertEqual(calculator.times(10, 4), 40)

    def test_float_times(self):
        self.assertEqual(calculator.times(4.2, 3.3), 13.86)

    def test_int_divided(self):
        self.assertEqual(calculator.divided(9, 3), 3)

    def test_int2_divided(self):
        self.assertEqual(calculator.divided(9, 0), "無限")

    def test_float_divided(self):
        self.assertEqual(calculator.divided(6.3, 3), 2.1)

if __name__ == '__main__':
    unittest.main()