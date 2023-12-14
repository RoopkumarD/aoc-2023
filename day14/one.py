from typing import List

with open("./input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]


def transpose(data: List[str]):
    return list(zip(*data))


def count_load(data: List[str]):
    new_data = transpose(data)
    width = len(new_data[0])

    total = 0
    for line in new_data:
        i = 0
        for j in range(width):
            if line[j] == "O":
                total += width - i
                i += 1
            elif line[j] == "#":
                i = j + 1

    return total


print(count_load(data))
