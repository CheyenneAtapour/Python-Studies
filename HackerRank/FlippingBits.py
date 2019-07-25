#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    s = ""
    while not n == 0:
        s += str(int(n % 2))
        n = math.floor(n/2)
    while not len(s) == 32:
        s += "0" 
    rev = s [::-1]
    #print("s is " + s)
    #print("rev is " + rev)
    flip = ""
    for x in range(len(rev)):
        if rev[x] == "0":
            flip += "1"
        else:
            flip += "0"
    #print("flip is " + flip)
    ex = len(flip) - 1
    count = 0
    for x in range(len(flip)):
        if flip[x] == "1":
            count += 2 ** (ex - x)
    return count 

#print flippingBits(4)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
