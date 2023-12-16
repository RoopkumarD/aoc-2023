with open("./input.txt", "r") as f:
    data = f.read().strip().split(",")


def hash_algorithm(string: str) -> int:
    initial = 0

    for char in string:
        initial += ord(char)
        initial = (initial * 17) % 256

    return initial


buckets = []
for i in range(256):
    buckets.append([])

label_marker = dict()

for i in data:
    if i[-1] == "-":
        k = i[:-1]
        num = None
    else:
        k = i[:-2]
        num = i[-1]

    box = hash_algorithm(k)

    if k not in label_marker:
        label_marker[k] = None

    if num != None:
        if label_marker[k] != None:
            buckets[box][label_marker[k][1]] = [k, int(num)]
        else:
            buckets[box].append([k, int(num)])
            label_marker[k] = (box, len(buckets[box]) - 1)
    else:
        if label_marker[k] != None:
            buckets[box].pop(label_marker[k][1])
            label_marker[k] = None
            for m in range(len(buckets[box])):
                label_marker[buckets[box][m][0]] = (box, m)


total = 0
for key in label_marker:
    if label_marker[key] != None:
        total += (
            (label_marker[key][0] + 1)
            * (label_marker[key][1] + 1)
            * (buckets[label_marker[key][0]][label_marker[key][1]][1])
        )

print(total)
