import current as current

from course import Course


class CourseList:
    def __init__(self):
        self.head = None
        self.count = 0
        self.currentItem = None

    def insert(self, course):
        """Insert method that keeps the course list sorted by the course numbers"""
        if self.head is None:
            # Course list is empty
            self.head = course
            self.insert(Course(9999999999))
        else:
            # Course list is not empty
            current_node = self.head
            prev = None
            while current_node is not None and course.number() > current_node.number():
                # Course number is greater than the current node's number
                prev = current_node
                current_node = current_node.next
            if prev is None:
                # Course number goes before the head
                course.next = current_node
                self.head = course
            else:
                prev.next = course
                course.next = current_node
        self.count += 1
        # print(self)
        # print(self.count)

    def print_list(self):
        current_node = self.head
        while current_node is not None and current_node.number() != 9999999999:
            print(current_node)
            current_node = current_node.next
        # print("~End of list~")

    def remove(self, number):
        self._remove(number)

    def _remove(self, number):
        current_node = self.head
        prev = None
        while current_node is not None and current_node.number() != number:
            prev = current_node
            current_node = current_node.next
        if current_node is not None:
            if prev is None:
                self.head = current_node.next
            else:
                prev.next = current_node.next
                current_node.next = None
            self.count -= 1
            return True
        return False

    def remove_all(self, number):
        while self._remove(number):
            continue

    def find(self, number):
        current_node = self.head
        index = 0
        while current_node is not None and current_node.number() != number:
            current_node = current_node.next
            index += 1
        if current_node is None:
            return -1
        return current_node

    def size(self):
        if self.head is None:
            return 0
        return self.count - 1

    def calculate_gpa(self):
        if self.count == 0:
            return 0
        totalhours = 0
        totalgpa = 0
        for c in self:
            totalgpa += (c._grade * c.hours)
            totalhours += c.hours
        return totalgpa / totalhours

    def is_sorted(self):
        if self.head is None:
            # raise AttributeError()
            return True
        current_node = self.head.next
        prev = self.head
        # current_node = current_node.head
        while current_node is not None:
            if prev.number() > current_node.number():
                return False
            prev = current_node
            current_node = current_node.next
        return True

    def __str__(self):
        result = ""
        for item in self:
            result += str(item) + "\n"
        return result

    def __iter__(self):
        self.currentItem = self.head
        return self

    def __next__(self):
        if self.currentItem.next is None:
            raise StopIteration
        temp = self.currentItem
        self.currentItem = self.currentItem.next
        return temp
