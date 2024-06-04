#!/usr/bin/python3



"""
This module contains a function to unlock boxes represented by a list of lists. It determines if all the boxes can be opened by checking if the keys in the boxes can unlock all the boxes.
"""



def unlock_boxes(boxes):
    """Unlock the boxes and return a sorted list

    of the boxes that were successfully unlocked.

    Parameters:
        boxes: list of lists representing locked boxes.
        Each sublist contains the keys to the other boxes.

    Returns:
        sorted list of successfully unlocked boxes.

    Algorithm:
    - Initialize empty list 'unlocked' to store unlocked boxes.
    - Initialize an empty list 'key_dump' to store keys found in unlocked boxes.
    - Initialize a list 'unlock_keys' with the first box index, which is 0 unlocked by default.
    - Iterate 'len(boxes)' times to ensure all boxes are processed.
        - Iterate over each key in 'unlock_keys'.
            - If key in 'unlocked' list, skip it.
            - Extend 'key_dump' list with keys found in current box.
            - Add the current key to 'unlocked' list.
        - Assign the unique values from 'key_dump' to 'unlock_keys' to get the next set of keys to check.
        - Clear the 'key_dump' list for the next iteration.
        - Return the sorted 'unlocked' list.
         """
    unlocked = []
    key_dump = []
    unlock_keys = [0]

    for _ in range(len(boxes)):
        for key in unlock_keys:
            if key in unlocked:
                pass
            key_dump.extend(boxes[key])
            unlocked.append(key)

        unlock_keys = list(set(key_dump))
        key_dump.clear()

    return sorted(unlocked)


def canUnlockAll(boxes):
    """Check if all the boxes can be unlocked.

    Parameters:
        boxes: list of lists representing locked boxes. 
        Each sublist contains the keys to the other boxes.

    Returns:
        True if all boxes can be unlocked, else False.

    Algorithm:
    - Call 'unlock_boxes' function with given 'boxes'.
    - Check if sorted list of unlocked boxes is equal to the range of the number of boxes.
        - If equal, return True else False.
    """

    return unlock_boxes(boxes) == list(range(len(boxes)))


