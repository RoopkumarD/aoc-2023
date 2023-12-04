with open("./input.txt", "r") as f:
    input = [line.strip() for line in f.readlines()]

d = dict()

for card in input:
    id = int(card.split(": ")[0].split()[1])
    if id not in d:
        d[id] = 1
    else:
        d[id] += 1

    nums = card.split(": ")[1].split(" | ")
    winning_str = nums[0].split()
    chance_str = nums[1].split()
    winning = set([int(i) for i in winning_str])
    chance = set([int(i) for i in chance_str])

    common = len(winning.intersection(chance))

    if common != 0:
        for k in range(1, common + 1):
            if id + k <= len(input):
                if id + k not in d:
                    d[id + k] = 0

                d[id + k] = d[id + k] + 1 * d[id]


print(sum(d.values()))
