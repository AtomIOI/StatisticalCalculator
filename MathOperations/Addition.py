class Addition:
    @staticmethod
    def sum(augend, addend):
        return augend + addend

    @staticmethod
    def sumlist(list):
        result = 0
        for value in list:
            result = Addition.sum(value, result)
        return result
