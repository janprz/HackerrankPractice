#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    hour_dict = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve'}
    minute_list = [
        "zero", 
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "twenty one",
        "twenty two",
        "twenty three",
        "twenty four",
        "twenty five",
        "twenty six",
        "twenty seven",
        "twenty eight",
        "twenty nine"
    ]
    minutes_word = ""
    middle_word = ""
    if m <= 30:
        middle_word = "past "
    if m > 30:
        middle_word = "to "
        m = 60 - m
        h += 1
    if m == 1:
        minutes_word = "one minute "
        return minutes_word+middle_word+hour_dict[h]
    if m == 15 or m==45:
        minutes_word = "quarter "
        return minutes_word+middle_word+hour_dict[h]
    if m == 30:
        minutes_word =  "half "
        return minutes_word+middle_word+hour_dict[h]
    if m not in([0,1,15,45,30]):
        minutes_word = "{} minutes ".format(minute_list[m])
        return minutes_word+middle_word+hour_dict[h]
    if m == 0:
        minutes_word = ' o\' clock'
        return hour_dict[h]+minutes_word
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
