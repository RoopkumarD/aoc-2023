from typing import List


def calculate_load(data: List[tuple[str, ...]]):
    height = len(data)
    total = 0

    for i in range(height):
        total += data[i].count("O") * (height - i)

    return total


def transpose(data: List[tuple[str, ...]]):
    return list(zip(*data))


def reverse_direction(data: List[tuple[str, ...]]):
    new_list = [tuple(reversed(line)) for line in data]
    return new_list


def one_cycle(data: List[tuple[str, ...]]):
    north = transpose(rotate(transpose(data)))
    west = rotate(north)
    south = transpose(reverse_direction(rotate(reverse_direction(transpose(west)))))
    east = reverse_direction(rotate(reverse_direction(south)))

    return east


def rotate(data: List[tuple[str, ...]]):
    after_rotation = []
    width = len(data[0])

    for line in data:
        i = 0
        temp = []
        for j in range(width):
            if line[j] == "O":
                temp.append(line[j])
                i += 1
            elif line[j] == "#":
                temp = temp + ["."] * (j - i)
                temp.append(line[j])
                i = j + 1

        temp = temp + ["."] * (width - len(temp))
        after_rotation.append("".join(temp))

    return after_rotation


if __name__ == "__main__":
    with open("./test.txt", "r") as f:
        temp = [line.strip() for line in f.readlines()]
        data = []
        for line in temp:
            data.append((char for char in line))
