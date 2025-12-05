from utilities import load_file, load_file_single, timing_val
from pathlib import Path
from utilities import grid_parser, print_map
import re

CURRENT_FOLDER = Path(__file__).parent.resolve()

def part_01(task_input) -> int:
    result = 0
    # put logic here
    for x, y in task_input["walls"]:
        possible_points = {(x + 1, y), (x - 1, y), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1), (x - 1, y - 1),
                           (x, y + 1), (x, y - 1)}
        neighbors = possible_points.intersection(task_input["walls"])
        if len(neighbors) < 4:
            result += 1
    return result


def part_02(task_input) -> int:
    result = 0
    # put logic here
    walls = task_input["walls"]
    # print_map((0,0), task_input["dimension"], walls, {})
    while True:
        points_to_remove = set()
        for x, y in walls:
            possible_points = {(x + 1, y), (x - 1, y), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1), (x - 1, y - 1),
                               (x, y + 1), (x, y - 1)}
            neighbors = possible_points.intersection(walls)
            if len(neighbors) < 4:
                points_to_remove.add((x,y))
                result += 1
        if len(points_to_remove) == 0:
            break
        walls = walls - points_to_remove
        # print_map((0,0), task_input["dimension"], walls, {})
    return result

def parse_input(task_input):
    grid = grid_parser(task_input, {"walls": "@"})
    # print_map((0,0), grid["dimension"], grid["walls"], {})
    return grid

@timing_val
def main():
    # task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'input'))
    result_part1 = part_01(task_input)
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(task_input)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_01(content)
    # put test result here
    assert result == 13

def test_part2():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 43
