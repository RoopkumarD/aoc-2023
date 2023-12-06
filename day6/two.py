import math

with open("./input.txt", "r") as f:
    data = [int("".join(line.strip().split()[1:])) for line in f.readlines()]

recorded_time = data[0]
recorded_distance = data[1]

D = recorded_time**2 - 4 * recorded_distance

t1 = (recorded_time + (D**0.5)) / 2
t2 = (recorded_time - (D**0.5)) / 2

print(math.floor(t1) - math.ceil(t2) + 1)
