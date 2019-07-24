# Naive way failed some test cases
# Plan: Make Magazine into a dictionary, indexed by its values
# If value not a key of the dictionary, print NO

# uses a defaultdict to handle duplicate keys
#!/bin/python3
from collections import defaultdict
import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    if len(magazine) < len(note):
        print("No")
        return
    dict = defaultdict(list)
    for x in range(len(magazine)):
        dict[magazine[x]].append(magazine[x])
    for x in range(len(note)):
        if note[x] in dict:
            dict[note[x]].pop(0)
            if(dict[note[x]] == []):
                del dict[note[x]]
        else:
           print("No")
           return
    print("Yes")



if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)



# Naive approach:

'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    if len(magazine) < len(note):
        print("No")
        return
    for x in range(len(note)): # for every string in the note
        found = 0
        for y in range(len(magazine)): # loop through the magazine
            if note[x] == magazine[y]: # if the element is found in magazine
                found = 1
                magazine.pop(y) # delete it from the magazine
                break
        if not found == 1:
            print("No")
            return
    print("Yes")



if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
'''

# Less Naive implementation but cannot handle duplicates
'''
#!/bin/python3
from collections import defaultdict
import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    if len(magazine) < len(note):
        print("No")
        return
    dict = {}
    for x in range(len(magazine)):
        dict[magazine[x]] = magazine[x]
    for x in range(len(note)):
        if note[x] in dict:
            dict.pop(note[x])
        else:
            print("No")
            return
    print("Yes")



if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
'''
'''
#!/bin/python3
from collections import defaultdict
import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    if len(magazine) < len(note):
        print("No")
        return
    dict = defaultdict(list)
    for x in range(len(magazine)):
        dict[magazine[x]].append(magazine[x])
    for x in range(len(note)):
        if note[x] in dict:
            dict[note[x]].pop(0)
            if(dict[note[x]] == []):
            	dict.pop([note[x]])
        else:
           print("No")
           return
    print("Yes")



if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

magazine = ["hello", "there", "bird", "there"]
note = ["hello", "there", "bird"]
checkMagazine(magazine, note)
'''
