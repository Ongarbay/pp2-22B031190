s = input()
s = s.split()[::-1]
l = list()
for i in s:
    l.append(i)
print(" ".join(l))
