import re
from typing import Dict

with open("./input.txt", "r") as f:
    temp = f.read().strip().split("\n\n")
    workflows = dict()

    pattern = r"([^{}]+)\{([^}]+)\}"
    for w in temp[0].split("\n"):
        match = re.search(pattern, w)
        if match:
            workflows[match.group(1)] = match.group(2).split(",")
        else:
            raise Exception("String didn't match with regex pattern")

    rating = []
    for rat in temp[1].split("\n"):
        part_feature = dict()
        diff_feature = rat.strip("{}").split(",")
        for df in diff_feature:
            feature, num = df.split("=")
            num_int = int(num)
            part_feature[feature] = num_int

        rating.append(part_feature)


def workflow_search(part: Dict[str, int], searching_for: str):
    accepted = False

    for condition in workflows[searching_for]:
        if ":" in condition:
            compare, result = condition.split(":")
            if ">" in compare:
                feature, feature_val = compare.split(">")
                if part[feature] > int(feature_val):
                    if result == "A":
                        accepted = True
                        break
                    elif result == "R":
                        break
                    else:
                        accepted = workflow_search(part, result)
                        break

            elif "<" in compare:
                feature, feature_val = compare.split("<")
                if part[feature] < int(feature_val):
                    if result == "A":
                        accepted = True
                        break
                    elif result == "R":
                        break
                    else:
                        accepted = workflow_search(part, result)
                        break
        else:
            if condition == "A":
                accepted = True
                break
            elif condition == "R":
                break
            else:
                accepted = workflow_search(part, condition)
                break

    return accepted


total = 0
for r in rating:
    if workflow_search(r, "in") == True:
        for key in r:
            total += r[key]

print(total)
