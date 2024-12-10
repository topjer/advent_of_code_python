from utilities import load_file, load_file_single, timing_val
from collections import Counter
import re
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

def is_valid_point(point, dimension):
    return (0 <= point[0] < dimension) and (0 <= point[1] < dimension)

def find_valid_points(topo, point, goal, dimension):
    valid_points = []
    up = (point[0] - 1, point[1])
    down = (point[0] + 1, point[1])
    left = (point[0], point[1] - 1)
    right = (point[0], point[1] + 1)
    # print(up, down, left, right)
    if is_valid_point(up, dimension) and topo[up[0]][up[1]] == goal:
        valid_points.append(up)

    if is_valid_point(down, dimension) and topo[down[0]][down[1]] == goal:
        valid_points.append(down)

    if is_valid_point(left, dimension) and topo[left[0]][left[1]] == goal:
        valid_points.append(left)

    if is_valid_point(right, dimension) and topo[right[0]][right[1]] == goal:
        valid_points.append(right)

    return valid_points

def part_01(task_input) -> int:
    result = 0
    topo, starting_points, dimension = task_input
    # print(topo)
    visited_points = dict()
    for start in starting_points:
        paths_to_check = [ [start] ]
        reached_points = set()
        while paths_to_check:
            next_path = paths_to_check.pop()
            if len(next_path) == 10:
                goal = next_path.pop()
                reached_points.add(goal)
                while next_path:
                    if next_path[-1] in visited_points:
                        visited_points[next_path.pop()].append(goal)
                    else:
                        visited_points[next_path.pop()] = [ goal ]
                # print(visited_points)
                continue
            last_step = next_path[-1]
            valid_points = find_valid_points(topo, last_step, len(next_path), dimension)
            # print(valid_points)
            for point in valid_points:
                if point in reached_points:
                    continue
                temp_path = next_path[:]
                temp_path.append(point)
                paths_to_check.append(temp_path)

        # print(len(reached_points))
        result += len(reached_points)
        # break

    # put logic here
    return result


def part_02(task_input) -> int:
    result = 0
    topo, starting_points, dimension = task_input
    # print(topo)
    possible_paths = Counter()
    for start in starting_points:
        paths_to_check = [ [start] ]
        # reachable_points = list()
        while paths_to_check:
            next_path = paths_to_check.pop()
            if len(next_path) == 10:
                possible_paths.update(next_path)
                # reachable_points.append(next_path.pop())
                continue
            last_step = next_path[-1]
            valid_points = find_valid_points(topo, last_step, len(next_path), dimension)
            # print(valid_points)
            for point in valid_points:
                if point in possible_paths:
                    possible_paths.update({path_point: possible_paths[point] for path_point in next_path})
                    continue
                temp_path = next_path[:]
                temp_path.append(point)
                paths_to_check.append(temp_path)
            # print(paths_to_check)
        # print(possible_paths)
        # print(len(reachable_points))
        result += possible_paths[start]
        # break

    # put logic here
    return result

def parse_input(task_input):
    # print(task_input)
    topo = [list(int(number) for number in line) for line in task_input.split('\n') if line]
    # must be length of a line
    dimension = len(topo)
    starting_points = list(map(lambda x: divmod(x.start(), dimension + 1), re.finditer(r'0', task_input)))
    # print(starting_points)
    # print(topo)
    return topo, starting_points, dimension

@timing_val
def main():
    print("Start Execution")
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
    assert result == 36

def test_part2():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 81
