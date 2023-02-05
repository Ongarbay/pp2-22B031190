print("Choose one of functions")
print("1.Unique_array    2.Volume_of_sphere    3.Histogram")
print("4.Ounces    5.Spygame    6.Heads,Legs")
print("7.Filter_prime    8.has_33    9.Celcius")
print("If you choose 0 then,calculator will stop working")
n = int(input())
while n != 0:
    if n == 1:
        from unique import unique_array
    elif n == 2:
        from volume import volume_of_sphere
    elif n == 3:
        from histogram import histogram
    elif n == 4:
        from ounces import ounces
    elif n == 5:
        from spygame import spygame
    elif n == 6:
        from heads_legs import solve
    elif n == 7:
        from prime import filter_prime
    elif n == 8:
        from has__33 import has__33
    elif n == 9:
        from fahrenheit import celcius
    else:
        print("Choose the number 1-9 or 0 to stop calculator")
    print("Choose one of functions")
    print("1.Unique_array    2.Volume_of_sphere    3.Histogram")
    print("4.Ounces    5.Spygame    6.Heads,Legs")
    print("7.Filter_prime    8.has_33    9.Celcius")
    n = int(input())
print("Well done!")
