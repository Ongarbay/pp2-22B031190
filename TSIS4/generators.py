import generators


def squares_generator():
    print("Enter a number:", end=" ")
    n = int(input())
    square = (x*x for x in range(n+1))


def even():
    print("Enter a number:", end=" ")
    n = int(input())
    div = (x for x in range(0, n+1, 2))
    for i in div:
        print(i, end=" ")


def divided():
    print("Enter a number:", end=" ")
    n = int(input())
    div = (x for x in range(0, n+1, 12))
    # or div=(x for x in range(n+1) if (x % 12 == 0))
    for i in div:
        print(i, end=' ')


def rev():
    l = []
    print("Enter a number:", end=" ")
    n = int(input())
    numbers = range(n, -1, -1)
    for i in numbers:
        l.append(i)
    return l


def squares():
    print("Enter a number a :", end=" ")
    a = int(input())
    print("Enter a number b :", end=" ")
    b = int(input())
    square = (x**2 for x in range(a, b+1))
    for i in square:
        print(i, end=" ")


