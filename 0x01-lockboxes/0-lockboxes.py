def canUnlockAll(boxes):
    n = len(boxes)  # Total number of boxes
    unlocked = [False] * n  # Initialize a list to track unlocked boxes
    unlocked[0] = True  # The first box is unlocked by default

    stack = [0]  # Start with the first box in the stack
    while stack:
        box = stack.pop()  # Take a box from the stack
        for key in boxes[box]:  # Iterate over the keys in the box
            if key < n and not unlocked[key]: 
                # Check if the key is valid and the box is locked
                unlocked[key] = True  # Unlock the box
                stack.append(key)  # Add the newly unlocked box to the stack
    return all(unlocked) 
# Return True if all boxes are unlocked, else return False

