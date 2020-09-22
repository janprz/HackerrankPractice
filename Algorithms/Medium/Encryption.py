#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    stripped = []
    for char in s:
        if char != ' ':
            stripped.append(char)
    rows = math.floor(math.sqrt(len(stripped)))
    cols = math.ceil(math.sqrt(len(stripped)))
    if rows * cols < len(stripped):
        rows += 1
    sentence = []
    for i in range(0,cols):
        word_as_string = ""
        word = []
        for j in range(0,rows):
            if i+j*cols < len(stripped):
                word.append(stripped[i+j*cols])
        sentence.append(word_as_string.join(word))
        sentence.append(' ')
    sentence_as_string = ""
    return sentence_as_string.join(sentence)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
