from typing import List

from utils import Node, StackFrontier


def find_starting_position(arr: List[List[int]]) -> tuple[int, int]:
    posn = (-1, -1)

    for line in range(len(arr)):
        for i in range(len(arr[0])):
            if arr[line][i] == 0:
                posn = (line, i)
                break

    return posn


def get_actions(pipes: List[List[int]], posn: tuple[int, int]):
    actions = []

    for x in range(posn[0] - 1, posn[0] + 2, 2):
        if 0 <= x < len(pipes):
            if pipes[x][posn[1]] == 0:
                actions.append((x, posn[1]))

    for y in range(posn[1] - 1, posn[1] + 2, 2):
        if 0 <= y < len(pipes[0]):
            if pipes[posn[0]][y] == 0:
                actions.append((posn[0], y))

    return actions


def flood_fill(
    pipes: List[List[int]], posn: tuple[int, int], color: int
) -> List[List[int]]:
    related_actions = get_actions(pipes, posn)
    stack = StackFrontier()
    stack.add(Node(posn, None, related_actions))

    while True:
        if stack.empty():
            break

        node = stack.remove()
        x, y = node.state
        pipes[x][y] = color

        for cell in node.actions:
            stack.add(Node(cell, node, get_actions(pipes, cell)))

    return pipes
