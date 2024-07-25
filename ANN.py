import math

def calculate_distances(O, list):
    distances = []
    for point in list:
        distance = math.sqrt((O[0] - point[0])**2 + (O[1] - point[1])**2)
        distances.append((point, distance))
    return distances

def near_neighbors(O, list, num_neighbors):
    distances = calculate_distances(O, list)
    nearest_neighbors = sorted(distances, key=lambda x: x[1])[:num_neighbors]
    return nearest_neighbors
num_neighbors = 3
list = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)]
O = (x, y) 
nearest_neighbors = near_neighbors(O, list, num_neighbors)

print(f"Point O: {O}")
print(f"There are {num_neighbors} neighbors:")
for point, distance in nearest_neighbors:
    print(f"Point {point} is {distance:.2f} units away.")