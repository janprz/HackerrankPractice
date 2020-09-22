#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    results = []
    scores = list(set(scores))
    scores = sorted(scores)
    print(scores)
    place = len(scores) + 1
    print(place)
    lastPosition = 0
    for alice_result in alice:
        for i in range(lastPosition,len(scores)):
            if alice_result >= scores[i]:
                place -= 1
                lastPosition += 1
            elif alice_result < scores[i]:
                break
        results.append(place)
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
