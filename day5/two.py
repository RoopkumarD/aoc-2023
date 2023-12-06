from typing import List

with open("./input.txt", "r") as f:
    seed_temp = [int(i) for i in f.readline().strip().split()[1:]]
    seeds = [
        [seed_temp[j], seed_temp[j] + seed_temp[j + 1]]
        for j in range(0, len(seed_temp), 2)
    ]
    mapping = dict()
    maps_value = dict()

    key = ""
    for line in f.readlines():
        if line == "\n":
            key = ""
        else:
            if key != "":
                if key not in maps_value:
                    maps_value[key] = []

                maps_value[key].append([int(i) for i in line.strip().split()])
            else:
                temp = line.strip().split()[0].split("-")
                key = temp[-1]
                mapping[temp[0]] = key


# range1 -> to compare, range2 -> against which is map
def intersect_two_range(range1, compare_against):
    range2 = [compare_against[1], compare_against[1] + compare_against[2]]

    if range1[1] < range2[0] or range2[1] < range1[0]:
        return None
    elif range2[0] <= range1[0] and range1[1] <= range2[1]:
        return {
            "new_range": [
                range1[0] - range2[0] + compare_against[0],
                range1[1] - range2[0] + compare_against[0],
            ],
            "leftover": [],
        }
    elif range1[0] < range2[0] and range2[1] < range1[1]:
        return {
            "new_range": [compare_against[0], compare_against[0] + compare_against[2]],
            "leftover": [[range1[0], range2[0]], [range2[1], range1[1]]],
        }
    elif range1[0] < range2[0] < range1[1] < range2[1]:
        return {
            "new_range": [
                compare_against[0],
                range1[1] - range2[0] + compare_against[0],
            ],
            "leftover": [[range1[0], range2[0]]],
        }
    elif range1[0] < range2[0] == range1[1] < range2[1]:
        return {
            "new_range": [compare_against[0], compare_against[0]],
            "leftover": [[range1[0], range1[1] - 1]],
        }
    elif range2[0] < range1[0] < range2[1] < range1[1]:
        return {
            "new_range": [
                range1[0] - range2[0] + compare_against[0],
                compare_against[0] + compare_against[2],
            ],
            "leftover": [[range2[1], range1[1]]],
        }
    elif range2[0] < range1[0] == range2[1] < range1[1]:
        return {
            "new_range": [
                compare_against[2] + compare_against[0],
                compare_against[2] + compare_against[0],
            ],
            "leftover": [[range1[0] + 1, range1[1]]],
        }


def split_ranges(ranged, against_ranges) -> List:
    finalised_ranges = []
    for compare_range in maps_value[against_ranges]:
        res = intersect_two_range(ranged, compare_range)
        if res != None:
            finalised_ranges.append(res["new_range"])
            for again_check in res["leftover"]:
                final = split_ranges(again_check, against_ranges)
                for i in final:
                    finalised_ranges.append(i)

            break

    if len(finalised_ranges) == 0:
        return [ranged]

    return finalised_ranges


def get_location_range(value_ranges, to_check):
    ranges = []
    for value_range in value_ranges:
        result = split_ranges(value_range, to_check)
        for i in result:
            ranges.append(i)

    if to_check == "location":
        return ranges
    else:
        return get_location_range(ranges, mapping[to_check])


s = get_location_range(seeds, mapping["seed"])
print(min(s)[0])
