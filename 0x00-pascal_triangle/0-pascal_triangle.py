#!/usr/bin/python3
"""
This script implements functions to generate Pascal's Triangle.

Function Documentation:

    `pascal(n)`:
        Takes an integer `n` as input, representing the row index (starting from 0).
        Returns a list containing the elements of the specified row in Pascal's Triangle.
        Utilizes the formula `row[x] * (n-x) / (x+1)` to calculate each element in the row.

    `pascal_triangle(n)`:
        Takes an integer `n` as input, representing the number of rows to generate.
        Returns a list of lists, where each inner list represents a row of Pascal's Triangle.
        Handles the case where `n` is less than or equal to 0 by returning an empty list.
        Uses a list comprehension to call the `pascal(nth)` function for each row index `nth` from 0 to `n-1`.

Example Usage:
    # Generate the first 5 rows of Pascal's Triangle
    triangle = pascal_triangle(5)

    # Print the triangle
    for row in triangle:
        print(row)

    Output:
        [1]
        [1, 1]
        [1, 2, 1]
        [1, 3, 3, 1]
        [1, 4, 6, 4, 1]
"""


def pascal(n):
    """
    Generates a single row of Pascal's Triangle.

    Args:
        n (int): The index of the row to generate (starting from 0).

    Returns:
        list: A list representing the elements of the specified row.
    """
    row = [1]
    for x in range(n):
        row.append(int(row[x] * (n - x) / (x + 1)))
    return row


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the specified number of rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists, where each inner list represents a row of Pascal's Triangle.
    """
    if n <= 0:
        return []
    return [pascal(nth) for nth in range(n)]
