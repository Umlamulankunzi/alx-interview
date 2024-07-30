# 0x09. Island Perimeter

## Description
The **0x09. Island Perimeter** project involves creating a function that calculates the perimeter of an island represented in a grid. The grid consists of integers where `0` represents water and `1` represents land. The function computes the total perimeter of the land mass (island) in the grid.

## Function
### `island_perimeter(grid)`

- **Parameters:**
  - `grid` (list of list of integers): A rectangular grid where each cell is represented as follows:
    - `0`: Water
    - `1`: Land

- **Returns:**
  - An integer representing the perimeter of the island.

### Constraints
- The grid's width and height do not exceed 100.
- The grid is completely surrounded by water.
- There is only one island (or no island at all).
- The island does not contain "lakes" (water that is not connected to the surrounding water).

## Example

### Usage

You can use the provided `0-main.py` file to test the `island_perimeter` function. Here’s an example:

```python
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
