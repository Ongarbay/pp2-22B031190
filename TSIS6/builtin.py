import math
import time


def multiply(lst):
    product = math.prod(lst)
    print(product)


def counter(string):
    lowers = 0
    uppers = 0
    for i in range(len(string)):
        if string[i].islower():
            lowers += 1
        elif string[i].isupper():
            uppers += 1
    print(f"Lower letters:{lowers}")
    print(f"Upper letters:{uppers}")


def palindrome(string):
    revstring = "".join(reversed(string))
    print(revstring)
    if string == revstring:
        print("This string is palidrome")
    else:
        print("This string is not palindrome")


def decode(number,miliseconds):
    time.sleep(miliseconds/1000)
    print(f"Square root of {number} after {miliseconds} is {math.sqrt(number)}")


def check(tuple):
    return all(tuple)
