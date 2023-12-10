from typing import List


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

    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False


def print_map(arr: List[List]):
    for line in arr:
        for i in line:
            print(i, end="")
        print()


def print_colors(arr: List[List]):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if 10 <= arr[i][j] < 100:
                print(arr[i][j], end=" ")
            else:
                print(arr[i][j], end="  ")
        print()
