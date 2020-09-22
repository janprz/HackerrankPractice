#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min_score = scores[0]
    max_score = scores[0]
    min_break = 0
    max_break = 0
    for score in scores[1:]:
        if min_score > score:
            min_break += 1
            min_score = score
        if max_score < score:
            max_break += 1
            max_score = score
    result = []
    result.append(max_break)
    result.append(min_break)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
