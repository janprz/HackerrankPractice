#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    position = []
    height = []
    max_field = 0
    position.append(0)
    height.append(h[0])
    for i,rec in enumerate(h):
        if i != 0:
            if rec > height[-1]:
                height.append(rec)
                position.append(i)
            elif rec < height[-1]:
                while len(height) > 0 and rec < height[-1]:
                    val = height.pop()
                    start_pos = position.pop()
                    max_field = max((i-start_pos)*val,max_field)
                position.append(start_pos)
                height.append(rec)
    length = len(h)
    i = len(height)
    while(i != 0):
        val = height.pop()
        start_pos = position.pop()
        max_field = max((length-start_pos)*val,max_field)
        i -= 1
    return max_field
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
