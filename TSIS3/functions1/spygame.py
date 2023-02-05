def spygame(lst):
    for i in range(len(lst)-2):
        if lst[i]==lst[i+1]==0 and lst[i+2]==7:
            return True
    return False

print("Enter size of list")
n=int(input())
print("Enter elements of list")
l=list()
for i in range(n):
    x=int(input())
    l.append(x)
print(spygame(l))