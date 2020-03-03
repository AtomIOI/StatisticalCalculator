import unittest

from Functions.Addition import Addition
from Functions.Subtraction import Subtraction
from Functions.Multiplication import Multiplication
from Functions.Division import Division
from Functions.Exponentiation import Exponentiation
from Functions.Logarithm import Logarithm
from Functions.Random import RNG
from Functions.Statistics import Stats

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

    def test_Random_Integer_Seed(self):
        self.assertEqual(9, RNG.prandINT(1, 10, 30))

    def test_Random_Float_Seed(self):
        self.assertEqual(5.851734081452295, RNG.prandFLT(1, 10, 30))

    def test_Random_IntegerList_Seed(self):
        self.assertEqual([9, 5, 1, 4, 5], RNG.prandINTL(1, 10, 5, 30))

    def test_Random_FloatList_Seed(self):
        self.assertEqual([5.851734081452295, 3.6027679927574847, 1.2703321769601437, 6.882721785034857, 2.89007825994758], RNG.prandFLTL(1, 10, 5, 30))

    def test_Random_Selection_Seed(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(5, RNG.prandElem(arr, 30))

    def test_Random_Multiple_Selection_Seed(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual([5, 3, 5, 1, 5], RNG.prandElems(arr, 5, 30))

    def test_Stats_Mean(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(3.0, Stats.mean(arr))

    def test_Stats_Median(self):
        arr = [1, 2, 3, 4, 5]
        arrTwo = [1, 2, 3, 4]
        self.assertEqual(3, Stats.median(arr))
        self.assertEqual(2.5, Stats.median(arrTwo))

if __name__ == '__main__':
    unittest.main()
