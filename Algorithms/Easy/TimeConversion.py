#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if s[-2] == 'P' and s[:2] != '12':
        s = str(int(s[:2]) + 12) + s[2:-2]
    elif s[-2] == 'A':
        if s[:2] == '12':
            s = '00' + s[2:-2]
        else:
            s = s[:-2]
    else:
        s = s[:-2]
    return s

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
