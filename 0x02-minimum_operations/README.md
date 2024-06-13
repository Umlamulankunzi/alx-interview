# Minimum Operations

This repository contains a Python function to calculate the minimum number of operations needed to achieve exactly `n` characters in a text file, starting with a single character 'H'. The operations allowed are "Copy All" and "Paste".

## Problem Statement

In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: "Copy All" and "Paste". Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

### Prototype

```python
def minOperations(n)
```

- **Parameters**: 
  - `n` (int): The target number of `H` characters.
- **Returns**: 
  - An integer representing the fewest number of operations needed to achieve `n` `H` characters.
  - If `n` is impossible to achieve, the function returns `0`.

### Example

```python
n = 9

# H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

# Number of operations: 6
print(minOperations(9))  # Output: 6
```

## Implementation

The function `minOperations` is implemented to determine the minimum number of operations required to achieve exactly `n` `H` characters.

### Algorithm

1. If `n` is less than or equal to 1, return 0 (since it's impossible to achieve).
2. Initialize `operations` to 0.
3. Start with the smallest divisor `d` of `n` greater than 1.
4. While `n` is greater than 1:
   - Find the smallest divisor of `n`.
   - Divide `n` by this divisor.
   - Add the divisor to `operations`.
5. Return the total number of operations.

### Code

```python
def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    d = 2
    while n > 1:
        while n % d == 0:
            operations += d
            n //= d
        d += 1
    return operations
```

## Usage

To use this function, simply call it with the desired number of `H` characters:

```python
print(minOperations(9))  # Output: 6
print(minOperations(15)) # Output: 8
```

---

Enjoy coding!
