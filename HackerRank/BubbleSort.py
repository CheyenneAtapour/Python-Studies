# Performs bubble sort, counts the number of swaps, and prints first and last element

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
	temp = 0
	count = 0
	for x in range(len(a)):
		for y in range(len(a) - 1):
			if a[y] > a[y + 1]:
				temp = a[y + 1]
				a[y + 1] = a[y]
				a[y] = temp
				count += 1
	print("Array is sorted in " + str(count) + " swaps.")
	print("First Element: " + str(a[0]))
	print("Last Element: " + str(a[-1]))


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
