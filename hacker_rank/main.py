#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'oddNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def oddNumbers(l, r):
    # Write your code here
    for x in range(l, r+1):
        if x % 2 == 1:
            print(str(x))


if __name__ == '__main__':
    oddNumbers(3, 9)
