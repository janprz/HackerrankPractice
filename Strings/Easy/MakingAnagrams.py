#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a_dict = {}
    b_dict = {}
    for char in a:
        a_dict[char] = a_dict.get(char,0) + 1
    for char in b:
        b_dict[char] = b_dict.get(char,0) + 1

    diff = 0
    for char in b:
        if a_dict.get(char,0) > 0:
            a_dict[char] = max(a_dict[char]-1,0)
        elif a_dict.get(char,0) == 0:
            diff += 1
    for key in a_dict:
        diff += a_dict[key]
    return diff




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
