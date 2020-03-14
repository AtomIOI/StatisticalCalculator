import math
from scipy import stats


class Stats:
    # Mean
    @staticmethod
    def mean(array):
        total = 0
        for num in array:
            total = total + num
        return total / len(array)

    # Median
    @staticmethod
    def median(array):
        array.sort()
        size = len(array)
        if size % 2 == 0:
            medOne = array[(size // 2) - 1]
            medTwo = array[size // 2]
            return (medOne + medTwo) / 2
        return array[math.floor(size / 2)]

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
            varianceTotal += math.pow(num - mean, 2)
        return varianceTotal / len(array)

    # Standard Deviation
    @staticmethod
    def standardDeviation(array):
        return math.pow(Stats.variance(array), .5)

    # Quartiles
    @staticmethod
    def quartiles(array):
        array.sort()
        size = len(array)
        if size % 2 == 0:
            medOne = array[(size // 2) - 1]
            medTwo = array[size // 2]
            qTwo = (medOne + medTwo) / 2
            qOne = Stats.median(array[:size // 2])
            qThree = Stats.median(array[size // 2:])
        else:
            qTwo = array[math.floor(size / 2)]
            qOne = Stats.median(array[:(size // 2) + 1])
            qThree = Stats.median(array[size // 2:])
        return [qOne, qTwo, qThree]

    # Skewness
    @staticmethod
    def skew(array):
        mean = Stats.mean(array)
        median = Stats.median(array)
        stdev = Stats.standardDeviation(array)
        diff = mean - median
        numerator = math.pow(diff, 3)
        return numerator / stdev

    # Sample Correlation
    @staticmethod
    def correlationS(array):
        x = array[0]
        y = array[1]
        meanX = Stats.mean(x)
        meanY = Stats.mean(y)
        numerator = 0
        for index in range(len(y)):
            xdiff = (x[index] - meanX)
            ydiff = (y[index] - meanY)
            numerator += (xdiff * ydiff)
        covariance = numerator / len(x)
        stdX = Stats.standardDeviation(x)
        stdY = Stats.standardDeviation(y)
        return covariance / (stdX * stdY)

    # Population Correlation
    @staticmethod
    def correlationP(array):
        x = array[0]
        y = array[1]
        meanX = Stats.mean(x)
        meanY = Stats.mean(y)
        numerator = 0
        for index in range(len(y)):
            xdiff = (x[index] - meanX)
            ydiff = (y[index] - meanY)
            numerator += (xdiff * ydiff)
        covariance = numerator / (len(x) - 1)
        stdX = Stats.standardDeviation(x)
        stdY = Stats.standardDeviation(y)
        return covariance / (stdX * stdY)

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
            numerator += abs(elem - mean)
        return numerator / len(array)