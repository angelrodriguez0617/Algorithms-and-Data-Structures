"""Pyramid file for Parts 1 and 2"""
import time
from hashmap import HashMap

FUNCTION_CALLS = 0


def total_weight(row, column):
    """Returns the total weight carried by an individual"""
    # try:
    #     return recordedWeight.get((row,column))
    # except:
    global FUNCTION_CALLS
    FUNCTION_CALLS += 1
    if row < 0 or column < 0 or column > row:
        return 0
    value = 200 + total_weight(row - 1, column - 1) / 2 + total_weight(row - 1, column) / 2
    # recordedWeight.insert((x, y), value)
    return value


def weight_on(row, column):
    """""Used to returns the weight on an individual"""""
    return total_weight(row - 1, column - 1) / 2 + total_weight(row - 1, column) / 2


def main():
    """Main function to execute project objectives"""
    global FUNCTION_CALLS
    FUNCTION_CALLS = 0
    rows = 7
    start = time.perf_counter()
    for y_y in range(rows):
        for x_x in range(y_y + 1):
            print(round(weight_on(y_y, x_x), 2), end=" ")
        print()
    end = time.perf_counter()
    print()
    print("Elapsed time:", end - start, "seconds")
    print("Number of function calls:", FUNCTION_CALLS)


# print(weight_on(0, 0))
# print(weight_on(3, 1))
# print()
main()

# Pyramid file for Part 3

FUNCTION_CALLS = 0
RECORDED_WEIGHT = HashMap()


def total_weight2(row, column):
    """Returns the total weight carried by an individual"""
    global FUNCTION_CALLS
    global RECORDED_WEIGHT
    try:
        return RECORDED_WEIGHT.get((row, column))
    except:
        FUNCTION_CALLS += 1
        if row < 0 or column < 0 or column > row:
            return 0
        value = 200 + total_weight2(row-1, column-1) / 2 + total_weight2(row-1, column) / 2
        RECORDED_WEIGHT.set((row, column), value)
        return value


def weight_on2(row, column):
    """""Used to returns the weight on an individual"""""
    return total_weight2(row - 1, column - 1) / 2 + total_weight2(row - 1, column) / 2


def main2():
    """Main function to execute project objectives"""
    global RECORDED_WEIGHT
    global FUNCTION_CALLS
    FUNCTION_CALLS = 0
    RECORDED_WEIGHT.clear()
    rows = 7
    start = time.perf_counter()
    for y_y in range(rows):
        for x_x in range(y_y + 1):
            print(round(weight_on2(y_y, x_x), 2), end=" ")
        print()
        end = time.perf_counter()
        print()
        print("Elapsed time:", end - start, "seconds")
        print("Number of function calls:", FUNCTION_CALLS)


main2()
