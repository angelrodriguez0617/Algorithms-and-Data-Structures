"""Classes and methods to have a functioning BST"""


class BST:
    """Binary Search Tree class"""

    def __init__(self):
        """Constructor for BST class"""
        self.root = None

    def get_root(self):
        """Returns the root node"""
        return self.root

    def set_root(self, node):
        """Defines the root node"""
        self.root = node

    def add(self, item):
        """Will add a new node in a sorted manner"""
        if self.root is None:
            self.root = TreeNode()
            self.root.value = item
        else:
            self.root.add(item)

    def rebalance(self):
        """Evens out the BST"""
        lyst = self.inorder()
        self.root = None
        self.recursive_rebalance(lyst)

    def recursive_rebalance(self, lyst):
        """Recursive function used by the rebalance function"""
        if len(lyst) == 0:
            return
        index = len(lyst) // 2
        self.add(lyst[index])
        self.recursive_rebalance(lyst[:index])
        self.recursive_rebalance(lyst[index + 1:])

    def remove(self, item):
        """Removed node from BST and appropriately rearranged remaining nodes"""
        if self.root is not None:
            self.root.remove(item)
        return self.root

    def find(self, value):
        """Returns searched node if node value exists in BST"""
        if self.root is None:
            raise ValueError
        return self.root.find(value)

    def height(self):
        """Returns the height of the BST"""
        if self.root is None:
            return 0
        return self.root._height() + 1

    def preorder(self):
        """Return a list with the data items in order of pre-order traversal. """
        result = []
        if self.root is not None:
            result += self.root.preorder()
        return result

    def inorder(self):
        """Return a list with the data items in order of in-order traversal. """
        result = []
        if self.root is not None:
            result += self.root.inorder()
        return result

    def postorder(self):
        """Return a list with the data items in order of post-order traversal."""
        result = []
        if self.root is not None:
            result += self.root.postorder()
        return result

    def __str__(self):
        """Prints a decent looking BST that is readable"""
        result = ""
        itemwidth = 9
        minspace = 1
        maxwidth = (2 ** self.height()) * (itemwidth + minspace)
        currentLevel = [self.root]
        nextLevel = []
        line = ""
        nextLevel = []
        line = ""
        nextline = ""
        # pos1 = 0
        # pos2 = 0
        while len(currentLevel) > 0:
            line = ' ' * maxwidth
            for node in currentLevel:
                name, position = node._hierarchy_str(maxwidth, itemwidth)
                line = line[:int(position)] + name + line[int(position + itemwidth):]
                if node.left is not None:
                    nextLevel.append(node.left)
                if node.right is not None:
                    nextLevel.append(node.right)
            result += line + "\n"
            currentLevel = nextLevel
            nextLevel = []
        return result

    def size(self):
        """Return the number of items in the tree."""
        if self.root is None:
            return 0
        return self.root._size() + 1

    def is_empty(self):
        """Return True if empty, False otherwise"""
        if self.size() == 0:
            return True
        return False


class TreeNode:
    """Class for nodes which make up the BST"""

    def __init__(self, parent=None):
        self.parent = parent
        self.left = None
        self.right = None
        self.value = None
        self.position = 0

    def _size(self):
        """Returns the size of the tree starting from the given node"""
        left_subtree = 0
        right_subtree = 0
        if self.left is not None:
            left_subtree += 1 + self.left._size()
        if self.right is not None:
            right_subtree += 1 + self.right._size()
        tree_size = left_subtree + right_subtree
        return tree_size

    def get_left_child(self):
        """Returns left child of given node"""
        return self.left

    def get_right_child(self):
        """Returns right child of given node"""
        return self.right

    def set_root_val(self, value):
        """Sets the root value of a BST"""
        self.value = value

    def get_root_val(self):
        """Returns the root value"""
        return self.value

    def add(self, value):
        """Makes sure the added node is placed in the correct sorted position"""
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(self)
                self.left.value = value
                self.left.position = (self.position * 2)
            else:
                self.left.add(value)
        else:
            if self.right is None:
                self.right = TreeNode(self)
                self.right.value = value
                self.right.position = (self.position * 2) + 1
            else:
                self.right.add(value)

    def level(self):
        """Returns the level of a given tree node"""
        if self.parent is None:
            return 0
        return self.parent.level() + 1

    def position(self):
        """Returns the position of a given tree node"""
        return self.position

    def replace(self, olditem, newitem):
        """Replaces a given node with a user chosen node"""
        if self.left is olditem:
            self.left = newitem
        elif self.right is olditem:
            self.right = newitem

    def remove(self, item):
        """Removes a given node from a tree"""
        if self.value == item:
            self.perform_remove(item)
        elif self.value > item and self.left is not None:
            self.get_left_child().remove(item)
        elif self.value < item and self.right is not None:
            self.get_right_child().remove(item)

    def perform_remove(self, item):
        """Used to aid in the node removal process of the remove function"""
        if self.left is None and self.right is not None:
            self.parent.replace(self, self.right)
        elif self.right is None and self.left is not None:
            self.parent.replace(self, self.left)
        elif self.right is None and self.left is None:
            self.parent.replace(self, None)
        else:
            smallest = self.right.inorder()[0]
            self.value = smallest
            self.right.remove(smallest)
            # largest = self.left.inorder()[-1]
            # self.value - largest
            # self.left.remove(largest)

    def find(self, value):
        """Return the given value if that value exists within the tree"""
        if self.value == value:
            return self.value
        if self.value > value and self.left is not None:
            return self.left.find(value)
        if self.value < value and self.right is not None:
            return self.right.find(value)
        raise ValueError

    def inorder(self):
        """Return a list with the data items in order of in-order traversal. """
        result = []
        if self.left is not None:
            result += self.left.inorder()
        result.append(self.value)
        if self.right is not None:
            result += self.right.inorder()
        return result

    def preorder(self):
        """Return a list with the data items in order of pre-order traversal. """
        result = []
        result.append(self.value)
        if self.left is not None:
            result += self.left.preorder()
        if self.right is not None:
            result += self.right.preorder()
        return result

    def postorder(self):
        """Return a list with the data items in order of post-order traversal."""
        result = []
        if self.left is not None:
            result += self.left.postorder()
        if self.right is not None:
            result += self.right.postorder()
        result.append(self.value)
        return result

    def _hierarchy_str(self, maxwidth, itemwidth):
        """Used to print a tree in the form of a tree shape"""
        linestart = maxwidth / (2 ** (self.level() + 1))
        linespacing = ((linestart * 2) * self.position) - itemwidth // 2
        name = (str(self.value)[:itemwidth]).center(itemwidth)
        return name, linestart + linespacing

    def __str__(self):
        """Used to print a tree node"""
        return str(self.value)

    def _height(self):
        """Returns the maximum level of a tree"""
        if self.left is None and self.right is None:
            return self.level()
        if self.left is None:
            return self.right._height()
        elif self.right is None:
            return self.left._height()
        return max(self.left._height(), self.right._height())

# tree = BST()
# tree.add(73)
# tree.add(19)
# tree.add(215)
# tree.add(1)
# tree.add(11)
# tree.add(19)
# tree.add(-20)
# tree.add(128)
# tree.add(158)
# tree.add(8)
# tree.add(13)
# print(tree)
# tree.rebalance
# print(tree)
