#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens
  on an N×N chessboard. Write a program that solves the N queens problem.
    Usage: nqueens N
        If the user called the program with the wrong number of arguments,
          print Usage: nqueens N, followed by a new line, and exit with
          the status 1
    where N must be an integer greater or equal to 4
        If N is not an integer, print N must be a number, followed by a
          new line, and exit with the status 1
        If N is smaller than 4, print N must be at least 4, followed by
          a new line, and exit with the status 1
    The program should print every possible solution to the problem
        One solution per line
        Format: see example
        You don’t have to print the solutions in a specific order
    You are only allowed to import the sys module
"""
import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    n_q = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if n_q < 4:
    print('N must be at least 4')
    exit(1)


def solve_nqueens(n):
    '''get number of queens'''
    if n == 0:
        return [[]]
    inner_solution = solve_nqueens(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(n_q)
            for solution in inner_solution
            if safe_queen((n, i + 1), solution)]


def attack_queen(square, queen):
    '''attacking the queen'''
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def safe_queen(sqr, queens):
    '''is the queen safe?'''
    for queen in queens:
        if attack_queen(sqr, queen):
            return False
    return True


for answer in reversed(solve_nqueens(n_q)):
    result = []
    for p in [list(p) for p in answer]:
        result.append([i - 1 for i in p])
    print(result)
