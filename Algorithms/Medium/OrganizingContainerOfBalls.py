#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    types_count = [0]*len(container)
    container_count = [0]*len(container)
    for i in range(0,len(container)):
        container_count[i] = sum(container[i])
    for i in range(0,len(container)):
        for j in range(0,len(container[i])):
            types_count[j] += container[i][j]
    types_count = sorted(types_count)
    container_count = sorted(container_count)
    for i in range(0,len(container)):
        if types_count[i] != container_count[i]:
            return 'Impossible'
    return 'Possible'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
