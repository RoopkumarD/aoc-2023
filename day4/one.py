with open("./input.txt", "r") as f:
    input = [line.strip() for line in f.readlines()]

sum = 0

for card in input:
    nums = card.split(": ")[1].split(" | ")
    winning_str = nums[0].split()
    chance_str = nums[1].split()
    winning = set([int(i) for i in winning_str])
    chance = set([int(i) for i in chance_str])

    common = len(winning.intersection(chance))

    if common != 0:
        points = 2 ** (common - 1)
        sum += points


print(sum)
