class string:
    def __init__(self, string):
        self.string = string

    def getString(self):
        return self.string

    def printString(self):
        self.string = self.string.upper()
        return self.string


s = string(input())
t = s.getString()
print(t)
up = s.printString()
print(up)
