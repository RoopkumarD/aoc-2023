import random
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


def generate_random_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
