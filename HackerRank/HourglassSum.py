#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
# Calculates max sum of an hourglass shape within a 6x6 array (3 across (top and bottom), middle 3 down)
def hourglassSum(arr):
    maxCount = -63
    for i in range (4):
        for j in range (4):
            count = 0
            count += arr[0+i][0+j]+ arr[0+i][1+j] + arr[0+i][2+j] + arr[1+i][1+j] + arr[2+i][0+j] + arr[2+i][1+j] + arr[2+i][2+j]
            if(count > maxCount):
                maxCount = count
    return maxCount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
