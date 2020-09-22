#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    n_bribes = 0       
    for i,n in enumerate(q):
        if n-i-1 > 2:
            n_bribes = -1
            break 
        for j in range(max(0,q[i]-2),i):
            if(q[j] > q[i]):
                n_bribes+=1
    if n_bribes != -1:
        print(n_bribes)
    else:
        print('Too chaotic')

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
