class Stack:
    """Class for stack data structure (first in last out)"""
    def __init__(self):
        self.list = LinkedList()

    def push(self, new_item):
        """Enters a node into the head of the stack"""
        # Create a new node to hold the item
        new_node = Node(new_item)
        # Insert the node as the list head (top of stack)
        self.list.prepend(new_node)

    def pop(self):
        """Removed the head node of a stack and returns the value of that node"""
        if self.list.head is None:
            raise IndexError('Stack is already empty.')
        # Copy data from list's head node (stack's top node)
        popped_item = self.list.head.data
        # Remove list head
        self.list.remove_after(None)
        # Return the popped item
        return popped_item

    def top(self):
        """Lets user know the head value of the stack without removing it"""
        if self.list.head is None:
            raise IndexError('Stack is already empty.')
        current_node = self.list.head
        if current_node is not None:
            return self.list.head.data
        else:
            return None

    def size(self):
        """Returns the size of the stack"""
        count = 0
        current_node = self.list.head
        if current_node is not None and self.list.tail is not None:
            while current_node is not self.list.tail.next:
                current_node = current_node.next
                count += 1
        return count

    def clear(self):
        """Pops the stack until the stack has been cleared entirely"""
        while int(self.size()) > 0:
            self.pop()

    def is_empty(self):
        """Returns True if the stack is empty"""
        return self.list.head is None and self.list.tail is None


class Node:
    """Class for nodes which is used in linked lists class"""
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None


class LinkedList:
    """Class for linked lists and used for the stack class"""
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        """Added node becomes the tail"""
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, new_node):
        """Added node becomes the head"""
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, current_node, new_node):
        """Insterts a node after a certain node"""
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    def remove_after(self, current_node):
        """Removed node after a certain value"""
        # Special case, remove head
        if (current_node is None) and (self.head is not None):
            succeeding_node = self.head.next
            self.head = succeeding_node
            if succeeding_node is None:  # Removed last item
                self.tail = None
        elif current_node.next is not None:
            succeeding_node = current_node.next.next
            current_node.next = succeeding_node
            if succeeding_node is None:  # Removed tail
                self.tail = current_node
