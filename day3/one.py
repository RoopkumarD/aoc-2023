with open("./input", "r") as f:
    input = [line.strip() for line in f.readlines()]

col = len(input[0])
row = len(input)
sum = 0
r = range(48, 58)


def check_for_symbols(i: int, j: int) -> bool:
    r = range(48, 58)
    for k in range(-1, 2):
        for m in range(-1, 2):
            if 0 <= i + k < row and 0 <= j + m < col:
                val = input[i + k][j + m]

                if ord(val) not in r and val != ".":
                    return True

    return False


for i in range(row):
    num = ""
    near_symbol = False
    for j in range(col):
        if ord(input[i][j]) in r:
            num += input[i][j]
            if near_symbol == False:
                near_symbol = check_for_symbols(i, j)

        elif num != "":
            if near_symbol == True:
                sum += int(num)

            num = ""
            near_symbol = False

        if j == col - 1:
            if num != "":
                if near_symbol == True:
                    sum += int(num)

                num = ""
                near_symbol = False


print(sum, "sum")
