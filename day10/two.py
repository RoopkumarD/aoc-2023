from typing import List

from flood_fill import find_starting_position, flood_fill
from gap import put_gap, remove_fillers
from simple_raycasting import simple_raycasting
from utils import Node, StackFrontier, print_colors, print_map

with open("./test2.txt", "r") as f:
    pipes = []
    start_position = (-1, -1)
    lines = [line.strip() for line in f.readlines()]
    for line in range(len(lines)):
        temp = []
        tempLine = lines[line].strip()
        for char in range(len(tempLine)):
            if tempLine[char] == "S":
                start_position = (line, char)
            temp.append(tempLine[char])
        pipes.append(temp)


def find_actions(
    cell: tuple[int, int], pipes: List[List[str]]
) -> List[tuple[int, int]]:
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


def find_loop(starting: tuple[int, int], pipes: List[List[str]]) -> Node:
    already_checked = set()
    other_ends = find_actions(starting, pipes)
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
            related_actions_list = find_actions(action_cell, pipes)
            filtered_list = []
            for a in related_actions_list:
                if a not in already_checked:
                    filtered_list.append(a)
            stack.add(Node(action_cell, node, filtered_list))

    return solution


def main(pipes: List[List[str]], start_position: tuple[int, int]):
    val = find_loop(start_position, pipes)
    loop_elem = [start_position]

    while val.parent != None:
        loop_elem.append(val.state)
        val = val.parent

    copied_map = []
    for i in range(len(pipes)):
        temp = []
        for j in range(len(pipes[0])):
            temp.append(0)
        copied_map.append(temp)

    for elem in loop_elem:
        x, y = elem
        copied_map[x][y] = 1

    print_map(copied_map)
    c = 1
    posn = find_starting_position(copied_map)

    while posn != (-1, -1):
        c += 1
        copied_map = flood_fill(copied_map, posn, c)
        posn = find_starting_position(copied_map)

    print_colors(copied_map)
    colors = dict()
    for i in range(len(copied_map)):
        for j in range(len(copied_map[0])):
            if copied_map[i][j] not in colors:
                colors[copied_map[i][j]] = list()

            colors[copied_map[i][j]].append((i, j))

    return [colors, loop_elem]


if __name__ == "__main__":
    print_map(pipes)
    gapped = put_gap(pipes)
    fillers = remove_fillers(gapped)
    print_map(gapped)

    start_position = (-1, -1)
    for i in range(len(gapped)):
        for j in range(len(gapped[0])):
            if gapped[i][j] == "S":
                start_position = (i, j)

    main_colors, loop_elem = main(gapped, start_position)

    sum = 0

    for i in range(2, max(main_colors.keys()) + 1):
        is_inside = simple_raycasting(gapped, main_colors[i], loop_elem)
        if is_inside:
            print(main_colors[i])
            final = set(main_colors[i]) - fillers
            print(final)
            sum += len(final)

    print(sum)
