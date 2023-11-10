n = int(input())
res = []
for _ in range(n):
    raw = input().split(", ")
    genre = raw[2]
    time_list = list(map(int, raw[3].split(":")))
    time = int(time_list[0] * 60 + time_list[1])
    res.append([time, genre])

res.sort(reversed=True)
for x in res:
    print(x[1], "-->", x[0]//60, ":", x[0]%60)