#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
# Counts number of jumps to get to end of string (cannot land on 1s, and can jump 1 or 2 spaces)
def jumpingOnClouds(c):
    jmp = 0
    x = 0
    while x < len(c) - 1:
        if x + 2 > len(c) - 1: # only 1 cloud in front of us to end, must be 0
            jmp += 1
            x += 2
        else: # otherwise, we have 2 clouds in front of the one we are standing on
            if str(c[x]) + str(c[x+1]) + str(c[x+2]) == "001":
                jmp += 2
                x += 3
            else:
                jmp += 1
                x += 2
    return jmp 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()