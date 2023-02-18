import math


def degree_to_radian():
    print("Input degree:", end=" ")
    d = int(input())
    r = math.radians(d)
    print(f"Output radian: {r:.6}")


def area_of_trapezoid():
    print("Height:", end=" ")
    h = int(input())
    print("Base, first value:", end=" ")
    b1 = int(input())
    print("Base, second value:", end=" ")
    b2 = int(input())
    S = (b1+b2)/2*h
    print(f"Expected output: {S}")


def area_of_polygon():
    print("Input number of sides:", end=' ')
    n = int(input())
    print("Input the length of a side:", end=" ")
    l = int(input())
    A = n*l*(l/2)/math.tanh(180/n)/2
    print(f"The area of the polygon is:{A}")


def area_of_parallegram():
    print("Length of base:", end=" ")
    l = int(input())
    print("Height of parallelogram:", end=' ')
    h = int(input())
    print(f"Expected Output:{l*h}")
