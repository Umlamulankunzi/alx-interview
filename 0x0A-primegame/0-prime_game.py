#!/usr/bin/python3

"""
Prime Game

This module contains the implementation of the Prime Game, where two
players, Maria and Ben, take turns choosing prime numbers from a set
of consecutive integers. The chosen prime number and its multiples
are removed from the set. The player unable to make a move loses the
game. The task is to determine the player who wins the most rounds
over multiple games.

The module provides:
- `generate_primes(max_num)`: Generates a list of prime numbers up to
   max_num.
- `determine_winner(n)`: Determines winner of game for given integer n
- `isWinner(x, nums)`: Determines player who won most rounds
   across x games given a list of n values.
"""

def generate_primes(max_num):
    """Generate list of prime numbers up to max_num

    Args:
        max_num (int): The upper limit for generating prime numbers

    Returns:
        List[int]: A list of prime numbers up to max_num
    """
    is_prime = [True] * (max_num + 1)
    p = 2
    while (p * p <= max_num):
        if (is_prime[p] == True):
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, max_num + 1) if is_prime[p]]

def determine_winner(n):
    """
    Determine winner of the Prime Game for a given integer n.

    Players take turns picking a prime number and removing it
    and its multiples. The player who cannot make 
    a move loses the game. Maria always starts first.

    Args:
        n (int): upper limit of set of consecutive ints (1 to n)

    Returns:
        str: name of player who wins the game, either 'Maria'or 'Ben'
    """
    primes = generate_primes(n)
    remaining = [True] * (n + 1)
    turn = 0  # 0 for Maria, 1 for Ben

    while True:
        prime_found = False
        for prime in primes:
            if prime > n:
                break
            if remaining[prime]:
                for multiple in range(prime, n + 1, prime):
                    remaining[multiple] = False
                prime_found = True
                break
        
        if not prime_found:
            return 'Ben' if turn == 0 else 'Maria'
        
        turn = 1 - turn

def isWinner(x, nums):
    """
    Determine winner of the Prime Game across multiple rounds.

    Args:
        x (int): The number of rounds.
        nums (List[int]): A list of integers where each integer
        represents the upper limit n for a round.

    Returns:
        str: The name of the player who won the most rounds. If
        both win the same number of rounds, return None.
    """
    if x <= 0 or not nums:
        return None

    wins = {'Maria': 0, 'Ben': 0}
    
    for n in nums:
        winner = determine_winner(n)
        if winner:
            wins[winner] += 1
    
    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Ben'] > wins['Maria']:
        return 'Ben'
    return None
