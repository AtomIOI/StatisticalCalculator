import unittest

from Functions.Addition import Addition
from Functions.Subtraction import Subtraction
from Functions.Multiplication import Multiplication
from Functions.Division import Division
from Functions.Exponentiation import Exponentiation
from Functions.Logarithm import Logarithm


class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(3, Addition.sum(1, 2))

    def test_MathOperations_AdditionList(self):
        numberlist = [1, 2, 3]
        self.assertEqual(6, Addition.sumlist(numberlist))

    def test_MathOperations_Subtraction(self):
        self.assertEqual(-1, Subtraction.difference(1, 2))

    def test_MathOperations_Multiplication(self):
        self.assertEqual(4, Multiplication.product(2, 2))

    def test_MathOperations_Division(self):
        self.assertEqual(2, Division.quotient(4, 2))

    def test_MathOperations_Exponentiation(self):
        self.assertEqual(16, Exponentiation.power(4, 2))

    def test_MathOperations_Logarithm(self):
        self.assertEqual(3, Logarithm.log(2, 8))


if __name__ == '__main__':
    unittest.main()
