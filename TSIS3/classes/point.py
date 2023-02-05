import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, x1, y1):
        self.x = x1
        self.y = y1
        return Point(self.x, self.y)

    def dist(self):
        return math.sqrt((self.x)**2+(self.y)**2)


xy = Point(int(input()), int(input()))
Point.show(xy)

distance = Point.dist(xy)
print(distance)

xy = Point.move(xy, int(input()), int(input()))
Point.show(xy)
