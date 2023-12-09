from typing import List

with open("./input.txt", "r") as f:
    data = []
    for line in f.readlines():
        temp = []
        for i in line.strip().split():
            temp.append(int(i))

        data.append(temp)


def find_first_elem(seqs: List[int]):
    if len(set(seqs)) == 1:
        return seqs[0]

    new_list = []
    for i in range(1, len(seqs)):
        new_list.append(seqs[i] - seqs[i - 1])

    return seqs[0] - find_first_elem(new_list)


sum = 0
for r in data:
    sum += find_first_elem(r)

print(sum)
