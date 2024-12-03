def scan(arm_position, lrequests, max_cylinder, direction="ascendente", debug=False):
    """
    SCAN (Elevator Algorithm) implementation with direction control.

    Args:
        arm_position (int): Current arm position.
        lrequests (list<int>): List of cylinder requests.
        max_cylinder (int): Maximum cylinder number.
        direction (str): Initial direction ("ascendente" or "descendente").
        debug (bool): If True, prints debug information.

    Returns:
        dict: Contains sequence of movements, average seek distance, and total distance.
    """
    # Sort the requests
    lrequests = sorted(lrequests)
    requests_right = [req for req in lrequests if req >= arm_position]
    requests_left = [req for req in lrequests if req < arm_position]

    # Determine sequence based on initial direction
    if direction == "ascendente":
        sequence = requests_right + [max_cylinder] + requests_left[::-1]
    else:  # "descendente"
        sequence = requests_left[::-1] + [0] + requests_right

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

# Ejemplo de uso con dirección descendente
result = scan(
    arm_position=50,
    lrequests=[176, 79, 34, 60, 92, 11, 41, 114],
    max_cylinder=226,
    direction="descendente",  # Indica que debe ir hacia atrás primero
    debug=True
)

# Imprimir resultados
print("Secuencia de movimientos:", result["sequence"])
print("Distancia total recorrida:", result["distance"])
print("Promedio de distancia por solicitud:", result["average"])