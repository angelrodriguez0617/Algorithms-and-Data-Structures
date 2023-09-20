class LPDictionary:

    def __init__(self):
        self.capacity = 10
        self.storage = [None] * self.capacity
        self._count = 0

    def insert(self, key, value):
        if self.loadfactor() > 0.75:
            self.rehash()
        index = hash(key) % self.capacity
        while self.storage[index] is not None and self.storage[index][0] != key:
            index = self._incrementWrap(index)
        if self.storage is not None and self.storage[index][0] == key:
            self.storage[index][1] = value
        else:
            self.storage[index] = [key, value]  
            self._count += 1

    def rehash(self):
        temp = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity
        for pair in temp:
            if pair is not None:
                self.insert(pair[0], pair[1])

    def keys(self):
        pass

    def _incrementWrap(self, i):
        i += 1
        if i >= self.capacity:
            i = 0
        return i

    def _find(self, key):
        index = hash(key) % self.capacity
        while self.storage[index][0] != key and self.storage[index] is not None:
            index += 1
            if index >= self.capacity:
                index = 0
        return index

    def find(self, key):
        index = self._find(key)
        if self.storage[index] is None:
            raise KeyError
        return self.storage[index][1]

    def remove(self, key):
        index = self._find(key)
        self.storage[index] = None
        index += 1
        temp = []
        while self.storage[index] is not None:
            temp.append(self.storage[index])


    def count(self):
        return self._count

    def __str__(self):
        return str(self.storage)

    def loadfactor(self):
        return self._count / self.capacity

    def is_empty(self):
        return self._count == 0


# dictionary = LPDictionary()
# dictionary.insert("Donald" "Duck")
# dictionary.insert("Mickey" "Mouse")
# dictionary.insert("Goofy" "Dog")
# dictionary.insert("Goofy," "Dog")
# print(dictionary)
