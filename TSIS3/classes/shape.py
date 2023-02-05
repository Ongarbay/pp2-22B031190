class Shape:
    def __init__(self, length):
        self.length = length

    class Square:
        def __init__(self, side):
            self.side = side

    def area(self):
        return self.length*self.length


n = Shape(int(input()))
print(Shape.area(n))
