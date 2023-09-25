#!/usr/bin/python3
"""
returns the perimeter of the island described in grid

  grid is a list of list of integers:
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
  The grid is completely surrounded by water
  There is only one island (or nothing).
  The island doesn’t have “lakes” (water inside that isn’t connected
    to the water surrounding the island).
"""


def island_perimeter(grid):
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # If it's a land cell, check its neighbors for water cells
                neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                for x, y in neighbors:
                    if (
                        x < 0 or x >= rows or
                        y < 0 or y >= cols or
                        grid[x][y] == 0
                    ):
                        # If the neighbor is out of bounds or a water cell,
                        #   increment perimeter
                        perimeter += 1

    return perimeter
