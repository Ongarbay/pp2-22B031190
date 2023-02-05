def unique_array(lst):
    ans = []
    for i in range(len(lst)):
        check = False
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                if i != j:
                    check = True
        if check != 1:
            ans.append(lst[i])
    return ans


print("Enter size of list:")
n = int(input())
print("Enter elements of list:")
l = list()
for i in range(n):
    x = int(input())
    l.append(x)
print(unique_array(l))
