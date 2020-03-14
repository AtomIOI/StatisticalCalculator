import math
from scipy import stats
from Functions.Random import RNG
from Functions.Statistics import Stats


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
            index = len(array) // n
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
        se = stdev / math.pow(len(array), .5)
        numerate = se * tval
        mean = Stats.mean(array)
        return [mean - numerate, mean + numerate]

    # Margin of Error
    @staticmethod
    def marginError(stdev, ci, n):
        df = n - 1
        alpha = 1 - ci
        tval = stats.t.ppf(1 - alpha, df)
        se = stdev / math.pow(n, .5)
        return tval * se

    # Cochran’s Sample Size Formula
    @staticmethod
    def cochran(array, e, p):
        df = len(array) - 1
        zscore = stats.t.ppf(e, df)
        q = 1 - p
        exp = math.pow(zscore, 2)
        numerator = (p * q) * exp
        return numerator / math.pow(e, 2)

    # How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation)
    @staticmethod
    def unknown_pop_sample(data, percent):
        zs = Stats.zscore(data)
        me = Sampling.marginError(data)
        p = percent
        q = (1 - p)

        val = (zs / me)
        samplePop = math.sqrt(val) * p * q

        return samplePop

    # How to Find a Sample Size Given a Confidence Interval and Width (known population standard deviation)
    @staticmethod
    def known_pop_sample(data):
        zs = Stats.zscore(data)
        me = Sampling.marginError(data)
        sd = Stats.standardDeviation(data)

        value = (zs * sd) / me

        popSample = math.sqrt(value)

        return popSample
