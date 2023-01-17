import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    counter = 0
    n = len(a)
    for i in range(n-1):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                counter += 1
            else:
                continue

    print("Array is sorted in " + str(counter) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[n-1]))


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)
