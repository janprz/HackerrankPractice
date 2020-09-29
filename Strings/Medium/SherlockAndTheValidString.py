#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):

    char_dict = {}
    for char in s:
        char_dict[char] = char_dict.get(char,0) + 1
    
    occ_dict = {}
    for key in char_dict:
        occ_dict[char_dict[key]] = occ_dict.get(char_dict[key],0) + 1

    if len(occ_dict.keys()) == 1:
        return 'YES'

    if len(occ_dict.keys()) == 2:
        keys = list(occ_dict.keys())
        if keys[0] == 1 and occ_dict[keys[0]] == 1:
            return 'YES'
        if keys[1] == 1 and occ_dict[keys[1]] == 1:
            return 'YES'
        if keys[0] == keys[1]+1 and occ_dict[keys[0]] == 1:
            return 'YES'
        if keys[1] == keys[0]+1 and occ_dict[keys[1]] == 1:
            return 'YES'
        return 'NO'
    return 'NO'
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
