import unittest

from Functions.Random import RNG
from Functions.Statistics import Stats
from Functions.Sampling import Sampling


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = RNG.prandINTL(1, 20, 30, 1)
        self.testDataTwo = RNG.prandINTL(1, 20, 29, 1)

    def test_Stats_Mean(self):
        self.assertEqual(9.266666666666667, Stats.mean(self.testData))

    def test_Stats_Median(self):
        self.assertEqual(9.0, Stats.median(self.testData))
        self.assertEqual(9, Stats.median(self.testDataTwo))

    def test_Stats_Mode(self):
        self.assertEqual(1, Stats.mode(self.testData))

    def test_Stats_Variance(self):
        self.assertEqual(37.328888888888876, Stats.variance(self.testData))

    def test_Stats_Standard_Deviation(self):
        self.assertEqual(6.109737219299115, Stats.standardDeviation(self.testData))

    def test_Stats_Quartiles(self):
        result = Stats.quartiles(self.testData)
        self.assertEqual(4, result[0])
        self.assertEqual(9.0, result[1])
        self.assertEqual(15, result[2])

    def test_Stats_Skew(self):
        self.assertEqual(0.003103728079018511, Stats.skew(self.testData))

    def test_Stats_Correlation_Sample(self):
        arr = [self.testData, self.testDataTwo]
        self.assertEqual(0.9729647047577678, Stats.correlationS(arr))

    def test_Stats_Correlation_Population(self):
        arr = [self.testData, self.testDataTwo]
        self.assertEqual(1.0065152118183804, Stats.correlationP(arr))

    def test_Stats_ZScore(self):
        self.assertEqual(-0.6983388177791585, Stats.zscore(self.testData)[0])

    def test_Stats_Mean_Deviation(self):
        self.assertEqual(5.484444444444445, Stats.meanDeviation(self.testData))

    def test_Confidence_Interval(self):
        self.assertEqual([7.734108247895442, 10.799225085437893], Sampling.confidenceInterval(self.testData, .91))

    def test_Margin_Error(self):
        self.assertEqual(-4.2666666666666675, Sampling.marginError(self.testData)[0])

    def test_Cochran(self):
        self.assertEqual(944671.2990750178, Sampling.cochran(self.testData, .001, .91))

    def test_Sample_Size_Unknown_Population(self):
        self.assertEqual(0.03313390601098227, Sampling.unknown_pop_sample(self.testData, .91)[0])

    def test_Sample_Size_Known_Population(self):
        self.assertEqual(1, Sampling.known_pop_sample(self.testData)[0])


if __name__ == '__main__':
    unittest.main()
