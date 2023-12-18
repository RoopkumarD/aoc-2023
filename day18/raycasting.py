from typing import List, Tuple


def raycast(grid: List[List[int]], posn: Tuple[int, int]):
    directions = 0
    height = len(grid)
    width = len(grid[0])

    # up direction
    temp = 0
    for i in range(posn[0], -1, -1):
        if grid[i][posn[1]] == 1:
            temp += 1

    if temp % 2 != 0:
        directions += 1

    # down direction
    temp = 0
    for i in range(posn[0], height):
        if grid[i][posn[1]] == 1:
            temp += 1

    if temp % 2 != 0:
        directions += 1

    # left direction
    temp = 0
    for i in range(posn[1], -1, -1):
        if grid[posn[0]][i] == 1:
            temp += 1

    if temp % 2 != 0:
        directions += 1

    # right direction
    temp = 0
    for i in range(posn[1], width):
        if grid[posn[0]][i] == 1:
            temp += 1

    if temp % 2 != 0:
        directions += 1

    # else
    if directions >= 3:
        return True
    else:
        return False
