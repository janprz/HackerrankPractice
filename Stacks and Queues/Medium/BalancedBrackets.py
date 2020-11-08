#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the isBalanced function below.
def isBalanced(s):
    stack = deque()
    brackets_dict = {'}':'{',')':'(',']':'['}
    for char in s:
        if char == '{' or char == '(' or char == '[':
            stack.append(char)
        else:
            if len(stack) > 0:
                if stack[-1] == brackets_dict.get(char,'-'):
                    stack.pop()
                else:
                    return 'NO'
            else:
                return 'NO'
    if len(stack) == 0:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
