class HashMap:
    """Hash Map class, my own dictionary type"""

    def customhash(self, value):
        """My own has function for keys"""
        if isinstance(value, tuple):
            return value[0] * 17 + value[1] * 3

    def __init__(self):
        """HashMap class initializer"""
        self._capacity = 7
        self.storage = [None] * self._capacity
        self._count = 0

    def set(self, key, value):
        """The insert function for the HashMap class"""
        index = self.customhash(key) % self._capacity
        while self.storage[index] is not None and self.storage[index][0] != key:
            index = self._incrementWrap(index)
        if self.storage[index] is not None and self.storage[index][0] == key:
            self.storage[index][1] = value
        else:
            self.storage[index] = [key, value]
            self._count += 1
        if self.loadfactor() >= 0.8:
            self.rehash()

    def rehash(self):
        """Rehash function which is similar to re-balancing a tree"""
        temp = self.storage
        self._capacity *= 2
        self._capacity -= 1
        self._count = 0
        self.storage = [None] * self._capacity
        for pair in temp:
            if pair is not None:
                # pylint: disable=E1136
                self.set(pair[0], pair[1])

    def keys(self):
        """Returns a list of keys"""
        result = []
        for item in self.storage:
            # pylint: disable=E1136
            if item is not None:
                result.append(item[0])
        return result

    def _incrementWrap(self, i):
        """Operation which increments wraps"""
        i += 1
        if i >= self._capacity:
            i = 0
        return i

    def _find(self, key):
        """Used by remove function to find values before removing"""
        index = self.customhash(key) % self._capacity
        while self.storage[index] is not None and self.storage[index][0] != key:
            index = self._incrementWrap(index)
        return index

    def get(self, key):
        """ Return the value for key if key is in the dictionary. If key is not in the dictionary,
             raise a KeyError."""
        index = self._find(key)
        if self.storage[index] is None:
            raise KeyError
        return self.storage[index][1]

    def remove(self, key):
        """Remove the key and its associated value from the map. If the key does not exist,
            nothing happens. Do not rehash the table after deleting keys"""
        index = self._find(key)
        if self.storage[index][0] != key:
            return
        self.storage[index] = None
        self._count -= 1
        index += 1
        temp = []
        while self.storage[index] is not None:
            temp.append(self.storage[index])
            self.storage[index] = None
            self._count -= 1
            index = self._incrementWrap(index)
        for item in temp:
            self.set(item[0], item[1])

    def size(self):
        """ Return the number of key-value pairs in the map"""
        return self._count

    def __str__(self):
        """Returns the HashMap in strings"""
        return str(self.storage)

    def loadfactor(self):
        """Returns the load factor"""
        return self._count / self._capacity

    def is_empty(self):
        """Returns True if the HashMap is empty and False if not empty"""
        return self._count == 0

    def capacity(self):
        """Returns the capacity of the HashMap"""
        return self._capacity

    def clear(self):
        """Empties the HashMap"""
        self._count = 0
        self._capacity = 7
        self.storage = []

# dictionary = LPDictionary()
# dictionary.insert("Donald" "Duck")
# dictionary.insert("Mickey" "Mouse")
# dictionary.insert("Goofy" "Dog")
# dictionary.insert("Goofy," "Dog")
# print(dictionary)
