from typing import List


def simple_raycasting(
    pipes: List[List[int]],
    posn_list: List[tuple[int, int]],
    loop: List[tuple[int, int]],
):
    width = len(pipes[0])

    for posn in posn_list:
        contact = 0
        current_posn = posn
        for i in range(posn[1], width):
            current_posn = (current_posn[0], current_posn[1] + 1)
            x, y = current_posn

            if current_posn in loop and pipes[x][y] != "-":
                contact += 1

        if contact % 2 == 0:
            return False
        else:
            return True
