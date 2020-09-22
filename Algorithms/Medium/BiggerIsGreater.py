#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    w_list = list(w)
    for i in range(len(w)-1,-1,-1):
        if i-1 > -1:
            if ord(w[i]) > ord(w[i-1]):
                pivot = i-1
                break
        else:
            return 'no answer'
    for i in range(len(w)-1,pivot,-1):
        if w_list[i] > w_list[pivot]:
            w_list[i],w_list[pivot] = w_list[pivot], w_list[i]
            break
    pre_reverse = "".join(w_list)
    left_part = pre_reverse[:pivot+1]
    right_part = pre_reverse[pivot+1:]
    result = left_part + "".join(reversed(list(right_part)))
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
