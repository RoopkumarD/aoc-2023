from utils import empty_cols, empty_rows, manhattan_dist_with_expand

with open("./input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    map_list = []
    count = 0
    for i in range(len(lines)):
        temp = []
        for j in range(len(lines[0])):
            if lines[i][j] == "#":
                count += 1
                temp.append(str(count))
            else:
                temp.append(lines[i][j])
        map_list.append(temp)


posn = dict()

empty_r = empty_rows(map_list)
empty_c = empty_cols(map_list)

for i in range(len(map_list)):
    for j in range(len(map_list[0])):
        if map_list[i][j] != ".":
            posn[map_list[i][j]] = (i, j)

keys = list(posn.keys())

sum = 0
for i in range(len(keys) - 1):
    for j in range(i + 1, len(keys)):
        dist = manhattan_dist_with_expand(
            posn[keys[i]], posn[keys[j]], empty_r, empty_c, 1000000 - 1
        )
        sum += dist

print(sum)
