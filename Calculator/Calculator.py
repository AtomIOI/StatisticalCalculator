from Functions.Addition import Addition
from Functions.Subtraction import Subtraction
from Functions.Multiplication import Multiplication
from Functions.Division import Division
from Functions.Exponentiation import Exponentiation
from Functions.Logarithm import Logarithm


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
