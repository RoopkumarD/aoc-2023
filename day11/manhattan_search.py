from typing import List

from utils import manhattan_dist


class Node:
    def __init__(self, state: tuple[int, int], parent, actions: set) -> None:
        self.state = state
        self.parent = parent
        self.actions = actions

    def __repr__(self) -> str:
        return f"{self.state}"


class StackFrontier:
    def __init__(self) -> None:
        self.stack = []

    def add(self, node: Node):
        self.stack.append(node)

    def remove(self, goal: tuple[int, int]):
        if self.empty():
            raise Exception("Node can't be removed from empty stack")

        small_dist = 100000
        node_to_remove = None
        for node in self.stack:
            dist = manhattan_dist(node.state, goal)
            if dist < small_dist:
                small_dist = dist
                node_to_remove = node

        if node_to_remove == None:
            raise Exception("node_to_remove is None")

        self.stack.remove(node_to_remove)
        return node_to_remove

    def empty(self):
        return len(self.stack) == 0


class Manhattan_Search:
    def __init__(
        self,
        map_list: List[List[str]],
        initial: tuple[int, int],
        final: tuple[int, int],
    ) -> None:
        self.height = len(map_list)
        self.width = len(map_list[0])
        self.map_list = map_list
        self.initial = initial
        self.final = final
        self.solution = None

    def actions_available(self, coordinate: tuple[int, int]):
        actions = set()

        for i in range(coordinate[0] - 1, coordinate[0] + 2, 2):
            if 0 <= i < self.height:
                actions.add((i, coordinate[1]))

        for j in range(coordinate[1] - 1, coordinate[1] + 2, 2):
            if 0 <= j < self.width:
                actions.add((coordinate[0], j))

        return actions

    def solve(self):
        already_checked = set()
        stack = StackFrontier()
        stack.add(Node(self.initial, None, self.actions_available(self.initial)))

        while True:
            node = stack.remove(self.final)
            if node.state == self.final:
                self.solution = node
                break

            already_checked.add(node.state)

            for cell in node.actions:
                cell_actions = self.actions_available(cell)
                filtered_actions = cell_actions - already_checked
                stack.add(Node(cell, node, filtered_actions))

        return self.find_steps()

    def find_steps(self):
        if self.solution == None:
            raise Exception("Solution is None")

        steps = []

        count = -1
        while self.solution != None:
            steps.append(self.solution.state)
            self.solution = self.solution.parent
            count += 1

        return steps, count
