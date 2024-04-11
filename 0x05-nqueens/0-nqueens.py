#!/usr/bin/python3

"""
Solving the N Queens problem
"""

import sys


def is_safe(board, row, col):
    """
    Checks if placing a queen at aa (row, col) is safe.
    """
    for i in range(row):
        if board[i] == col:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i] == j:
            return False

    return True


def solve_nqueens_util(N, row, board, solutions):
    """
    A utility function to solve the N queens problem using backtracking.
    """
    if row == N:
        solutions.append(board[:])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens_util(N, row + 1, board, solutions)
            board[row] = -1  # Backtrack


def solve_nqueens(N):
    """
    Function to solve the N queens problem using backtracking.
    """
    board = [-1] * N
    solutions = []
    solve_nqueens_util(N, 0, board, solutions)

    return solutions


def print_solution(solution):
    """
    Function to print a single solution.
    """
    print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print_solution(solution)
