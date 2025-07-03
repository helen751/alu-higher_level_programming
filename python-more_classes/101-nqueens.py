#!/usr/bin/python3
"""Solves the N Queens problem."""
import sys


def print_solutions(n, board):
    result = []
    for i in range(n):
        result.append([i, board[i]])
    print(result)


def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve(n, row, board):
    if row == n:
        print_solutions(n, board)
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve(n, row + 1, board)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1 for i in range(n)]
    solve(n, 0, board)
