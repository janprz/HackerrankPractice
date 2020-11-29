#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.
class Node:
    def __init__(self,idx):
        self.idx = idx
        self.edges = []
        
    def add_edge(self,idx):
        self.edges.append(idx)
        
def dfs(idx,visited, nodes):
    if visited[idx] == True:
        return 0
    if nodes[idx].edges == None:
        return 1
    visited[idx] = True
    cost = 1
    for neighb in nodes[idx].edges:
        if visited[neighb] != True:
            cost += dfs(neighb,visited,nodes)
    return cost

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return n*c_lib
    else:
        
    
        nodes = [None] + [Node(i) for i in range(1,n+1)]
        for city1, city2 in cities:
            nodes[city1].add_edge(city2)
            nodes[city2].add_edge(city1)
        
        visited = [False] * (n+1)
        roads_to_build = []
        for i in range(1,n+1):
            res = dfs(i,visited, nodes)
            if res > 0:
                roads_to_build.append(res)
        cost = 0
        for n in roads_to_build:
            cost += (n-1)*c_road + c_lib
        return cost
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
