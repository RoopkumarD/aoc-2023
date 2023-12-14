from rotate import calculate_load, one_cycle

with open("./input.txt", "r") as f:
    temp = [line.strip() for line in f.readlines()]
    data = []
    for line in temp:
        data.append((char for char in line))


CYCLES = 1000000000 - 1

checker = []
reoccurence_gap = []
matches_pattern_in_checker = None

initial = list(data)
checker.append(initial)

for i in range(1000):
    initial = one_cycle(initial)
    for j in range(len(checker)):
        if checker[j] == initial:
            if matches_pattern_in_checker == None:
                reoccurence_gap.append(i)
                matches_pattern_in_checker = j
            elif checker[matches_pattern_in_checker] == initial:
                if (
                    matches_pattern_in_checker != None
                    and j != matches_pattern_in_checker
                ):
                    raise Exception("not same j")

                reoccurence_gap.append(i)
                matches_pattern_in_checker = j

            break

    if len(reoccurence_gap) == 2:
        break

    checker.append(initial)


gap_between = reoccurence_gap[1] - reoccurence_gap[0]

m = (CYCLES - reoccurence_gap[0]) % gap_between
print(calculate_load(checker[matches_pattern_in_checker + m]))
