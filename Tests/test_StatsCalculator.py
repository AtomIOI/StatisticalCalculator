import unittest
from Calculator.StatsCalculator import StatsCalculator


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = StatsCalculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, StatsCalculator)

if __name__ == '__main__':
    unittest.main()
