# finds the minimum absolute difference between 2 integers in a given array

# Sort the Array first!
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    mina = 2000000000
    arr.sort()
    x = 0
    while x + 1 < len(arr):
        if abs(arr[x] - arr[x+1]) < mina:
            mina = abs(arr[x] - arr[x+1])
        x += 1
    return mina

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()



# a little bit naiive 4/10 timeouts

#!/bin/python3
'''
import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    mina = 2000000000
    x = 0
    while x < len(arr):
        j = x
        while j < len(arr):
            if not x == j:
                if abs(arr[x]-arr[j]) < mina:
                    mina = abs(arr[x]-arr[j])
            j += 1
        x += 1
    return mina
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
'''