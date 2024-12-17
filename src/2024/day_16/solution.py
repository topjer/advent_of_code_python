from utilities import load_file, load_file_single, timing_val, grid_parser
import heapq as h
from pathlib import Path
import re
CURRENT_FOLDER = Path(__file__).parent.resolve()

def print_map(current_position, dimension: tuple[int, int], walls, boxes):
    for row in range(dimension[0]):
        for col in range(dimension[1]):
            if (row, col) in walls:
                print("#", end="")
            elif (row, col) == current_position:
                print('@', end='')
            elif (row, col) in boxes:
                print('O', end='')
            else:
                print('.', end='')
        print("")
    print("")

DIRECTIONS = {
    0: (0, 1),
    1: (-1, 0),
    2: (0, -1),
    3: (1, 0)
}

def is_valid(point, diff, walls):
    new_point = (point[0] + diff[0], point[1] + diff[1])
    if new_point in walls:
        return None
    else:
        return new_point

def part_01(task_input) -> tuple[int, int]:
    result = 0
    start, goal, dimension, walls = task_input
    # print_map(start, (dimension, dimension), walls, set())
    max_cost = 1000000
    direction = 0
    paths = []
    h.heappush(paths, (0, 0, [start]))
    viable_paths = set()
    seen_points = dict()
    while paths[0][0] <= max_cost:
        cost, direction, path = h.heappop(paths)
        # potential optimization: not necessary to allow all paths, only required to know the additional
        # points that added to this path
        if (direction, path[-1]) in seen_points:
            if seen_points[(direction, path[-1])] < cost:
                continue
        else:
            seen_points[(direction, path[-1])] = cost
        # check straight
        if (point_straigth:=is_valid(path[-1], DIRECTIONS[direction], walls)) is not None:
            temp = path[:]
            temp.append(point_straigth)
            if point_straigth == goal:
                result = cost + 1 
                max_cost = result
                viable_paths = viable_paths.union(set(temp))
                continue
            h.heappush(paths, (cost + 1, direction, temp))

        if (point_left:=is_valid(path[-1], DIRECTIONS[(direction - 1) % 4], walls)) is not None:
            temp = path[:]
            temp.append(point_left)
            if point_left == goal:
                result = cost + 1001
                max_cost = result
                viable_paths = viable_paths.union(set(temp))
                continue
            h.heappush(paths, (cost + 1001, (direction - 1) % 4, temp))

        if (point_right:=is_valid(path[-1], DIRECTIONS[(direction + 1) % 4], walls)) is not None:
            temp = path[:]
            temp.append(point_right)
            if point_right == goal:
                result = cost + 1001
                max_cost = result
                viable_paths = viable_paths.union(set(temp))
                continue
            h.heappush(paths, (cost + 1001, (direction + 1) % 4, temp))

    return result, len(viable_paths)


def part_02(task_input) -> int:
    result = 0
    # put logic here
    return result


def parse_input(task_input):
    foo = grid_parser(task_input, {'start': 'S', 'end': 'E', 'walls': '#'})
    # print(walls)
    return foo['start'], foo['end'], foo['dimension'], foo['walls']

@timing_val
def main():
    # task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'input'))
    result_part1, result_part2 = part_01(task_input)
    print(f"Outcome of part 1 is: {result_part1}.")
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_01(content)
    # put test result here
    assert result == 7036

def test_part2():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 0
