#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
# Counts the number of "a"'s within n characters of a string s, repeated infinitely 
def repeatedString(s, n):
    l = len(s)
    inita = 0
    offCount = 0
    for x in range (len(s)):
        if(s[x]) == "a":
            inita += 1
    mod = n % l
    if mod == 0:
        return int(inita * (n / l))
    else:
        for y in range (mod):
            if s[y] == "a":
                offCount += 1
        return int((inita * math.floor(n / l)) + offCount)





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
