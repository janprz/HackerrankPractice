#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    n_substr = 0
    n_substr += len(s)
    mid_char_indices = []
    for i in range(0,n): # to find the all one letter substrings
        for j in range(0,n-i-1):
            if s[i] == s[i+1+j]:
                n_substr += 1
            else:
                break
    for i in range(1,n-1):
        if s[i] != s[i-1] and s[i] != s[i+1] and s[i-1] == s[i+1]:
            for j in range(0,min(i,n-1-i)):
                if s[i-1-j] == s[i+1+j] and s[i+1] == s[i+1+j]:
                    n_substr += 1
                else:
                    break
    return n_substr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
