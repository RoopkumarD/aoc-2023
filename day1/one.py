with open("./input.txt", "r") as f:
    input = f.read().split("\n")

first = None
last = None

sum = 0

# going through each line
for word in input:
    if word == "":
        continue

    length = len(word)
    # iterating from left
    for char in range(length):
        if 48 <= ord(word[char]) <= 57:
            first = word[char]
            break

    # iterating from right
    for char in range(length - 1, -1, -1):
        if 48 <= ord(word[char]) <= 57:
            last = word[char]
            break

    sum += int(f"{first}{last}")
    first = None
    last = None


print(sum)
