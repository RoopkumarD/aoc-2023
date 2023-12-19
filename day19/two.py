import re
from typing import Dict, Tuple

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

    ratings: Dict[str, Tuple[int, int]] = {
        "x": (1, 4000),
        "m": (1, 4000),
        "a": (1, 4000),
        "s": (1, 4000),
    }


total = 0


def split_regions(ratings: Dict[str, Tuple[int, int]], search_for: str):
    global total

    for condition in workflows[search_for]:
        if ":" in condition:
            compare, result = condition.split(":")
            if ">" in compare:
                feature, feature_val = compare.split(">")
                if int(feature_val) + 1 > ratings[feature][1]:
                    continue

                new_rating = dict(ratings)
                new_rating[feature] = (int(feature_val) + 1, ratings[feature][1])

                if result == "A":
                    t = 1
                    print(new_rating)
                    for r in new_rating:
                        t *= new_rating[r][1] - new_rating[r][0] + 1

                    total += t
                elif result == "R":
                    break
                else:
                    split_regions(new_rating, result)

                if int(feature_val) < ratings[feature][0]:
                    continue

                ratings[feature] = (ratings[feature][0], int(feature_val))

            elif "<" in compare:
                feature, feature_val = compare.split("<")
                if int(feature_val) - 1 < ratings[feature][0]:
                    continue

                new_rating = dict(ratings)
                new_rating[feature] = (ratings[feature][0], int(feature_val) - 1)

                if result == "A":
                    t = 1
                    print(new_rating)
                    for r in new_rating:
                        t *= new_rating[r][1] - new_rating[r][0] + 1

                    total += t
                elif result == "R":
                    break
                else:
                    split_regions(new_rating, result)

                if int(feature_val) > ratings[feature][1]:
                    continue

                ratings[feature] = (int(feature_val), ratings[feature][1])
        else:
            if condition == "A":
                t = 1
                print(ratings)
                for r in ratings:
                    t *= ratings[r][1] - ratings[r][0] + 1

                total += t
            elif condition == "R":
                break
            else:
                split_regions(ratings, condition)


split_regions(ratings, "in")
print(total)
