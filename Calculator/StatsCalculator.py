from Functions.Statistics import Stats
from Functions.Sampling import Sampling


class StatsCalculator:
    Result = 0

    def __init__(self):
        pass

    def Mean(self, a):
        self.Result = Stats.mean(a)
        return self.Result

    def Median(self, a):
        self.Result = Stats.median(a)
        return self.Result

    def Mode(self, a):
        self.Result = Stats.mode(a)
        return self.Result

    def Variance(self, a):
        self.Result = Stats.variance(a)
        return self.Result

    def Standarddeviation(self, a):
        self.Result = Stats.standardDeviation(a)
        return self.Result

    def Quartiles(self, a):
        self.Result = Stats.quartiles(a)
        return self.Result

    def Skewness(self, a):
        self.Result = Stats.skew(a)
        return self.Result

    def SampleCorrelation(self, a):
        self.Result = Stats.correlationS(a)
        return self.Result

    def PopulationCorrelation(self, a):
        self.Result = Stats.correlationP(a)
        return self.Result

    def ZScore(self, a):
        self.Result = Stats.zscore(a)
        return self.Result

    def MeanAbsoluteDeviation(self, a):
        self.Result = Stats.meanDeviation(a)
        return self.Result

    def SimpleRandomSampling(self, a, b):
        self.Result = Sampling.simpleSample(a, b)
        return self.Result

    def SystematicSampling(self, a, b):
        self.Result = Sampling.systematicSample(a, b)
        return self.Result

    def ConfidenceInterval(self, a, b):
        self.Result = Sampling.confidenceInterval(a, b)
        return self.Result

    def MarginError(self, a, b, c):
        self.Result = Sampling.marginError(a, b, c)
        return self.Result

    def Cochran(self, a, b, c):
        self.Result = Sampling.cochran(a, b, c)
        return self.Result

    def SampleSizeUnknown(self, a, b):
        self.Result = Sampling.unknown_pop_sample(a, b)
        return self.Result

    def SampleSizeKnown(self, a):
        self.Result = Sampling.known_pop_sample(a)
        return self.Result
