#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    n_anagrams = {}
    for i in range(0,len(s)):
        for j in range(0,len(s)-i):
            string = s[j:j+i+1]
            string = sorted(string)
            string = "".join(string)
            print(string)
            if n_anagrams.get(string) != None:
                    n_anagrams[string] += 1
            else:
                n_anagrams[string] = 0
    result = 0
    for key in n_anagrams:
        if n_anagrams[key] == 1:
            result += int(n_anagrams[key])
        else:
            result += int((n_anagrams[key]+1) * (n_anagrams[key])/2)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
