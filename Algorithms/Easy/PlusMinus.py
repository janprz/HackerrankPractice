#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    neg = []
    pos = []
    zero = []
    for i in arr:
        if(i>0):
            pos.append(i)
        if(i==0):
            zero.append(i)
        if(i<0):
            neg.append(i)
    print(round(len(pos)/len(arr),6))
    print(round(len(neg)/len(arr),6))
    print(round(len(zero)/len(arr),6))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
