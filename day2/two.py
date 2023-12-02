with open("./input.txt", "r") as f:
    input = f.read().split("\n")

sum = 0

# extracting the data
for line in input:
    if line == "":
        continue

    separate = line.split(": ")
    val = {"red": 0, "blue": 0, "green": 0}

    rounds = separate[1].split("; ")

    for round in rounds:
        colors = round.split(", ")
        for color in colors:
            temp = color.split(" ")
            if val[temp[1]] < int(temp[0]):
                val[temp[1]] = int(temp[0])

    sum += val["red"] * val["blue"] * val["green"]


print(sum)
