import math

from utils import common_number

with open("./test.txt", "r") as f:
    instructions = f.readline().strip()
    f.readline()
    nodes = dict()
    for line in f.readlines():
        temp = line.strip().split(" = ")
        k = temp[1].strip("()").split(", ")
        nodes[temp[0]] = {"L": k[0], "R": k[1]}


mapping = dict()

for node in nodes:
    if node[-1] not in mapping:
        mapping[node[-1]] = []

    mapping[node[-1]].append(node)


def find_steps_one(nodes, instructions, current, final):
    steps = 0
    current_node = current
    redo = True

    while redo:
        for instruct in instructions:
            current_node = nodes[current_node][instruct]
            steps += 1

        if current_node[-1] == final:
            redo = False

    return steps


steps_list = []
for i in mapping["A"]:
    steps_list.append(find_steps_one(nodes, instructions, i, "Z"))

print(common_number(steps_list))


# did this to find about periodic behaviour
def find_steps_final(nodes, instructions, current):
    current_node = current

    for instruct in instructions:
        current_node = nodes[current_node][instruct]

    return current_node


def create_instructions(instructions, num):
    first = ""
    other = 0

    length = len(instructions)
    for i in range(num):
        if (num - i) % length == 0:
            first = instructions * math.floor((num - i) / length)
            other = i
            break

    for i in range(other):
        first += instructions[i % len(instructions)]

    return first


# for i in range(1, 10):
#     node = find_steps_final(nodes, create_instructions(instructions, i * 12737), "CQA")
#     print(node)


# shitty brute force method
def find_steps(nodes, instructions, current, final):
    steps = 0
    current_nodes = current
    new_nodes = []
    redo = True

    while redo:
        print(current_nodes, steps)
        for instruct in instructions:
            for nxt_node in current_nodes:
                new_nodes.append(nodes[nxt_node][instruct])

            steps += 1
            current_nodes = new_nodes
            new_nodes = []

        count = 0
        for node in current_nodes:
            if node[-1] == final:
                count += 1

        if count == len(current_nodes):
            redo = False

    return steps
