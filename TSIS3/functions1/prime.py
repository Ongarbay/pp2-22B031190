def filter_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print("Enter size of list:")
n = int(input())
print("Enter elements of list:")
l = list()
for i in range(n):
    x = int(input())
    if filter_prime(x):
        l.append(x)
print(l)
