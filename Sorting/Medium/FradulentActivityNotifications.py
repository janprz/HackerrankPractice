#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    notif = 0
    l_exp = len(expenditure)
    for i in range(d,l_exp):
        window = expenditure[i-d:i]
        len_w = len(window)     
        if i-d == 0:
            sort_arr = [0] * 201
            for val in window:
                sort_arr[val] += 1
        else:
            sort_arr[expenditure[i-1-d]] -= 1
            sort_arr[expenditure[i-1]] += 1
        sorted_window = [0] * len_w
        k = 0
        for j in range(0,201):
            if sort_arr[j] != 0:
                for z in range(0,sort_arr[j]):
                    sorted_window[k] = j
                    k += 1
            if k == len_w:
                break
        if len_w % 2 == 0:
            double_median = sorted_window[len_w//2] + sorted_window[len_w//2-1]
        elif len_w % 2 != 0:
            double_median = 2*sorted_window[len_w//2]
        if double_median <= expenditure[i]:
            notif += 1
    return notif


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
