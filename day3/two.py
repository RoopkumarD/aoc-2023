with open("./input", "r") as f:
    input = [line.strip() for line in f.readlines()]

imp = dict()

col = len(input[0])
row = len(input)
r = range(48, 58)


def check_for_stars(i: int, j: int) -> None | tuple:
    for k in range(-1, 2):
        for m in range(-1, 2):
            if 0 <= i + k < row and 0 <= j + m < col:
                val = input[i + k][j + m]

                if val == "*":
                    return (i + k, j + m)

    return None


for i in range(row):
    num = ""
    near_symbol = False
    value_near_star = None
    for j in range(col):
        if ord(input[i][j]) in r:
            num += input[i][j]
            if near_symbol == False:
                value_near_star = check_for_stars(i, j)
                if value_near_star != None:
                    near_symbol = True
                    if value_near_star not in imp:
                        imp[value_near_star] = []

        elif num != "":
            if near_symbol == True:
                imp[value_near_star].append(int(num))

            num = ""
            near_symbol = False

        if j == col - 1:
            if num != "":
                if near_symbol == True:
                    imp[value_near_star].append(int(num))

                num = ""
                near_symbol = False


sum = 0
for star in imp:
    if len(imp[star]) == 2:
        sum += imp[star][0] * imp[star][1]

print(sum)
