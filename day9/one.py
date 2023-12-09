from typing import List

with open("./input.txt", "r") as f:
    data = []
    for line in f.readlines():
        temp = []
        for i in line.strip().split():
            temp.append(int(i))

        data.append(temp)


def find_last_elem(seqs: List):
    if len(set(seqs)) == 1:
        return seqs[0]

    new_list = []
    for i in range(1, len(seqs)):
        new_list.append(seqs[i] - seqs[i - 1])

    return seqs[-1] + find_last_elem(new_list)


sum = 0
for r in data:
    sum += find_last_elem(r)

print(sum)
