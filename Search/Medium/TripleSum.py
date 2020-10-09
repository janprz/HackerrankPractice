#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    new_a = list(sorted(set(a)))
    new_c = list(sorted(set(c)))
    new_b = list(sorted(set(b)))
    n_triplets = 0
    ai = 0
    ci = 0
    for val in new_b:
        num_a = ai
        num_c = ci
        for val_a in new_a[ai:]:
            if val_a <= val:
                num_a += 1
                ai+=1
            else:
                break
        for val_c in new_c[ci:]:
            if val_c <= val:
                num_c += 1
                ci += 1
            else:
                break
        n_triplets += num_c * num_a
    return n_triplets


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
