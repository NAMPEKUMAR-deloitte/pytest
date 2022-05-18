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

class EqualSumPairs():
    def count(self, list1):
        list2 = []
        for i in list1:
            sum = 0
            for j in i:
                sum += int(j)
            list2.append(sum)
        print("List of unique Sums in possible pairs of string: ")
        print(set(list2))
        return len(set(list2))



value1 = input("Enter String1: ")
obj1 = StringClass(value1)
print("Length of the String: ")
print(obj1.length())
print("List of String: ")
print(obj1.tolist(value1))
obj2 = PairsPossible(value1)
list1=obj2.pairs()
print("Possible Pairs of String1 are: ")
print(list1)
print("-------------------------------------------------------------")

value2 = input("Enter String2: ")
obj3 = PairsPossible(value2)
list2=obj3.pairs()
print("Possible Pairs of String 2 are: ")
print(list2)
print("-------------------------------------------------------------")

obj4=SearchCommonElements(value1,value2)
print("Common Elements between String1 and string2: ")
print(obj4.commonElements())
obj5 = EqualSumPairs()
length=obj5.count(list2)
print("Count of unique sums in possible pairs of string2: ")
print(length)
