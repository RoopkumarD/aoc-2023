from copy import deepcopy
from typing import Dict, List, Set

from utils import consistency, fuzzy_pattern_checker, pattern_checker

with open("./input.txt", "r") as f:
    data = [line.strip().split() for line in f.readlines()]


# def prep(spring_row: List[str]):
#     num_list = [int(i) for i in spring_row[1].split(",")]
#     string_length = len(spring_row[0])
#
#     working_spring_num = string_length - sum(num_list)
#     defective_springs = []
#     for i in num_list:
#         defective_springs.append("#" * i)
#
#     final = list(defective_springs)
#     for j in range(working_spring_num):
#         final.append(".")
#
#     return final
#
#
# def list_permutations(
#     original_row: List[str], list_val: List[str], final_list: List[str], duplicates: Set
# ):
#     if len(list_val) == 0:
#         final_string = "".join(final_list)
#
#         if fuzzy_pattern_checker(original_row[0], final_string) == True:
#             return 1
#         else:
#             return 0
#     else:
#         sum = 0
#         for i in range(len(list_val)):
#             copied_list_val = deepcopy(list_val)
#             new_final_list = list(final_list)
#
#             elem = copied_list_val.pop(i)
#             new_final_list += [elem]
#
#             if consistency(new_final_list, original_row[1]) == False:
#                 continue
#
#             pass_on = True
#             # so that, we don't have continuous '#' joined
#             for o in range(len(new_final_list)):
#                 if o > 0:
#                     if new_final_list[o][0] == "#" and new_final_list[o - 1][0] == "#":
#                         pass_on = False
#                         break
#
#             if pass_on == True:
#                 if tuple(new_final_list) not in duplicates:
#                     duplicates.add(tuple(new_final_list))
#                     sum += list_permutations(
#                         original_row, copied_list_val, new_final_list, duplicates
#                     )
#
#         return sum
#
#
# sum_total = 0
# for row in data:
#     print(row)
#     duplicates = set()
#     k = prep(row)
#     val = list_permutations(row, k, [], duplicates)
#     sum_total += val
#
# print(sum_total)


# naive solution
# 2**n exponential explode
def prep(data: List[str]):
    posn = dict()
    posn_set = set()
    for i in range(len(data[0])):
        if data[0][i] == "?":
            posn[i] = ""
            posn_set.add(i)

    combination_sum = combinations(data, posn, posn_set)
    return combination_sum


def combinations(data: List[str], posn: Dict, posn_set: Set):
    if len(posn_set) == 0:
        possible_struct = [char for char in data[0]]

        for key in posn:
            possible_struct[key] = posn[key]

        if pattern_checker("".join(possible_struct), data[1]):
            # print("".join(possible_struct))
            return 1
        else:
            return 0
    else:
        copied_posn_set = deepcopy(posn_set)
        elem = copied_posn_set.pop()

        dot_possibility = deepcopy(posn)
        dot_possibility[elem] = "."
        dot_sum = combinations(data, dot_possibility, copied_posn_set)

        hash_possibility = deepcopy(posn)
        hash_possibility[elem] = "#"
        hash_sum = combinations(data, hash_possibility, copied_posn_set)

        return dot_sum + hash_sum


sum = 0
for i in data:
    print(i)
    sum += prep(i)

print(sum)
