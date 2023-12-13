from typing import List

with open("./input.txt", "r") as f:
    temp = [line.strip() for line in f.readlines()]
    data = []
    t = []
    for line in temp:
        if line == "":
            data.append(t)
            t = []
        else:
            t.append(line)
    data.append(t)


def horizontanl_line_reflection(pattern: List[str]):
    line = []
    length = len(pattern)

    for i in range(length - 1):
        if pattern[i] == pattern[i + 1]:
            line.append(i)

    point = None

    for k in line:
        reflects = True
        for i in range(1, k + 1):
            one_end = k - i
            other_end = k + i + 1
            if other_end == length:
                break

            if pattern[one_end] != pattern[other_end]:
                reflects = False
                break

        if reflects == True:
            point = k + 1
            break

    return point


def convert_col_to_row(pattern: List[str]):
    new_pattern = []
    width = len(pattern[0])

    for i in range(width):
        temp = []
        for line in pattern:
            temp.append(line[i])

        new_pattern.append("".join(temp))

    return new_pattern


sum = 0
for i in data:
    h_r = horizontanl_line_reflection(i)
    if h_r != None:
        sum += 100 * h_r
        continue

    new_pattern = convert_col_to_row(i)
    v_r = horizontanl_line_reflection(new_pattern)
    if v_r != None:
        sum += v_r

print(sum)
