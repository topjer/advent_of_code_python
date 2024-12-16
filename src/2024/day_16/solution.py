from utilities import load_file, load_file_single, timing_val
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

def part_01(task_input) -> int:
    result = 0
    start, goal, dimension, walls = task_input
    # print_map(start, (dimension, dimension), walls, set())
    direction = 0
    paths = []
    h.heappush(paths, (0, 0, [start]))
    seen_points = set()
    while paths:
        cost, direction, path = h.heappop(paths)
        # print("current_cost", cost)
        # print_map(path[-1], (dimension, dimension), walls, path)
        if (direction, path[-1]) in seen_points:
            continue
        else:
            seen_points.add((direction, path[-1]))
        # print(cost, direction, path)
        # print(paths)
        # check straight
        if (point_straigth:=is_valid(path[-1], DIRECTIONS[direction], walls)) is not None:
            if point_straigth == goal:
                result = cost + 1 
                break
            temp = path[:]
            temp.append(point_straigth)
            h.heappush(paths, (cost + 1, direction, temp))

        if (point_left:=is_valid(path[-1], DIRECTIONS[(direction - 1) % 4], walls)) is not None:
            if point_left == goal:
                result = cost + 1001
                break
            temp = path[:]
            temp.append(point_left)
            # print(point_left)
            h.heappush(paths, (cost + 1001, (direction - 1) % 4, temp))

        if (point_right:=is_valid(path[-1], DIRECTIONS[(direction + 1) % 4], walls)) is not None:
            if point_right == goal:
                result = cost + 1001
                break
            temp = path[:]
            temp.append(point_right)
            # print(point_right)
            h.heappush(paths, (cost + 1001, (direction + 1) % 4, temp))


        # print(paths)
    # put logic here
    return result


def part_02(task_input) -> int:
    result = 0
    # put logic here
    return result

def parse_input(task_input):
    dimension = task_input.find('\n')
    cleaned_input = task_input.replace('\n', '')
    start = divmod(cleaned_input.find('S'), dimension)
    goal = divmod(cleaned_input.find('E'), dimension)
    walls = set(divmod(match.start(), dimension) for match in re.finditer(r'#', cleaned_input))
    # print(walls)
    return start, goal, dimension, walls

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
    assert result == 7036

def test_part2():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 0
