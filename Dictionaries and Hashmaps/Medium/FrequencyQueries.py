#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    # num_dict = {}
    # occ_dict = {}
    # output = []
    # for query in queries:
    #     if query[0] == 1:
    #         if num_dict.get(query[1]) == None:
    #             num_dict[query[1]] = 1
    #             if occ_dict.get(num_dict[query[1]]) != None:
    #                 occ_dict[num_dict[query[1]]] += 1
    #             else:
    #                 occ_dict[num_dict[query[1]]] = 1
    #         else:
    #             num_dict[query[1]] += 1
    #             if occ_dict[num_dict[query[1]]-1] > 0:
    #                 occ_dict[num_dict[query[1]]-1] -= 1
    #             if occ_dict.get(num_dict[query[1]]) != None:
    #                 occ_dict[num_dict[query[1]]] += 1
    #             if occ_dict.get(num_dict[query[1]]) == None:
    #                 occ_dict[num_dict[query[1]]] = 1
    #     if query[0] == 2:
    #          if num_dict.get(query[1]) != None:
    #             num_dict[query[1]] = max(0, num_dict[query[1]]-1)
    #             occ_dict[num_dict[query[1]]+1] -= 1
    #             if occ_dict.get(num_dict[query[1]]) != None:
    #                 occ_dict[num_dict[query[1]]] += 1
    #             else:
    #                 occ_dict[num_dict[query[1]]] = 1
    #     if query[0] == 3:
    #         if occ_dict.get(query[1]) != None:
    #             if occ_dict.get(query[1]) >= 1:
    #                 output.append(1)
    #             else:
    #                 output.append(0)
    #         else:
    #             output.append(0)
    # return output

    num_dict = {} # count number of occurences for each number
    occ_dict = {} # count number of occurences generally
    output = []
    for query in queries:
        if query[0] == 1:
            num_dict[query[1]] = num_dict.get(query[1],0) + 1
            occ_dict[num_dict[query[1]]] = occ_dict.get(num_dict[query[1]],0) + 1
            occ_dict[num_dict[query[1]] - 1] = max(occ_dict.get(num_dict[query[1]]-1,0) - 1,0)
        if query[0] == 2:
            if num_dict.get(query[1]) != None:
                new_n = max(num_dict.get(query[1],0) - 1,0)
                old_n = num_dict[query[1]]
                num_dict[query[1]] = new_n
                occ_dict[new_n] = occ_dict.get(num_dict[query[1]],0) + 1
                occ_dict[old_n] = max(occ_dict.get(old_n,0) - 1,0)
        if query[0] == 3:
            occured = occ_dict.get(query[1],0)
            if occured > 0:
                output.append(1)
            else:
                output.append(0)
    return output


            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
