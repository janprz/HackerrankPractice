#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    counter_arr = [[0 for i in range(len_s1+1)] for j in range(len_s2+1)]
    
    longest = 0
    for i in range(len_s1):
        for j in range(len_s2):
            if s1[i] == s2[j]:
                print('true')
                counter_arr[i+1][j+1] = counter_arr[i][j] + 1
                if counter_arr[i+1][j+1] > longest:
                    longest = counter_arr[i+1][j+1]   
            else:
                counter_arr[i+1][j+1] = max(counter_arr[i+1][j],counter_arr[i][j+1])


    return longest


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
