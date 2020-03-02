from MathOperations.Addition import Addition
from MathOperations.Subtraction import Subtraction
from MathOperations.Multiplication import Multiplication
from MathOperations.Division import Division
from MathOperations.Exponentiation import Exponentiation
from MathOperations.Logarithm import Logarithm


class Calculator:
    Result = 0

    def __init__(self):
        pass

    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def Product(self, a, b):
        self.Result = Multiplication.product(a, b)
        return self.Result

    def Quotient(self, a, b):
        self.Result = Division.quotient(a, b)
        return self.Result

    def Power(self, a, b):
        self.Result = Exponentiation.power(a, b)
        return self.Result

    def Log(self, a, b):
        self.Result = Logarithm.log(a, b)
        return  self.Result
