class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def area(self):
        return self.length*self.width


n=Rectangle(int(input()),int(input()))
print(Rectangle.area(n))