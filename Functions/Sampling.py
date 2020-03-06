import math
from scipy import stats
from Functions.Random import RNG
from Functions.Division import Division
from Functions.Statistics import Stats
from Functions.Multiplication import Multiplication
from Functions.Addition import Addition
from Functions.Subtraction import Subtraction
from Functions.Exponentiation import Exponentiation


class Sampling:
    # Simple random sampling
    @staticmethod
    def simpleSample(array, n):
        result = []
        while n >= 0:
            result.append(array.pop(RNG.randINT(0, len(array) - 1)))
            n -= 1
        return result

    # Systematic sampling
    @staticmethod
    def systematicSample(array, n):
        result = []
        while n > 0:
            index = len(array)//n
            if index >= len(array):
                index -= 1
            result.append(array.pop(index))
            n -= 1
        return result

    # Confidence Interval For a Sample
    @staticmethod
    def confidenceInterval(array, ci):
        df = len(array) - 1
        alpha = 1 - ci
        tval = stats.t.ppf(1 - alpha, df)
        stdev = Stats.standardDeviation(array)
        se = Division.quotient(stdev, Exponentiation.power(len(array), .5))
        numerate = Multiplication.product(se, tval)
        mean = Stats.mean(array)
        return [mean - numerate, mean + numerate]

    # Margin of Error
    @staticmethod
    def marginError(stdev, ci, n):
        df = n - 1
        alpha = 1 - ci
        tval = stats.t.ppf(1 - alpha, df)
        se = Division.quotient(stdev, Exponentiation.power(n, .5))
        return Multiplication.product(tval, se)

    # Cochran’s Sample Size Formula
    @staticmethod
    def cochran(array, e, p):
        df = len(array) - 1
        zscore = stats.t.ppf(e, df)
        q = 1 - p
        exp = Exponentiation.power(zscore, 2)
        numerator = Multiplication.product(p*q, exp)
        return Division.quotient(numerator, Exponentiation.power(e, 2))

    # How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation)
    # How to Find a Sample Size Given a Confidence Interval and Width (known population standard deviation)


dem = Sampling()
arr = RNG.prandINTL(0, 10, 100, 1)
print(arr)
print(dem.cochran(arr, .05, .5))
