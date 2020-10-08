#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    cost_dict = {}

    for i,ice_cost in enumerate(cost):
        if money-ice_cost in cost_dict:
            print(str(cost_dict[money-ice_cost]+1),str(i+1))
        else:
            cost_dict[ice_cost] = i
    return

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())
        n = int(input())
        cost = list(map(int, input().rstrip().split()))
        whatFlavors(cost, money)
