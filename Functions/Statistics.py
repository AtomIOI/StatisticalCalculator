import math
from Functions.Division import Division
from Functions.Multiplication import Multiplication
from Functions.Addition import Addition
from Functions.Subtraction import Subtraction
from Functions.Exponentiation import Exponentiation
from Functions.Random import RNG
from scipy import stats


class Stats:
    # Mean
    @staticmethod
    def mean(array):
        total = 0
        for num in array:
            total = total + num
        return Division.quotient(total, len(array))

    # Median
    @staticmethod
    def median(array):
        array.sort()
        size = len(array)
        if size % 2 == 0:
            medOne = array[(size // 2) - 1]
            medTwo = array[size // 2]
            return Division.quotient(Addition.sum(medOne, medTwo), 2)
        return array[math.floor(Division.quotient(size, 2))]

    # Mode
    @staticmethod
    def mode(array):
        mode = 0
        modeCount = 0
        for num in array:
            if array.count(num) > modeCount:
                mode = num
                modeCount = array.count(num)
        return mode

    # Variance
    @staticmethod
    def variance(array):
        mean = Stats.mean(array)
        varianceTotal = 0
        for num in array:
            varianceTotal += Exponentiation.power(Subtraction.difference(num, mean), 2)
        return Division.quotient(varianceTotal, len(array))

    # Standard Deviation
    @staticmethod
    def standardDeviation(array):
        return Exponentiation.power(Stats.variance(array), .5)

    # Quartiles
    @staticmethod
    def quartiles(array):
        array.sort()
        size = len(array)
        if size % 2 == 0:
            medOne = array[(size // 2) - 1]
            medTwo = array[size // 2]
            qTwo = Division.quotient(medOne + medTwo, 2)
            qOne = Stats.median(array[:size // 2])
            qThree = Stats.median(array[size // 2:])
        else:
            qTwo = array[math.floor(Division.quotient(size, 2))]
            qOne = Stats.median(array[:(size // 2) + 1])
            qThree = Stats.median(array[size // 2:])
        return [qOne, qTwo, qThree]

    # Skewness
    @staticmethod
    def skew(array):
        mean = Stats.mean(array)
        median = Stats.median(array)
        stdev = Stats.standardDeviation(array)
        diff = Subtraction.difference(mean, median)
        numerator = Exponentiation.power(diff, 3)
        return Division.quotient(numerator, stdev)

    # Sample Correlation
    @staticmethod
    def correlationS(array):
        x = array[0]
        y = array[1]
        meanX = Stats.mean(x)
        meanY = Stats.mean(y)
        numerator = 0
        for index in range(len(x)):
            xdiff = Subtraction.difference(x[index], meanX)
            ydiff = Subtraction.difference(y[index], meanY)
            numerator += Multiplication.product(xdiff, ydiff)
        covariance = Division.quotient(numerator, len(x))
        stdX = Stats.standardDeviation(x)
        stdY = Stats.standardDeviation(y)
        return Division.quotient(covariance, (Multiplication.product(stdX, stdY)))

    # Population Correlation
    @staticmethod
    def correlationP(array):
        x = array[0]
        y = array[1]
        meanX = Stats.mean(x)
        meanY = Stats.mean(y)
        numerator = 0
        for index in range(len(x)):
            xdiff = Subtraction.difference(x[index], meanX)
            ydiff = Subtraction.difference(y[index], meanY)
            numerator += Multiplication.product(xdiff, ydiff)
        covariance = Division.quotient(numerator, (len(x)) - 1)
        stdX = Stats.standardDeviation(x)
        stdY = Stats.standardDeviation(y)
        return Division.quotient(covariance, (Multiplication.product(stdX, stdY)))

    # Z - Score
    @staticmethod
    def zscore(array):
        return stats.zscore(array)

    # Mean Deviation/ Mean Absolute Deviation
    @staticmethod
    def meanDeviation(array):
        mean = Stats.mean(array)
        numerator = 0
        for elem in array:
            numerator += abs(Subtraction.difference(elem, mean))
        return Division.quotient(numerator, len(array))