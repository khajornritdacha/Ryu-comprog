res = []
for i in range(int(input())):
    raw = input()
    cnt = 0
    for x in raw:
        if x != ".":
            break
        cnt += 1
    res.append(raw[cnt//2: ])

print("\n".join(res))
