#!/usr/bin/python3

"""
Module: 0-island_perimeter

This module provides function for calculating the perimeter of an island
contained within the grid argument.

Function:
    island_perimeter(grid): calculates perimeter of island contained in
    grid.

grid argument constraints:
    grid is a list of lists of integers
    - 0 represents water
    - 1 represents land
    - Each cell is a square, with side length 1
    - Cells are connected horizontally/ vertically (not diagonally)
    - grid is rectangular, with width and height >= 100
    - grid completely surrounded by water
    - There is only one island (or none)
    - The island doesn't have "lakes"
"""


def island_perimeter(grid):
    """Calculates perimeter of island in grid

    Args:
        grid (list[list[int]]): list of lists of integers
    Returns:
        int: perimeter of island
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for row in range(rows):
        for sq in range(cols):
            if grid[row][sq] == 1:  # Land found
                perimeter += 4

                # Check the cell above
                if row > 0 and grid[row - 1][sq] == 1:
                    perimeter -= 2

                # Check the cell to the left
                if sq > 0 and grid[row][sq - 1] == 1:
                    perimeter -= 2

    return perimeter
