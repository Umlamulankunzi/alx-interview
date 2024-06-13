#!/usr/bin/python3

"""
Module that imolements minimum operations function
"""


def minOperations(n):
    """Calculates the fewest number of operations needed to

    result in exactly n H characters in the file.

    Args:
        n: The desired number of H characters.

    Returns:
        The minimum number of operations required
    """
    if n <= 1:
        return 0  # No operations needed for 0 or 1 H

    operations = 0
    current = 1  # Initially, we have 1 H in the file

    # Try to factorize n and count the num of operations
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
