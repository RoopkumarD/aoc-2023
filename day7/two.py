with open("./input.txt", "r") as f:
    input = [
        [line.strip().split()[0], int(line.strip().split()[1]), -1]
        for line in f.readlines()
    ]


# rank = {
#     "Five": 6,
#     "Four": 5,
#     "Full_House": 4,
#     "Three": 3,
#     "Two": 2,
#     "One": 1,
#     "High": 0,
# }
def replace_and_check(hand: str) -> str:
    components = []
    for char in hand:
        if char not in components:
            components.append([char, -1])

    for component in components:
        component[1] = categories(hand.replace("J", component[0]), 1)

    components = sorted(components, key=lambda c: c[1], reverse=True)
    return hand.replace("J", components[0][0])


def categories(hand: str, depth=0) -> int:
    if "J" in hand and depth == 0:
        hand = replace_and_check(hand)

    d = dict()
    for char in hand:
        if char not in d:
            d[char] = 0

        d[char] += 1

    if len(d) == 1:
        return 6
    elif len(d) == 2:
        l = sorted(list(d.values()))
        if l[0] == 1:
            return 5
        else:
            return 4
    elif len(d) == 3:
        l = sorted(list(d.values()))
        if l == [1, 1, 3]:
            return 3
        else:
            return 2
    elif len(d) == 4:
        return 1
    else:
        return 0


for i in input:
    i[2] = categories(i[0])

num_rank = {
    "J": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}


sorted_input = []
while len(input) != 0:
    smallest = input[0]
    removing = 0
    for i in range(len(input)):
        if input[i][2] < smallest[2]:
            smallest = input[i]
            removing = i
        elif input[i][2] == smallest[2]:
            for k in range(5):
                if num_rank[input[i][0][k]] < num_rank[smallest[0][k]]:
                    smallest = input[i]
                    removing = i
                    break
                elif num_rank[input[i][0][k]] > num_rank[smallest[0][k]]:
                    break

    sorted_input.append(smallest)
    input.pop(removing)

sum = 0
for i in range(len(sorted_input)):
    sum += sorted_input[i][1] * (i + 1)

print(sum)
