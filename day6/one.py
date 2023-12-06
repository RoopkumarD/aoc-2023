with open("./input.txt", "r") as f:
    temp = [line.strip().split()[1:] for line in f.readlines()]
    input = []
    for line in temp:
        temporary = []
        for i in line:
            temporary.append(int(i))

        input.append(temporary)


final = 1
for j in range(len(input[0])):
    possible = 0
    for i in range(input[0][j] + 1):
        speed = i
        distance = speed * (input[0][j] - i)
        if distance > input[1][j]:
            possible += 1

    final = final * possible

print(final)
