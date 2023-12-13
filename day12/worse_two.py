from copy import deepcopy
from typing import List, Set

from utils import another_fuzzy_pattern_checker, consistency, fuzzy_pattern_checker

with open("./test.txt", "r") as f:
    data = []
    temp = [line.strip().split() for line in f.readlines()]
    for line in temp:
        num = ",".join([line[1]] * 5)
        data.append(("?".join([line[0]] * 5), [int(i) for i in num.split(",")]))


def prep(spring_row: tuple[str, List[int]]):
    working_spring_num = len(spring_row[0]) - sum(spring_row[1])
    final = ["#" * i for i in spring_row[1]] + ["."] * working_spring_num
    return final


def arrangements(
    spring_row: tuple[str, List[int]],
    list_val: List[str],
    final_list: List[str],
    duplicates: Set,
):
    if len(list_val) == 0:
        final_string = "".join(final_list)
        if fuzzy_pattern_checker(spring_row[0], final_string) == True:
            return 1
        else:
            return 0
    else:
        sum = 0
        for i in range(len(list_val)):
            # to avoid continuous '#'
            if len(final_list) >= 1 and (
                list_val[i][0] == "#" and final_list[-1][0] == "#"
            ):
                continue

            # check nums consistency
            if consistency(final_list + [list_val[i]], spring_row[1]) == False:
                continue

            # check pattern
            if (
                another_fuzzy_pattern_checker(
                    spring_row[0], "".join(final_list + [list_val[i]])
                )
                == False
            ):
                continue

            # check duplicates
            if tuple(final_list + [list_val[i]]) in duplicates:
                continue

            copied_list_val = deepcopy(list_val)
            new_final_list = list(final_list)

            elem = copied_list_val.pop(i)
            new_final_list += [elem]

            duplicates.add(tuple(new_final_list))

            sum += arrangements(spring_row, copied_list_val, new_final_list, duplicates)

        return sum


sum_total = 0
for row in data:
    print(row)
    duplicates = set()
    k = prep(row)
    val = arrangements(row, k, [], duplicates)
    sum_total += val

print(sum_total)
