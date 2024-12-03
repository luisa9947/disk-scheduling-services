def look(arm_position, lrequests, debug=False):
    """
    LOOK implementation.

    Args:
        arm_position (int): Current arm position.
        lrequests (list<int>): List of cylinder requests.
        debug (bool): If True, prints debug information.

    Returns:
        dict: Contains sequence of movements, average seek distance, and total distance.
    """
    # Sort the requests and split them into those to the right and left of the arm position
    lrequests = sorted(lrequests)
    requests_right = [req for req in lrequests if req >= arm_position]
    requests_left = [req for req in lrequests if req < arm_position]

    # Sequence of movements: first to the right, then to the left
    sequence = requests_right + requests_left[::-1]
    
    # Add the initial arm position to the sequence
    full_sequence = [arm_position] + sequence
    
    # Calculate total seek distance
    distance = 0
    current_pos = arm_position
    for req in sequence:
        distance += abs(req - current_pos)
        current_pos = req
        if debug:
            print("> ", current_pos, "seeked")

    # Calculate average distance
    average = distance / len(lrequests)

    return {
        "sequence": full_sequence,
        "average": average,
        "distance": distance,
    }

# Ejemplo de uso
result = look(96, [125, 17, 23, 67, 90, 128, 189, 115, 97], debug=True)
print(result)
