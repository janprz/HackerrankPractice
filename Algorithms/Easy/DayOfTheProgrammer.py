#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]
    non_leap_year = [31,28,31,30,31,30,31,31,30,31,30,31]
    special_case_1918 = [31,15,31,30,31,30,31,31,30,31,30,31] # we need to remember to shift the date in february
    if year < 1918:
        if year % 4 == 0: # leap year
            return '12.09.{}'.format(year)
        if year % 4 != 0: # non leap year
            return '13.09.{}'.format(year)
    if year == 1918:
        return '26.09.{}'.format(year)
    div_by_4_not_by_100 = year % 4 == 0 and year % 100 != 0
    if year > 1918:
        if year % 400 == 0 or div_by_4_not_by_100: # leap year
            return '12.09.{}'.format(year)
        else: # non leap year
            return '13.09.{}'.format(year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
