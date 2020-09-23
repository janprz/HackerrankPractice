#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    array = [0] * (n+1)
    max_val = -math.inf
    
    for query in queries:
        array[query[0]-1] += query[2]
        array[query[1]] -= query[2]
    sum_at_place = 0
    for value in array:
        sum_at_place += value
        if max_val < sum_at_place:
            max_val = sum_at_place
    return max_val


    for i in range(0,len(queries)):
        tempSum = queries[i][2]
        for j in range(i+1,len(queries)):
            cond_1 = queries[i][1] >= queries[j][0] and queries[i][1] <= queries[j][1]
            cond_2 = queries[i][0] >= queries[j][0] and queries[i][0] <= queries[j][1]
            cond_3 = queries[i][0] <= queries[j][0] and queries[i][1] >= queries[j][1]
            if cond_1 or cond_2 or cond_3:
                tempSum += queries[j][2]
        if tempSum > max_val:
            max_val = tempSum
    return max_val


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
