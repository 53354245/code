import math

def calculate_distances(O, list, max):
    distances = []
    for point in list:
        distance = math.sqrt((O[0] - point[0])**2 + (O[1] - point[1])**2)
        if distance <= max:
            distances.append((point, distance))
    return distances

max = 3

list = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)] #tự nhập tọa độ
O = (x, y)

distances = calculate_distances(O, list, max)

print(f"Starting Point: {O}")
print("Distances from the starting point to points in the list (max distance 3):")
for point, distance in distances:
    print(f"Distance to point {point}: {distance:.2f}")
