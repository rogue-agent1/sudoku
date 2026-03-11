#!/usr/bin/env python3
"""Sudoku solver. Input: 9 lines, 0=empty."""
import sys
grid = []
for line in (open(sys.argv[1]) if len(sys.argv)>1 else sys.stdin):
    row = [int(c) for c in line.strip().replace(' ','') if c.isdigit()]
    if len(row)==9: grid.append(row)
def valid(g,r,c,n):
    if n in g[r] or n in [g[i][c] for i in range(9)]: return False
    br,bc = 3*(r//3),3*(c//3)
    return n not in [g[br+i][bc+j] for i in range(3) for j in range(3)]
def solve(g):
    for r in range(9):
        for c in range(9):
            if g[r][c]==0:
                for n in range(1,10):
                    if valid(g,r,c,n):
                        g[r][c]=n
                        if solve(g): return True
                        g[r][c]=0
                return False
    return True
if solve(grid):
    for row in grid: print(' '.join(map(str, row)))
else: print("No solution")
