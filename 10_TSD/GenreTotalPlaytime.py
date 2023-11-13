n = int(input())
music = {}
for _ in range(n):
    raw = input().split(", ")
    genre = raw[2]
    time_list = list(map(int, raw[3].split(":")))
    time = int(time_list[0] * 60 + time_list[1])
    if genre not in music:
        music[genre] = 0
    music[genre] += time

res = []
for genre, time in music.items():
    res.append([time, genre])
res = sorted(res)[:-4:-1]

for x in res:
    toatl_time = "{}:{:02d}".format(x[0]//60, x[0]%60)
    print(x[1], "-->", toatl_time)