import math


def volume_of_sphere(radius):
    return 4/3*radius**3*math.pi


print("Enter radius of sphere:")
radius = float(input())
print(volume_of_sphere(radius))
