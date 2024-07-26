import numpy as np

def calculate_distances(O, list, max):
    distances = []
    for point in list:
        distance = np.linalg.norm(np.array(O) - np.array(point))
        if distance <= max:
            distances.append((point, distance))
    return distances

max = 3
list = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)] #tự điền vào

O = (x, y) 

distances = calculate_distances(O, list, max)

print(f"Point O: {O}")
print(f"Points within a distance of {max}:")
for point, distance in distances:
    print(f"Point {point} is {distance:.2f} units away.")