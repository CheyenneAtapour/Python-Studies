#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    arr = [0] * 101
    for x in range (len(ar)):
        arr[ar[x]] += 1
        if(arr[ar[x]] % 2 == 0):
            pairs += 1
    return pairs



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()