import random
import math
import time


def get_lyst():
    """Creates a random list of 20000 values up to a magnitude of 20000"""
    result = random.sample(range(20000), 20000)
    return result


def bubble_sort(lyst):
    """Bubble sort algorithm"""
    assignments = 0
    for i in range(len(lyst)):
        for j in range(len(lyst) - 1, i, -1):
            if lyst[j] < lyst[j - 1]:
                assignments += 1
                lyst[j - 1], lyst[j] = lyst[j], lyst[j - 1]
    print(assignments)


def selection_sort(lyst):
    """Selection sort algorithm"""
    length = len(lyst)
    for j in range(length):
        minimum = length - 1
        for i in range(length - 1, j - 1, -1):
            if lyst[i] < lyst[minimum]:
                minimum = i
        lyst[j], lyst[minimum] = lyst[minimum], lyst[j]
    return lyst


def insertion_sort(lyst):
    """insertion sort algorithm"""
    length = len(lyst)
    for i in range(1, length):
        while i > 0 and lyst[i - 1] > lyst[i]:
            lyst[i - 1], lyst[i] = lyst[i], lyst[i - 1]
            i -= 1
    return lyst


def mergesort(lyst):
    """Merge sort algorithm"""
    # divide
    length = len(lyst)
    if length > 1:
        mid = length // 2
        left = lyst[:mid]
        right = lyst[mid:]

        mergesort(left)
        mergesort(right)
        # conquer
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lyst[k] = left[i]
                i += 1
            else:
                lyst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lyst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lyst[k] = right[j]
            j += 1
            k += 1
    return lyst


def shell_sort(lyst):
    """Shell sort algorithm"""
    length = len(lyst)
    gap = length // 2

    while gap > 0:
        for j in range(gap):
            for i in range(gap + j, length, gap):
                while i > 0 and lyst[i - gap] > lyst[i]:
                    lyst[i - gap], lyst[i] = lyst[i], lyst[i - gap]
                    i -= gap

        gap = gap // 2
    return lyst


def partition(numbers, start_index, end_index):
    """Cuts a list into two parts"""
    # Select the middle value as the pivot.
    midpoint = start_index + (end_index - start_index) // 2
    pivot = numbers[midpoint]

    # "low" and "high" start at the ends of the list segment
    # and move towards each other.
    low = start_index
    high = end_index

    done = False
    while not done:
        # Increment low while numbers[low] < pivot
        while numbers[low] < pivot:
            low = low + 1

        # Decrement high while pivot < numbers[high]
        while pivot < numbers[high]:
            high = high - 1

        # If low and high have crossed each other, the loop
        # is done. If not, the elements are swapped, low is
        # incremented and high is decremented.
        if low >= high:
            done = True
        else:
            temp = numbers[low]
            numbers[low] = numbers[high]
            numbers[high] = temp
            low = low + 1
            high = high - 1

    # "high" is the last index in the left segment.
    return high


def quick_sort(numbers, start_index, end_index):
    """Quick sort algorithm which requires three parameters"""
    # Only attempt to sort the list segment if there are
    # at least 2 elements
    if end_index <= start_index:
        return

    # Partition the list segment
    high = partition(numbers, start_index, end_index)

    # Recursively sort the left segment
    quick_sort(numbers, start_index, high)

    # Recursively sort the right segment
    quick_sort(numbers, high + 1, end_index)


def quicksort(lyst):
    """Quick sort algorithm that only requires one parameter"""
    end_index = len(lyst) - 1
    quick_sort(lyst, 0, end_index)
    return lyst


def is_sorted(lyst):
    """Checks if list is sorted AND contains integers only"""
    for i in range(1, len(lyst)):
        if lyst[i - 1] > lyst[i]:
            return False
        if not isinstance(lyst[i], int):
            return isinstance(lyst[i-1], int)
    return True


def main():
    """non-interactive main function that runs each sort, times each run, and
    reports the results to the console."""

    # This is so all sort algorithms sort the exact same list and the results can easily portray varying
    # efficiencies
    my_lyst = get_lyst()
    print("my_lyst is sorted?", is_sorted(my_lyst))
    print()

    temp_lyst = my_lyst.copy()
    print("starting selection_sort")
    start = time.perf_counter()
    selection_sort(temp_lyst)
    end = time.perf_counter()
    print("selection_sort duration:", format(end - start, ".7f"))
    print("List is sorted?", is_sorted(temp_lyst))
    print()

    temp_lyst = my_lyst.copy()
    print("starting insertion_sort")
    start = time.perf_counter()
    insertion_sort(temp_lyst)
    end = time.perf_counter()
    print("insertion_sort duration:", format(end - start, ".7f"))
    print("List is sorted?", is_sorted(temp_lyst))
    print()

    temp_lyst = my_lyst.copy()
    print("starting mergesort")
    start = time.perf_counter()
    mergesort(temp_lyst)
    end = time.perf_counter()
    print("mergesort duration:", format(end - start, ".7f"))
    print("List is sorted?", is_sorted(temp_lyst))
    print()

    temp_lyst = my_lyst.copy()
    print("starting quicksort")
    start = time.perf_counter()
    quicksort(temp_lyst)
    end = time.perf_counter()
    print("quicksort duration:", format(end - start, ".7f"))
    print("List is sorted?", is_sorted(temp_lyst))
    print()

    temp_lyst = my_lyst.copy()
    print("starting timsort")
    start = time.perf_counter()
    temp_lyst = sorted(temp_lyst)
    end = time.perf_counter()
    print("timsort duration:", format(end - start, ".7f"))
    print("List is sorted?", is_sorted(temp_lyst))


main()
