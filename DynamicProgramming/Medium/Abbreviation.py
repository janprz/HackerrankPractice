#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.

memory = set()
possible = False

def abbreviation(a, b):
    global possible, memory
    possible = False
    memory.clear()
    check_possibility(a,b)
    if possible:
        return "YES"
    else:
        return "NO"
    
    
def check_possibility(a,b):
    global possible, memory
    if possible or len(a) < len(b):
        return
    if len(b) == 0:
        if a.islower() or len(a) == 0:
            possible = True
            return
    
    key = a + '#' + b
    if key in memory:
        return
    memory.add(key)
    
    first_char = a[0:1]
    a = a[1:]
    if first_char.islower():
        check_possibility(a,b)
    if first_char.upper() != b[0:1]:
        return
    b = b[1:]
    check_possibility(a,b)
    return

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
