raw = input().strip()
cartoon = {}
animals_type = []
while raw != "q":
    raw = raw.split(", ")
    if raw[1] not in cartoon:
        cartoon[raw[1]] = []
        animals_type.append(raw[1])
    cartoon[raw[1]].append(raw[0])
    raw = input().strip()

for x in animals_type:
    print(x + ": ", end="")
    print(", ".join(cartoon[x]))
