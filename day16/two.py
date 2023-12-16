from typing import List, Tuple

from utils import GridWorld

with open("./input.txt", "r") as f:
    data = [[char for char in line.strip()] for line in f.readlines()]

all_possible_start = []
height = len(data)
width = len(data[0])

for i in range(width):
    all_possible_start.append((0, i))
    all_possible_start.append((height - 1, i))

for j in range(height):
    all_possible_start.append((j, 0))
    all_possible_start.append((width - 1, 0))


def get_directions(cell: Tuple[int, int]):
    all_dir = []

    for i in range(cell[0] - 1, cell[0] + 2, 2):
        if 0 <= i < height:
            all_dir.append((i - cell[0], 0))

    for j in range(cell[1] - 1, cell[1] + 2, 2):
        if 0 <= j < width:
            all_dir.append((0, j - cell[1]))

    return all_dir


grid = GridWorld(data)

energized: List[int] = []
for s in all_possible_start:
    directions = get_directions(s)

    for d in directions:
        num_tiles = grid.solve_grid(s, d)
        energized.append(num_tiles)

print(max(energized))
