from utils import GridWorld

with open("./input.txt", "r") as f:
    data = [[char for char in line.strip()] for line in f.readlines()]


grid = GridWorld(data)
num_tiles = grid.solve_grid((0, 0), (0, 1))
print(num_tiles)
