#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):

    c.sort()
    len_c = len(c)
    flowers_bought = []
    total_price = 0
    n_flowers = 0
    while n_flowers != len_c:
        flowers_bought.append(0)
        for customer in range(k):
            total_price += len(flowers_bought)*c[len_c-1-n_flowers]
            n_flowers += 1
            if n_flowers == len_c:
                break
    return total_price



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
