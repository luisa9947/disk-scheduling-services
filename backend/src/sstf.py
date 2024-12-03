from heapq import *

def sstf(arm_position, lrequests, debug=False):
  """
  Shortest Seek Time First implementation

  Args:
      arm_position (int): arm position
      lrequests (list<int>): request list
  """
  distance = 0
  n = len(lrequests)
  current_pos = arm_position
  requests = lrequests.copy()
  sequence = [arm_position]

  while requests:
    # Seleccionar la solicitud más cercana
    closest_request = min(requests, key=lambda x: abs(x - current_pos))
    requests.remove(closest_request)

    # Calcular la distancia
    distance += abs(closest_request - current_pos)
    current_pos = closest_request
    sequence.append(current_pos)

    if debug: 
      print("> ", current_pos, "seeked")
  
  average = distance / n
  return {
    "sequence": sequence,
    "average": average,
    "distance": distance,
  }

# Ejemplo de uso
# print(sstf(96, [125, 17, 23, 67, 90, 128, 189, 115, 97]))
