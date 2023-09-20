from lpdDictionary import LPDictionary


def myhash(x):
    result = 0
    for char in x:
        result += ord(char)
    return result % 100

    def identity_hash(x):
        return x

    def modulus_hash(x):
        return x % 100

    def bitwise_hash(x):
        return x & 500

    def folding_hash(x):
        current = x
        finalresult = 0
        while current > 0:
            finalresult |= current % 100
            current //= 100
        return finalresult % 500

    def middle_and_ends(x):
        length = len(x)
        if length >= 3:
            first = x[0]
            last = x[-1]
            middle = x[length // 2]
            return ((ord(first)) + (ord(middle) ** 2) + (ord(last) ** 3)) % 500
        return 0

    def character_folding_hash(x):
        finalresult = 0
        multiplier = 1
        for char in x:
            finalresult += ord(char) * multiplier
            multiplier += 1
        return finalresult


class myClass:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.age = 0

    def __hash__(self):
        return hash(self.name) + hash(self.address) + hash(self.age)


#
# print(identity_hash('c'))
# print(myhash("Baz"))
# w = "population"
# print(middle_and_ends(w))

recordedWeight = LPDictionary()


def total_weight(x, y):
    try:
        return recordedWeight.find((x, y))
    except:
        if x < 0 or y < 0 or x > y:
            return 0
        else:
            value = 200 + weight_on_r(x - 1, y - 1) / 2 + weight_on_r(x, y - 1) / 2
            recordedWeight.find((x, y), value)
            return value


def weight_on(y, x):
    return weight_on_r(x - 1, y - 1) / 2 + weight_on_r(x, y - 1) / 2


def weight_on_r(y, x):
    if x < 0 or y < 0 or x > y:
        return 0
    return 200 + weight_on_r(x - 1, y - 1) / 2 + weight_on_r(x, y - 1) / 2


for y in range(10):
    for x in range(y + 1):
        print(weight_on(x, y), end=" ")
    print()
