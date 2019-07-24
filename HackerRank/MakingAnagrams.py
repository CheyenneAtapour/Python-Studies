#!/bin/python3

from collections import defaultdict
import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
# run through string a, delete from b, add remaining characters up
def makeAnagram(a, b):
    count = 0
    dict = defaultdict(list)
    for x in range(len(b)):
        dict[b[x]].append(b[x])
    for x in range(len(a)):
        if a[x] in dict:
            dict[a[x]].pop(0)
            if dict[a[x]] == []:
                del dict[a[x]]
        else:
            count += 1
    for k,v in dict.items():
        count += len(v)
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
