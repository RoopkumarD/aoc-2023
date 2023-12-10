from typing import List


def put_gap(pipes: List[List[str]]):
    new_arr = []

    for i in range(len(pipes)):
        temp = []
        for j in range(len(pipes[0])):
            temp.append(pipes[i][j])

            if pipes[i][j] in ["-", "F", "S", "L"]:
                temp.append("-")
            else:
                temp.append(" ")

        new_arr.append(temp)

    return new_arr


def remove_fillers(pipes: List[List[str]]):
    fillers = set()
    for i in range(len(pipes)):
        for j in range(len(pipes[0])):
            if pipes[i][j] == " ":
                fillers.add((i, j))

    return fillers
