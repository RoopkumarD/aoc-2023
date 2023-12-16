with open("./input.txt", "r") as f:
    data = f.read().strip().split(",")


def hash_algorithm(string: str) -> int:
    initial = 0

    for char in string:
        initial += ord(char)
        initial = (initial * 17) % 256

    return initial


sum = 0
for i in data:
    sum += hash_algorithm(i)

print(sum)
