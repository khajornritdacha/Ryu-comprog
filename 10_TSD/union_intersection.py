n = int(input())
un = set()
inter = set()
for i in range(n):
    raw = set(map(int, input().split()))
    if i == 0:
        un = raw
        inter = raw
    else:
        un = un.union(raw)
        inter = inter.intersection(raw)



print(len(un))
print(len(inter))
