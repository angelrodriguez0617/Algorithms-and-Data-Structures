class Dictionary:

    def __init__(self):
        self.capacity = 10
        self.storage = [None] * self.capacity
        self._count = 0

    def insert(self, key, value):
        if self.loadfactor() > 0.75:
            self.rehash()
        index = hash(key) % self.capacity
        if self.storage[index] is None:
            self.storage[index] = [(key, value)]
        else:
            self.storage[index].append[(key, value)]
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

    def find(self, key):
        index = hash(key) % self.capacity
        while self.storage[index] != key and self.storage[index] is not None:
            index += 1
            if index >= self.capacity:
                index = 0
        if self.storage[index] is None:
            raise KeyError
        return self.storage[index][1]

    def remove(self, key):
        index = hash(key) % self.capacity
        if self.storage[index] is not None:
            chain = self.storage[index]
            for i in range(len(self.storage[index])):
                if chain[i][0] == key:
                    chain.pop(i)
                    self._count -= 1
            if len(chain) == 0:
                self.storage[index] = None

    def count(self):
        return self._count

    def __str__(self):
        return str(self.storage)

    def loadfactor(self):
        return self._count / self.capacity

    def is_empty(self):
        return self._count == 0


dictionary = Dictionary()
dictionary.insert("Donald" "Duck")
dictionary.insert("Mickey" "Mouse")
dictionary.insert("Goofy" "Dog")
dictionary.insert("Goofy," "Dog")
print(dictionary)

