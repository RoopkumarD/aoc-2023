from typing import List


def manhattan_dist(inital: tuple[int, int], goal: tuple[int, int]):
    return abs(goal[1] - inital[1]) + abs(goal[0] - inital[0])


def empty_rows(map_list: List[List[str]]):
    posn = []
    for i in range(len(map_list)):
        if len(set(map_list[i])) == 1:
            posn.append(i)

    return posn


def empty_cols(map_list: List[List[str]]):
    width = len(map_list[0])
    posn_to_add = []

    for i in range(width):
        no_elem = True
        for line in map_list:
            if line[i] != ".":
                no_elem = False
                break

        if no_elem == True:
            posn_to_add.append(i)

    return posn_to_add


def manhattan_dist_with_expand(
    inital: tuple[int, int],
    goal: tuple[int, int],
    expand_x: List[int],
    expand_y: List[int],
    expand: int,
):
    x = abs(goal[0] - inital[0])
    if goal[0] > inital[0]:
        x_range = range(inital[0], goal[0])
    else:
        x_range = range(goal[0], inital[0])

    for i in expand_x:
        if i in x_range:
            x += expand

    y = abs(goal[1] - inital[1])
    if goal[1] > inital[1]:
        y_range = range(inital[1], goal[1])
    else:
        y_range = range(goal[1], inital[1])

    for j in expand_y:
        if j in y_range:
            y += expand

    return x + y


def expand_map(map_list: List[List[str]], expand: int):
    map_list = expand_map_vertically(map_list, expand)
    map_list = expand_map_horizontally(map_list, expand)

    return map_list


def expand_map_vertically(map_list: List[List[str]], expand: int):
    length = len(map_list[0])

    new_map_list = []

    for line in map_list:
        if len(set(line)) == 1:
            for q in range(expand):
                new_map_list.append(["."] * length)

        new_map_list.append(line)

    return new_map_list


def expand_map_horizontally(map_list: List[List[str]], expand: int):
    width = len(map_list[0])
    height = len(map_list)

    posn_to_add = []

    for i in range(width):
        no_elem = True
        for line in map_list:
            if line[i] != ".":
                no_elem = False
                break

        if no_elem == True:
            posn_to_add.append(i)

    copied_list = []
    for i in range(height):
        temp = []
        for j in range(width):
            temp.append(map_list[i][j])
            if j in posn_to_add:
                for l in range(expand):
                    temp.append(".")

        copied_list.append(temp)

    return copied_list
