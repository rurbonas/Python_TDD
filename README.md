# Test Driven Development (TDD)
![TDD](https://developer.ibm.com/developer/default/articles/5-steps-of-test-driven-development/images/tdd-red-green-refactoring-v3.png)

- Import 'unittest' and 'pytest' as these are the dependencies for test creation
```python

import unittest # Unit testing is a software testing method by which individual units of source code are tested to determine whether they are fit for use.
import pytest # Python testing tool that helps you write better programs

from simple_calc import SimpleCalc

class Calctest(unittest.TestCase):

    calc = SimpleCalc()


# Assertions to write our test cases
# We will use our basic calculator example to write the tests first then the code

    # def test_add(self, num1, num2): # Method
    def test_add(self): # Test
        # Naming convention is essential to have the test in the name of our method
        self.assertEqual(self.calc.add(3,2) ,5) # if True, the test will pass
        

    def test_subtract(self):  # Test
        self.assertAlmostEqual(self.calc.subtract(3,2) ,1)

    def test_multi(self):
        self.assertEqual(self.calc.multi(2,2) ,4) # 2 * 2 = 4

    def test_divide(self):
        self.assertEqual(self.calc.divide(6,3) ,2)
```
- We'll call these functions when testing
```python
class SimpleCalc:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multi(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2

```