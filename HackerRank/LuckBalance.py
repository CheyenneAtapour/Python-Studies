# counts the karma Lena gains by losing at most k important contests

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    imp = []
    luk = 0
    for x in range(len(contests)):
        if contests[x][1] == 1:
            imp.append(contests[x][0])
        else:
            luk += contests[x][0]
    imp.sort(reverse = True)
    i = 0
    while i < len(imp) and i < k:
        luk += imp[i]
        i += 1
    while i < len(imp):
        luk -= imp[i]
        i += 1
    return luk
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
