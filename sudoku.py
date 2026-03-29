#!/usr/bin/env python3
"""Sudoku solver and generator."""
import sys, random

def solve(board):
    empty = find_empty(board)
    if not empty: return True
    r, c = empty
    for num in range(1, 10):
        if is_valid(board, r, c, num):
            board[r][c] = num
            if solve(board): return True
            board[r][c] = 0
    return False

def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0: return r, c
    return None

def is_valid(board, row, col, num):
    if num in board[row]: return False
    if num in [board[r][col] for r in range(9)]: return False
    br, bc = 3*(row//3), 3*(col//3)
    for r in range(br, br+3):
        for c in range(bc, bc+3):
            if board[r][c] == num: return False
    return True

def generate(clues=30, seed=None):
    if seed is not None: random.seed(seed)
    board = [[0]*9 for _ in range(9)]
    # Fill diagonal boxes
    for b in range(3):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                board[b*3+i][b*3+j] = nums.pop()
    solve(board)
    # Remove cells
    cells = [(r,c) for r in range(9) for c in range(9)]
    random.shuffle(cells)
    for r, c in cells[:81-clues]:
        board[r][c] = 0
    return board

def to_string(board):
    lines = []
    for r in range(9):
        if r % 3 == 0 and r > 0: lines.append("-"*21)
        row = ""
        for c in range(9):
            if c % 3 == 0 and c > 0: row += "| "
            row += f"{board[r][c] if board[r][c] else '.'} "
        lines.append(row)
    return chr(10).join(lines)

def test():
    board = [
        [5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]
    ]
    assert solve(board)
    assert board[0][2] == 4
    assert all(board[r][c] != 0 for r in range(9) for c in range(9))
    gen = generate(35, seed=42)
    zeros = sum(1 for r in range(9) for c in range(9) if gen[r][c] == 0)
    assert zeros == 46
    print("  sudoku: ALL TESTS PASSED")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test": test()
    else: print(to_string(generate()))
