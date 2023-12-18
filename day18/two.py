from typing import Tuple

from flood_fill import find_starting_position, flood_fill
from ppm_maker import create_ppm
from raycasting import raycast

with open("./test.txt", "r") as f:
    data = []
    temp = [line.strip().split() for line in f.readlines()]
    for line in temp:
        m = line[2].strip("()")[1:]
        steps = m[:-1]
        dir = m[-1]

        if dir == "0":
            direction = "R"
        elif dir == "1":
            direction = "D"
        elif dir == "2":
            direction = "L"
        elif dir == "3":
            direction = "U"
        else:
            raise Exception("Different last digit")

        data.append((direction, int(steps, 16), line[2].strip("()")))


row_low = 0
col_low = 0
row_high = 0
col_high = 0
row_current = 0
col_current = 0
edge_coordinate = set((0, 0))


def dug_according_instruction(
    instruction: Tuple[str, int, str], row_current: int, col_current: int
):
    new_edge_coordinates = set()

    if instruction[0] == "D":
        for j in range(instruction[1]):
            row_current += 1
            new_edge_coordinates.add((row_current, col_current))
    elif instruction[0] == "L":
        for j in range(instruction[1]):
            col_current -= 1
            new_edge_coordinates.add((row_current, col_current))
    elif instruction[0] == "R":
        for j in range(instruction[1]):
            col_current += 1
            new_edge_coordinates.add((row_current, col_current))
    elif instruction[0] == "U":
        for j in range(instruction[1]):
            row_current -= 1
            new_edge_coordinates.add((row_current, col_current))

    return new_edge_coordinates, row_current, col_current


for line in data:
    new_edge_coordinates, rc, cc = dug_according_instruction(
        line, row_current, col_current
    )

    edge_coordinate = edge_coordinate.union(new_edge_coordinates)
    row_current = rc
    col_current = cc

    if row_current > row_high:
        row_high = row_current
    elif row_current < row_low:
        row_low = row_current

    if col_current > col_high:
        col_high = col_current
    elif col_current < col_low:
        col_low = col_current


grid = []
for i in range(row_low, row_high + 1):
    temp = [0] * (col_high - col_low + 1)
    for j in range(col_low, col_high + 1):
        if (i, j) in edge_coordinate:
            temp[j - col_low] = 1
    grid.append(temp)


posn = find_starting_position(grid)
color = 2
while posn != (-1, -1):
    grid = flood_fill(grid, posn, color)
    color += 1
    posn = find_starting_position(grid)


colors_with_posn = dict()

for i in range(row_high - row_low + 1):
    for j in range(col_high - col_low + 1):
        if grid[i][j] not in colors_with_posn:
            colors_with_posn[grid[i][j]] = []
        colors_with_posn[grid[i][j]].append((i, j))

points_color_inside = [1]

for key in colors_with_posn:
    if key == 1:
        continue
    if raycast(grid, colors_with_posn[key][0]) == True:
        points_color_inside.append(key)

print(points_color_inside)

create_ppm(grid, "grid")

for i in colors_with_posn:
    print(i, len(colors_with_posn[i]))

total = 0
for j in points_color_inside:
    total += len(colors_with_posn[j])

print(total)
