def solution(A):
    # write your code in Python 3.6
    A.sort()
    temp = 1
    for x in range(len(A)):
        if A[x] == temp:
            temp += 1
    return temp
