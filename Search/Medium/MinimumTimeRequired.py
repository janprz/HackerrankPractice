#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    mach_len = len(machines)
    best_case = goal/mach_len*min(machines)
    worst_case = goal/mach_len*max(machines)
    r = worst_case
    l = best_case

    while l<r:
        mid = (l+r)//2
        product = 0
        for machine in machines:
            product += mid//machine
        if product >= goal:
            r = mid
        else:
            l = mid+1

    return int(l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
