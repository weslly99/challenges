#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    sorted_arr = arr.copy()
    sorted_arr.sort()
    frequency_size = sorted_arr[len(sorted_arr)-1] +1
    frequency = [0 for i in range(frequency_size)]
    for i in range(len(arr)-1):
        for j in arr:
            if i == j:
                frequency[i] += 1
    return frequency

    

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print(result)
