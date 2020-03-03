import random


class RNG:
    # 1. Generate a random number without a seed between a range of two numbers - Both Integer and Decimal
    @staticmethod
    def randINT(lowest, highest):
        return random.randrange(lowest, highest)

    @staticmethod
    def randFLT(lowest, highest):
        return random.uniform(lowest, highest)

    # 2. Generate a random number with a seed between a range of two numbers - Both Integer and Decimal
    @staticmethod
    def prandINT(lowest, highest, seed):
        random.seed(seed)
        return random.randrange(lowest, highest)

    @staticmethod
    def prandFLT(lowest, highest, seed):
        random.seed(seed)
        return random.uniform(lowest, highest)

    # 3. Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
    @staticmethod
    def prandINTL(lowest, highest, n, seed):
        result = []
        random.seed(seed)
        for i in range(n):
            result.append(random.randrange(lowest, highest))
        return result

    @staticmethod
    def prandFLTL(lowest, highest, n, seed):
        result = []
        random.seed(seed)
        for i in range(n):
            result.append(random.uniform(lowest, highest))
        return result

    # 4. Select a random item from a list
    @staticmethod
    def randElem(arr):
        return arr[random.randrange(0, len(arr))]

    # 5. Set a seed and randomly select the same value from a list
    @staticmethod
    def prandElem(arr, seed):
        random.seed(seed)
        return arr[random.randrange(0, len(arr))]

    # 6. Select N number of items from a list without a seed
    @staticmethod
    def randElems(arr, n):
        result = []
        for i in range(n):
            result.append(arr[random.randrange(0, len(arr))])
        return result

    # 7.  Select N number of items from a list with a seed
    @staticmethod
    def prandElems(arr, n, seed):
        random.seed(seed)
        result = []
        for i in range(n):
            result.append(arr[random.randrange(0, len(arr))])
        return result
