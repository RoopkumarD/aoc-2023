with open("./test.txt", "r") as f:
    instructions = f.readline().strip()
    f.readline()
    nodes = dict()
    for line in f.readlines():
        temp = line.strip().split(" = ")
        k = temp[1].strip("()").split(", ")
        nodes[temp[0]] = {"L": k[0], "R": k[1]}


steps = 0


def find_steps(nodes, instructions, current, final):
    global steps
    for instruct in instructions:
        current = nodes[current][instruct]
        steps += 1

    if current != final:
        find_steps(nodes, instructions, current, final)

    return


find_steps(nodes, instructions, "AAA", "ZZZ")
print(steps)
