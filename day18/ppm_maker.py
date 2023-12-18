import array
from typing import Dict, List, Tuple

from utils import generate_random_rgb


def create_ppm(grid: List[List[int]], name: str):
    width = len(grid[0])
    height = len(grid)
    maxval = 255
    ppm_header = f"P6 {width} {height} {maxval}\n"

    image = array.array("B", [0, 0, 255] * width * height)

    colors = dict()

    for y in range(height):
        for x in range(width):
            index = 3 * (y * width + x)

            if grid[y][x] not in colors:
                color_numed = generate_random_rgb()
                while color_numed in colors.values():
                    color_numed = generate_random_rgb()
                colors[grid[y][x]] = color_numed

            r, g, b = colors[grid[y][x]]
            image[index] = r
            image[index + 1] = g
            image[index + 2] = b

    for key in colors:
        r, g, b = colors[key]
        print(f"\033[38;2;{r};{g};{b}m{key}\033[0m", end=" ")
    print()

    with open(f"./{name}.ppm", "wb") as f:
        f.write(bytearray(ppm_header, "ascii"))
        image.tofile(f)

    return
