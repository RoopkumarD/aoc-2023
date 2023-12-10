from typing import List

with open("./input.txt", "r") as f:
    pipes = []
    start_position = (-1, -1)
    lines = f.readlines()
    for line in range(len(lines)):
        temp = []
        tempLine = lines[line].strip()
        for char in range(len(tempLine)):
            if tempLine[char] == "S":
                start_position = (line, char)
            temp.append(tempLine[char])
        pipes.append(temp)


def find_actions(cell: tuple[int, int]) -> List[tuple[int, int]]:
    actions = []
    if cell[0] - 1 >= 0:
        if pipes[cell[0]][cell[1]] in ["S", "|", "L", "J"]:
            x = cell[0] - 1
            y = cell[1]
            if (
                pipes[x][y] == "|"
                or pipes[x][y] == "F"
                or pipes[x][y] == "7"
                or pipes[x][y] == "S"
            ):
                actions.append((x, y))

    if cell[0] + 1 < len(pipes):
        if pipes[cell[0]][cell[1]] in ["S", "|", "7", "F"]:
            x = cell[0] + 1
            y = cell[1]
            if (
                pipes[x][y] == "|"
                or pipes[x][y] == "L"
                or pipes[x][y] == "J"
                or pipes[x][y] == "S"
            ):
                actions.append((x, y))

    if cell[1] - 1 >= 0:
        if pipes[cell[0]][cell[1]] in ["S", "-", "J", "7"]:
            x = cell[0]
            y = cell[1] - 1
            if (
                pipes[x][y] == "-"
                or pipes[x][y] == "L"
                or pipes[x][y] == "F"
                or pipes[x][y] == "S"
            ):
                actions.append((x, y))

    if cell[1] + 1 < len(pipes[0]):
        if pipes[cell[0]][cell[1]] in ["S", "-", "L", "F"]:
            x = cell[0]
            y = cell[1] + 1
            if (
                pipes[x][y] == "-"
                or pipes[x][y] == "J"
                or pipes[x][y] == "7"
                or pipes[x][y] == "S"
            ):
                actions.append((x, y))

    return actions


class Node:
    def __init__(self, state, parent, actions) -> None:
        self.state = state
        self.parent = parent
        self.actions = actions

    def __repr__(self) -> str:
        return f"{self.state}"


class StackFrontier:
    def __init__(self) -> None:
        self.stack = list()

    def add(self, node: Node):
        self.stack.append(node)

    def remove(self):
        if len(self.stack) == 0:
            raise Exception("Can't remove as Empty Stack")

        node = self.stack.pop()
        return node


def find_loop(starting: tuple[int, int]) -> Node:
    already_checked = set()
    other_ends = find_actions(starting)
    start_end = other_ends.pop()

    stack = StackFrontier()
    stack.add(Node(starting, None, [start_end]))
    solution = None

    while True:
        node = stack.remove()
        if node.state in other_ends:
            solution = node
            break

        already_checked.add(node.state)

        for action_cell in node.actions:
            related_actions_list = find_actions(action_cell)
            filtered_list = []
            for a in related_actions_list:
                if a not in already_checked:
                    filtered_list.append(a)
            stack.add(Node(action_cell, node, filtered_list))

    return solution


val = find_loop(start_position)
steps = 1

while val.parent != None:
    steps += 1
    val = val.parent

print(steps / 2)
