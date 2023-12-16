from typing import List, Tuple


def multiply_vector_scalar(vector: Tuple[int, int], scalar: int) -> Tuple[int, int]:
    return (vector[0] * scalar, vector[1] * scalar)


def add_vectors(vector1: Tuple[int, int], vector2: Tuple[int, int]) -> Tuple[int, int]:
    return (vector1[0] + vector2[0], vector1[1] + vector2[1])


def rotate_vector(
    rotation_matrix: List[List[int]], vector: Tuple[int, int]
) -> Tuple[int, int]:
    transposed = list(zip(*rotation_matrix))

    return add_vectors(
        multiply_vector_scalar(transposed[0], vector[0]),
        multiply_vector_scalar(transposed[1], vector[1]),
    )


class Node:
    def __init__(self, state: Tuple[int, int], direction: Tuple[int, int]) -> None:
        self.state = state
        self.direction = direction

    def __repr__(self) -> str:
        return f"{self.state} -> {self.direction}"


class QueueFrontier:
    def __init__(self) -> None:
        self.queue = list()

    def add_node(self, node) -> None:
        self.queue.append(node)

    def remove_node(self):
        if self.is_empty() == True:
            raise Exception("Stack is empty")

        node = self.queue.pop(0)
        return node

    def is_empty(self):
        return len(self.queue) == 0


class GridWorld:
    def __init__(self, grid: List[List[str]]) -> None:
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])

    def find_actions(
        self, cell: Tuple[int, int], direction: Tuple[int, int]
    ) -> List[Tuple[int, int]]:
        actions = []

        if self.grid[cell[0]][cell[1]] == ".":
            new_action = add_vectors(cell, direction)
            if 0 <= new_action[0] < self.height and 0 <= new_action[1] < self.width:
                actions.append(new_action)
        elif self.grid[cell[0]][cell[1]] == "/":
            rotation_matrix = [[0, -1], [-1, 0]]
            new_action = add_vectors(rotate_vector(rotation_matrix, direction), cell)
            if 0 <= new_action[0] < self.height and 0 <= new_action[1] < self.width:
                actions.append(new_action)
        elif self.grid[cell[0]][cell[1]] == "\\":
            rotation_matrix = [[0, 1], [1, 0]]
            new_action = add_vectors(rotate_vector(rotation_matrix, direction), cell)
            if 0 <= new_action[0] < self.height and 0 <= new_action[1] < self.width:
                actions.append(new_action)
        elif self.grid[cell[0]][cell[1]] == "|":
            if direction[1] == 1 or direction[1] == -1:
                new_action = add_vectors(cell, (1, 0))
                if 0 <= new_action[0] < self.height and 0 <= new_action[1] < self.width:
                    actions.append(new_action)

                new_action = add_vectors(cell, (-1, 0))
                if 0 <= new_action[0] < self.height and 0 <= new_action[1] < self.width:
                    actions.append(new_action)
            else:
                new_action = add_vectors(cell, direction)
                if 0 <= new_action[0] < self.height and 0 <= new_action[1] < self.width:
                    actions.append(new_action)
        elif self.grid[cell[0]][cell[1]] == "-":
            if direction[0] == 1 or direction[0] == -1:
                new_action = add_vectors(cell, (0, 1))
                if 0 <= new_action[0] < self.height and 0 <= new_action[1] < self.width:
                    actions.append(new_action)

                new_action = add_vectors(cell, (0, -1))
                if 0 <= new_action[0] < self.height and 0 <= new_action[1] < self.width:
                    actions.append(new_action)
            else:
                new_action = add_vectors(cell, direction)
                if 0 <= new_action[0] < self.height and 0 <= new_action[1] < self.width:
                    actions.append(new_action)

        return actions

    def solve_grid(self, start_cell: Tuple[int, int], direction_info: Tuple[int, int]):
        # do note that this direction is not with respect to normal cartesian system
        # thats why direction = (y, x)
        start_node = Node(start_cell, direction_info)

        queue = QueueFrontier()
        queue.add_node(start_node)

        # later will be used to check for tile with light passing through it
        already_seen = set()
        already_checked = set()

        while len(queue.queue) != 0:
            node = queue.remove_node()
            already_seen.add(node.state)
            already_checked.add((node.state, node.direction))

            node_actions = self.find_actions(node.state, node.direction)
            for act in node_actions:
                direction = (act[0] - node.state[0], act[1] - node.state[1])
                if (act, direction) not in already_checked:
                    queue.add_node(Node(act, direction))

        return len(already_seen)
