#!/usr/bin/python3
"""
Module that contains a function to determine the fewest number of coins
needed to meet a given total amount when given a pile of coins of different values.
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total amount
    when given a pile of coins of different values.

    Parameters:
    coins (list of int): A list of the values of the available coins.
    total (int): The total amount to meet with the fewest number of coins.

    Returns:
    int: The fewest number of coins needed to meet the total amount.
         Returns -1 if the total cannot be met by any combination of coins.
    """
    if total <= 0:
        return 0

    remainder = total
    coin_count = 0
    sorted_coins = sorted(coins, reverse=True)
    
    for coin in sorted_coins:
        coin_count += remainder // coin
        remainder = remainder % coin
        if remainder == 0:
            return coin_count
            
    return -1

if __name__ == "__main__":
    print(make_change([1, 2, 25], 37))