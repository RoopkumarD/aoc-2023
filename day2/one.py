with open("./input.txt", "r") as f:
    input = f.read().split("\n")

max = {"blue": 14, "red": 12, "green": 13}
sum = 0

# extracting the data
for line in input:
    if line == "":
        continue

    separate = line.split(": ")
    id = int(separate[0].split(" ")[1])
    add_it = True

    rounds = separate[1].split("; ")

    for round in rounds:
        colors = round.split(", ")
        for color in colors:
            temp = color.split(" ")
            if int(temp[0]) > max[temp[1]]:
                add_it = False

    if add_it == True:
        sum += id


print(sum)
