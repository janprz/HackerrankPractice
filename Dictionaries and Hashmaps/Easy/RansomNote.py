#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_dict = {}
    for word in magazine:
        if magazine_dict.get(word) == None:
            magazine_dict[word] = 1
        else:
            magazine_dict[word] += 1
    for word in note:
        if magazine_dict.get(word) == None or magazine_dict.get(word) == 0:
            print("No")
            return
        else:
            magazine_dict[word] -= 1
    print('Yes')
    return
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
