'''Lockboxes Challenge'''

def canUnlockAll(boxes):
    '''
    Determines if all the boxes can be opened or not
    Returns:
    	True: if all the boxes can be opened
    	False: if all the boxes cant be opened
    '''
    # Total number of boxes
    n = len(boxes)  
    # Initialize a list to track unlocked boxes
    unlocked = [False] * n
    # The first box is unlocked by default  
    unlocked[0] = True  

    # Start with the first box in the stack
    stack = [0]  
    while stack:
    	# Take a box from the stack
        box = stack.pop()  
        # Iterate over the keys in the box
        for key in boxes[box]:  
            # Check if the key is valid and the box is locked
            if key < n and not unlocked[key]: 
                unlocked[key] = True  
                stack.append(key) 
    # Return True if all boxes are unlocked, else return False 
    return all(unlocked) 


