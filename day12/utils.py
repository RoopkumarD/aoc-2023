from typing import List


def factorial(num: int):
    total = 1

    while num > 0:
        total = total * num
        num -= 1

    return total


def common_elements(value_list: List[str]):
    elem_dict = dict()
    for i in value_list:
        if i not in elem_dict:
            elem_dict[i] = 0

        elem_dict[i] += 1

    total = 1
    for j in elem_dict.values():
        if j > 1:
            total = total * factorial(j)

    return total


def pattern_checker(string_pattern: str, num_pattern: str) -> bool:
    num_list = [int(i) for i in num_pattern.split(",")]
    string_list = [char for char in string_pattern.split(".") if char != ""]

    if len(num_list) != len(string_list):
        return False

    length = len(num_list)
    matched_pattern = True
    for i in range(length):
        if len(string_list[i]) != num_list[i]:
            matched_pattern = False
            break

    return matched_pattern


def fuzzy_pattern_checker(string_pattern: str, possible_string: str) -> bool:
    length = len(string_pattern)

    matching_pattern = True
    for i in range(length):
        if string_pattern[i] != "?":
            if string_pattern[i] != possible_string[i]:
                matching_pattern = False
                break

    return matching_pattern


def another_fuzzy_pattern_checker(string_pattern: str, possible_string: str) -> bool:
    compare_string_pattern = string_pattern[: len(possible_string)]
    length = len(possible_string)
    matching_pattern = True

    for i in range(length):
        if compare_string_pattern[i] != "?":
            if compare_string_pattern[i] != possible_string[i]:
                matching_pattern = False
                break

    return matching_pattern


def consistency(string_list: List[str], nums: List[int]) -> bool:
    i = 0
    consistent = True

    for char in string_list:
        if char != ".":
            if len(char) != nums[i]:
                consistent = False
                break
            else:
                i += 1

    return consistent
