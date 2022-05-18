from itertools import combinations


class StringClass:
    def __init__(self, value):
        self.str = value

    def length(self):
        return len(self.str)

    def tolist(self, value):
        list1 = list(value)
        return list1

class PairsPossible(StringClass):
    def __init__(self,value):
        self.str = value
    def pairs(self):
        pair = list(combinations(self.str, 2))
        return pair

class SearchCommonElements(StringClass):
    def __init__(self,str1,str2):
        self.str1 = str1
        self.str2 = str2

    def commonElements(self):
        removed = list(set(self.str1) & set(self.str2))
        return removed
