with open("./input.txt", "r") as f:
    seeds = [int(i) for i in f.readline().strip().split()[1:]]
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


smallest_location = 1000000000000000000


def find_location(value: int, to_check: str) -> int:
    correspondent = None
    for nums in maps_value[to_check]:
        if value in range(nums[1], nums[1] + nums[2]):
            correspondent = value - nums[1] + nums[0]

    if correspondent == None:
        correspondent = value

    if to_check == "location":
        return correspondent
    else:
        return find_location(correspondent, mapping[to_check])


for seed in seeds:
    location = find_location(seed, mapping["seed"])
    if location < smallest_location:
        smallest_location = location

print(smallest_location)
