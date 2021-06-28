# Import unittest and pytest as these are the dependencies for test creation

import unittest
import pytest

from simple_calc import SimpleCalc

class Calctest(unittest.TestCase):

    calc = SimpleCalc()


# Assertions to write our test cases
# We will use our basic calculator example to write the tests first then the code

    # def test_add(self, num1, num2): # Method
    def test_add(self): # Test
        # Naming convention is essential to have the test in the name of our method
        self.assertEqual(self.calc.add(3,2) ,5) # if True, the test will pass
        # return num1 + num2

    def test_subtract(self):  # Test
        self.assertAlmostEqual(self.calc.subtract(3,2) ,1)

    def test_multi(self):
        self.assertEqual(self.calc.multi(2,2) ,4) # 2 * 2 = 4

    def test_divide(self):
        self.assertEqual(self.calc.divide(6,3) ,2)