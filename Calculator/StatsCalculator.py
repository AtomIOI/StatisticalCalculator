from Functions.Random import RNG


class StatsCalculator:
    Result = 0

    def __init__(self):
        pass

    def randINT(self, a, b):
        self.Result = RNG.randINT(a, b)
        return self.Result

    def randFLT(self, a, b):
        self.Result = RNG.randFLT(a, b)
        return self.Result

    def prandINT(self, a, b, c):
        self.Result = RNG.prandINT(a, b, c)
        return self.Result

    def prandFLT(self, a, b, c):
        self.Result = RNG.prandFLT(a, b, c)
        return self.Result
