from utilities import load_file_single, timing_val
from collections import defaultdict
import re
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

# answer between 1570 and 1962

def print_plan(plan, visited_positions, obstacle = None):
    for line_number, line in enumerate(plan):
        for column_number, char in enumerate(line):
            if (column_number, line_number) in visited_positions:
                print('X', end='')
            else:
                if (column_number, line_number) == obstacle:
                    print('O', end='')
                else:
                    print(char, end='')
        print('')

DIRECTIONS = {
    0: (0,-1),
    1: (1,0),
    2: (0,1),
    3: (-1,0),
}

def generate_points_in_between(start, end, direction):
    if direction % 2 == 0:
        points = [(i, start[1]) for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1)]
    else:
        points = [(start[0], i) for i in range(min(start[1], end[1]), max(start[1], end[1]) + 1)]

    return points

# new DIRECTIONS
# 0 up, 1 right, 2 down, 3 left

@timing_val
def experiment(task_input):
    start, row_obstacles, column_obstacles, dimension = task_input
    # print(start)
    keep_looping = True
    direction = 0
    current_point = start
    visited_points = set()
    visited_points.add(start)
    # print(visited_points)
    while keep_looping:
        if direction % 2 == 0:
            obstacles = column_obstacles[current_point[1]]
        else:
            obstacles = row_obstacles[current_point[0]]

        if direction in (0,3):
            aggregation_function = max
        else:
            aggregation_function = min

        if direction == 0:
            comparison_function = lambda x: x < current_point[0]
        elif direction == 1:
            comparison_function = lambda x: x > current_point[1]
        elif direction == 2:
            comparison_function = lambda x: x > current_point[0]
        else:
            comparison_function = lambda x: x < current_point[1]

        obstacles = list(obs for obs in obstacles if comparison_function(obs))
        if not obstacles:
            if direction == 0:
                target_point = (0, current_point[1])
            elif direction == 1:
                target_point = (current_point[0], dimension - 2)
            elif direction == 2:
                target_point = (dimension - 2, current_point[1])
            else:
                target_point = (current_point[0], 0)
            # print(current_point, target_point)
            # print("Would leave map")
            keep_looping = False
        else:
            obstacle = aggregation_function(obstacles)

            if direction == 0:
                target_point = (obstacle + 1, current_point[1])
            elif direction == 1:
                target_point = (current_point[0], obstacle - 1)
            elif direction == 2:
                target_point = (obstacle - 1, current_point[1])
            else:
                target_point = (current_point[0], obstacle + 1)

        visited_points.update(list(generate_points_in_between(current_point, target_point, direction)))
        current_point = target_point
        # print(target_point)

        direction = (direction + 1) % 4

    print(len(visited_points))
    return len(visited_points)

@timing_val
def part_01(task_input: str) -> int:
    result = 0
    # put logic here
    dimension = task_input.find('\n')
    visited_positions = set()
    # print(dimension)
    plan = task_input.splitlines()
    start_position = task_input.replace('\n', '').find('^')
    current_y, current_x = divmod(start_position, dimension)
    visited_positions.add((current_x, current_y))
    direction = 0
    # print(current_x, current_y)
    # while True:
    for _ in range(10000):
        diff = DIRECTIONS[direction]
        next_x = current_x + diff[0]
        next_y = current_y + diff[1]
        if next_x < 0 or next_y < 0:
            break
        # print(next_x, next_y)
        try:
            next_field = plan[next_y][next_x]
        except IndexError:
            break
        if next_field in ('.', '^'):
            visited_positions.add((next_x, next_y))
            current_x, current_y = next_x, next_y
            # print(current_x, current_y)
        else:
            direction = (direction + 1) % 4
        if plan[next_y][next_x] == '\n':
            break
    # print_plan(plan, visited_positions)
    # print(visited_positions)

    return len(visited_positions)


def would_loop(direction, current_x, current_y, obstacle_x, obstacle_y, plan, visited_positions_dir, visited_positions):

    while True:
    # for _ in range(10):
        # print('here')
        diff = DIRECTIONS[direction]
        next_x = current_x + diff[0]
        next_y = current_y + diff[1]
        if (next_x, next_y, direction) in visited_positions_dir:
            # print_plan(plan, visited_positions, (obstacle_x, obstacle_y))
            # print("")
            return True
        if next_x < 0 or next_y < 0:
            return False
        # print(next_x, next_y)
        try:
            next_field = plan[next_y][next_x]
        except IndexError:
            return False

        if next_field in ('.', '^') and not (next_x == obstacle_x and obstacle_y == next_y):
            visited_positions_dir.add((next_x, next_y, direction))
            visited_positions.add((next_x, next_y))
            # print_plan(plan, visited_positions)
            current_x, current_y = next_x, next_y
        else:
            direction = (direction + 1) % 4


@timing_val
def part_02(task_input: str) -> int:
    result = 0
    # put logic here
    dimension = task_input.find('\n')
    visited_positions = set()
    visited_positions_dir = set()
    # print(dimension)
    plan = task_input.splitlines()
    start_position = task_input.replace('\n', '').find('^')
    current_y, current_x = divmod(start_position, dimension)
    direction = 0
    visited_positions_dir.add((current_x, current_y, direction))
    visited_positions.add((current_x, current_y))
    # print(current_x, current_y)
    # while True:
    for i in range(10000):
        # print(i)
        diff = DIRECTIONS[direction]
        next_x = current_x + diff[0]
        next_y = current_y + diff[1]
        if next_x < 0 or next_y < 0:
            break
        # print(next_x, next_y)
        try:
            next_field = plan[next_y][next_x]
        except IndexError:
            break
        if next_field in ('.', '^'):
            if (would_loop(direction, current_x, current_y, next_x, next_y, plan, visited_positions_dir.copy(), visited_positions.copy())
                and not (next_x, next_y) in visited_positions):
                # print("Loop found")
                result += 1
            visited_positions_dir.add((next_x, next_y, direction))
            visited_positions.add((next_x, next_y))
            current_x, current_y = next_x, next_y
        else:
            direction = (direction + 1) % 4
    # print_plan(plan, visited_positions)
    # print(visited_positions)
    return result

def parse_input(task_input: str):
    column_obstacles = defaultdict(list)
    row_obstacles = defaultdict(list)
    # print(task_input)
    dimension = task_input.find('\n') + 1
    start = divmod(task_input.find('^'), dimension)
    # print(start)
    for y,x in (divmod(match.start(), dimension) for match in re.finditer(r'#', task_input)):
        row_obstacles[y].append(x)
        column_obstacles[x].append(y)
    return start, row_obstacles, column_obstacles, dimension


def main():
    # task_input = load_file_single(CURRENT_FOLDER / 'tests/input')
    task_input = load_file_single(CURRENT_FOLDER / 'input')
    foo = parse_input(task_input)
    result_part1 = experiment(foo)
    print(f"Outcome of part 1 is: {result_part1}.")
    # 5153
    result_part1 = part_01(task_input)
    print(f"Outcome of part 1 is: {result_part1}.")
    # 1711
    # result_part2 = part_02(task_input)
    # print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = load_file_single(CURRENT_FOLDER / 'tests/input')
    result = part_01(content)
    # put test result here
    assert result == 41

def test_part2():
    content = load_file_single(CURRENT_FOLDER / 'tests/input')
    result = part_02(content)
    # put test result here
    assert result == 6
