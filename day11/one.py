# from manhattan_search import Manhattan_Search
from utils import expand_map, manhattan_dist

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


map_list = expand_map(map_list, 1)
posn = dict()

for i in range(len(map_list)):
    for j in range(len(map_list[0])):
        if map_list[i][j] != ".":
            posn[map_list[i][j]] = (i, j)

keys = list(posn.keys())

sum = 0
for i in range(len(keys) - 1):
    for j in range(i + 1, len(keys)):
        dist = manhattan_dist(posn[keys[i]], posn[keys[j]])
        # print(dist, keys[i], keys[j])
        sum += dist

print(sum)

# overcomplicating stuff
# slow as shit
# sum = 0
# for i in range(len(keys) - 1):
#     for j in range(i + 1, len(keys)):
#         print(i, j)
#         _, count = Manhattan_Search(map_list, posn[keys[i]], posn[keys[j]]).solve()
#         sum += count
#
# print(sum)
