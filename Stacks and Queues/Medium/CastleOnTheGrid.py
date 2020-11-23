#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    print(find_nb(startX,startY,len(grid),grid))
    q = [[startX,startY]]
    N = len(grid)
    n_steps = [[0 for i in range(N)] for j in range(N)]
    while q:
        point = q.pop()
        nb = find_nb(point[0],point[1],N,grid)
        for n in nb:
            n_steps[n[0]][n[1]] = n_steps[point[0]][point[1]] + 1
            if n == [goalX, goalY]:
                return n_steps[n[0]][n[1]]
            q.append(n) 
            
        
    

def find_nb(x,y,N, arr):
    # arr = list(reversed(arr))
    nb = []
    org_x = x
    org_y = y
    while x > 0:
        x -= 1
        if arr[x][y] == 'X':
            x += 1
            break
    if x != org_x:
        nb.append([x,y])
    x = org_x
    while x < N-1:
        x += 1
        if arr[x][y] == 'X':
            x -= 1
            break
    if x != org_x:
        nb.append([x,y])
    x = org_x
    while y > 0:
        y -= 1
        if arr[x][y] == 'X':
            y += 1
            break
    if y != org_y:
        nb.append([x,y])
    y = org_y
    while y < N-1:
        y += 1
        if arr[x][y] == 'X':
            y -= 1
            break
    if y != org_y:
        nb.append([x,y])
    y = org_y
    return nb

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
