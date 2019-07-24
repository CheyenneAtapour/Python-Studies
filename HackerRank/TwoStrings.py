# Tests if the two given string share a common substring (of even 1 char)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
	dict = {}
	for x in range(len(s2)):
		dict[s2[x]] = s2[x]
	for x in range(len(s1)):
		if(s1[x] in dict):
			return "YES"
	return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
