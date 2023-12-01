with open("./input.txt", "r") as f:
    input = f.read().split("\n")

mapping = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

# fuzzy finding array so that, later i can use them to do fuzzy finding
left_to_right = []
right_to_left = []

# inserting each sequence for fuzzy finding
# for example, two -> ["t", "tw", "two"]
for number in mapping.keys():
    word = ""
    for char in number:
        word += char
        left_to_right.append(word)


for number in mapping.keys():
    word = ""
    for char in range(len(number) - 1, -1, -1):
        word = number[char] + word
        right_to_left.append(word)


sum = 0

# iterating over each line
for word in input:
    if word == "":
        continue

    possible = ""
    first = None
    last = None
    length = len(word)

    # iterating from left
    for char in range(length):
        if 48 <= ord(word[char]) <= 57:
            first = word[char]
            possible = ""
            break

        possible += word[char]
        if possible not in left_to_right:
            # this basically mean that the possible is in fuzzy finding array
            # so we are removing those which is not a part in the array
            # for example, sth -> then we want th as if the word follows by ree
            # then we would have three and that is correct number
            check = ""
            for c in range(len(possible) + 1):
                check = possible[c:]
                if check in left_to_right:
                    break

            possible = check

        if possible in mapping:
            first = mapping[possible]
            possible = ""
            break

    # iterating from right
    for char in range(length - 1, -1, -1):
        if 48 <= ord(word[char]) <= 57:
            last = word[char]
            break

        possible = word[char] + possible
        if possible not in right_to_left:
            # same as above but doing it from right
            check = ""
            for c in range(len(possible), -1, -1):
                check = possible[0:c]
                if check in right_to_left:
                    break

            possible = check

        if possible in mapping:
            last = mapping[possible]
            possible = ""
            break

    sum += int(f"{first}{last}")


print(sum)
