from bst import BST
from bst import TreeNode
"""Imports from bst.py"""

class Pair:
    """Used since the data at each node needs to account for both a letter and its count"""

    def __init__(self, letter, count=1):
        self.letter = letter
        self.count = count

    def __eq__(self, other):
        return self.letter == other.letter

    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count}'

    def __str__(self):
        return f'({self.letter}, {self.count}'


def make_tree():
    """returns a tree constructed from the input file"""
    bst = BST()
    file = open("C:\\Users\\angel\\Downloads\\around-the-world-in-80-days-3.txt")
    while 1:
        char = file.read(1)
        if not char:
            break
        if not char.isalnum():
            continue
        newPair = Pair(char)
        try:
            pair = bst.find(newPair)
            pair.count += 1
        except ValueError:
            bst.add(newPair)
    file.close()
    return bst


def main():
    """must implement a function make_tree, which takes no parameters but
    returns a tree constructed from the input file"""
    value = make_tree()
    print(value)
    value.rebalance()
    print(value)
