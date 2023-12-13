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
            t.append([char for char in line])
    data.append(t)


def transpose(pattern: List[List[str]]):
    # zip("AB", "CD") => ("A", "C") and ("B", "D")
    return list(zip(*pattern))


def check_reflections(pattern: List[List[str]]) -> int | None:
    line = []
    length = len(pattern)

    for i in range(length - 1):
        if "".join(pattern[i]) == "".join(pattern[i + 1]):
            line.append(i)

    point = []

    for k in line:
        reflects = True
        for i in range(1, k + 1):
            one_end = k - i
            other_end = k + i + 1
            if other_end == length:
                break

            if "".join(pattern[one_end]) != "".join(pattern[other_end]):
                reflects = False
                break

        if reflects == True:
            point.append(k)
            break

    final = None
    for i in point:
        final = i + 1

    return final


def fix_smudge_check_reflection(pattern: List[List[str]]):
    rows, cols = len(pattern), len(pattern[0])
    total = 0

    h_l, v_l = set(), set()
    for row in range(rows):
        for col in range(cols):
            original_horizontal = check_reflections(pattern)
            original_vertical = check_reflections(transpose(pattern))

            pattern[row][col] = "#" if pattern[row][col] == "." else "."

            new_horizontal = check_reflections(pattern)
            if (
                new_horizontal != original_horizontal
                and new_horizontal != None
                and new_horizontal not in h_l
            ):
                h_l.add(new_horizontal)
                total += 100 * new_horizontal

            new_vertical = check_reflections(transpose(pattern))
            if (
                new_vertical != original_vertical
                and new_vertical != None
                and new_vertical not in v_l
            ):
                v_l.add(new_vertical)
                total += new_vertical

            # making the pattern in previous mode
            pattern[row][col] = "#" if pattern[row][col] == "." else "."

    return total


sum = 0
for i in data:
    k = fix_smudge_check_reflection(i)
    sum += k
print(sum)
