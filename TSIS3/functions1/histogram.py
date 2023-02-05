def histogram(lst):
    for i in lst:
        print("*"*i)


print("Enter size of list")
n = int(input())
l = list()
print("Enter elements of list")
for i in range(n):
    x = int(input())
    l.append(x)
histogram(l)
