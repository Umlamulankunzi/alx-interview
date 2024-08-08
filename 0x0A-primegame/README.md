# 0x0A-primegame: Prime Game

## Project Overview

The Prime Game project involves implementing a competitive game where two players, Maria and Ben, take turns selecting prime numbers from a set of consecutive integers. The objective is to determine the winner based on optimal play strategies. The project will leverage your understanding of prime numbers, game theory, and algorithm optimization.

### Concepts Needed

1. **Prime Numbers:**
   - Understand what prime numbers are.
   - Efficient algorithms for identifying prime numbers within a range.

2. **Sieve of Eratosthenes:**
   - An efficient algorithm to find all prime numbers up to a given limit.

3. **Game Theory:**
   - Basic principles of competitive games and optimal play strategies.
   - Understanding win conditions and strategies.

4. **Dynamic Programming/Memoization:**
   - Using previous results to optimize future calculations.

5. **Python Programming:**
   - Implementation using loops, conditional statements, arrays, and lists.

### Resources

- **Prime Numbers and Sieve of Eratosthenes:**
  - [Khan Academy: Prime Numbers](https://www.khanacademy.org/math/algebra/x2f8bb115bf2c59b4:prime-numbers)
  - [Sieve of Eratosthenes in Python](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)

- **Game Theory Basics:**
  - [Game Theory Introduction](https://www.coursera.org/lecture/game-theory/game-theory-introduction-0Fk23)

- **Dynamic Programming:**
  - [What Is Dynamic Programming With Python Examples](https://www.datacamp.com/community/tutorials/dynamic-programming-python)

- **Python Official Documentation:**
  - [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)


### Tasks

#### 0. Prime Game (Mandatory)

Implement a function to determine the winner of the Prime Game.

**Prototype:**
```python
def isWinner(x, nums):
    """
    Determine the winner of the Prime Game based on multiple rounds.

    Args:
        x (int): Number of rounds.
        nums (List[int]): List of integers representing different values of n for each round.

    Returns:
        str: Name of the player who won the most rounds. If the winner cannot be determined, return None.
    """
```

**Example:**
```python
x = 3
nums = [4, 5, 1]
# Output: "Ben"
```

**Explanation:**
- For each round, players choose a prime number, remove it and its multiples, and the player unable to make a move loses.
- Maria always goes first, and both players play optimally.

### Usage

To test your implementation, use the following script:

```python
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
```
