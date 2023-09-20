'''This is Project 1'''

import random
import math
import time


def linear_search(lyst, target):
    """A linear search function"""
    for i in range(len(lyst)):
        if lyst[i] == target:
            return True
        if lyst[i] > target:
            return False
    return False


def binary_search(lyst, target):
    """A linear search function which checks values sequentially"""
    length = len(lyst)
    if length == 0:
        return False
    middle = length // 2
    if lyst[middle] == target:
        return True
    elif lyst[middle] > target:
        return binary_search(lyst[:middle], target)
    elif lyst[middle] < target:
        return binary_search(lyst[middle + 1:], target)


def jump_search(lyst, target):
    """A jump search algorithm """
    length = len(lyst)
    interval = int(math.sqrt(length))
    i = 0
    while i < length:
        if lyst[i] == target:
            return True
        i += interval
        if i >= length or lyst[i] > target:
            break
    i -= interval
    j = i
    while j < (i + interval):
        if lyst[j] == target:
            return True
        j += 1
    return False


def get_lyst():
    """Creates a random list of 1000000 values up to a magnitude of 10000000"""
    result = random.sample(range(10000000), 1000000)
    return sorted(result)


def main():
    """Main function to run each search, time each run, and report results to the console"""
    myLyst = get_lyst()
    start = time.perf_counter()
    linear_search(myLyst, myLyst[0])
    end = time.perf_counter()
    print("Linear took", format(end - start, ".7f"), "seconds to find the first element of the sorted array")
    start = time.perf_counter()
    linear_search(myLyst, myLyst[len(myLyst) // 2])
    end = time.perf_counter()
    print("Linear took", format(end - start, ".7f"), "seconds to find a number at the middle of the sorted array")
    start = time.perf_counter()
    linear_search(myLyst, myLyst[-1])
    end = time.perf_counter()
    print("Linear took", format(end - start, ".7f"), "seconds to find a number at the end of the sorted array")
    start = time.perf_counter()
    linear_search(myLyst, -1)
    end = time.perf_counter()
    print("Linear took", format(end - start, ".7f"), "seconds to find a number NOT in the array")
    print()

    start = time.perf_counter()
    binary_search(myLyst, myLyst[0])
    end = time.perf_counter()
    print("Binary took", format(end - start, ".7f"), "seconds to find the first element of the sorted array")
    start = time.perf_counter()
    binary_search(myLyst, myLyst[len(myLyst) // 2])
    end = time.perf_counter()
    print("Binary took", format(end - start, ".7f"), "seconds to find a number at the middle of the sorted array")
    start = time.perf_counter()
    binary_search(myLyst, myLyst[-1])
    end = time.perf_counter()
    print("Binary took", format(end - start, ".7f"), "seconds to find a number at the end of the sorted array")
    start = time.perf_counter()
    binary_search(myLyst, -1)
    end = time.perf_counter()
    print("Binary took", format(end - start, ".7f"), "seconds to find a number NOT in the array")
    print()

    start = time.perf_counter()
    jump_search(myLyst, myLyst[0])
    end = time.perf_counter()
    print("Jump took", format(end - start, ".7f"), "seconds to find the first element of the sorted array")
    start = time.perf_counter()
    jump_search(myLyst, myLyst[len(myLyst) // 2])
    end = time.perf_counter()
    print("Jump took", format(end - start, ".7f"), "seconds to find a number at the middle of the sorted array")
    start = time.perf_counter()
    jump_search(myLyst, myLyst[-1])
    end = time.perf_counter()
    print("Jump took", format(end - start, ".7f"), "seconds to find a number at the end of the sorted array")
    start = time.perf_counter()
    jump_search(myLyst, -1)
    end = time.perf_counter()
    print("Jump took", format(end - start, ".7f"), "seconds to find a number NOT in the array")


main()
