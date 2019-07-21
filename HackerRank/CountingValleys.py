#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
# Counts number of times hiker, starting at sea level, walks into valley (negative altitude from sea level)
def countingValleys(n, s):
    alt = 0
    count = 0
    val = 0
    for x in range (len(s)):
        if(s[x] == "D"):
            alt -= 1
        else:
            alt += 1
        if(alt < 0 and val == 0):
            count += 1
            val = 1
        elif(alt >= 0 and val == 1):
            val = 0
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
