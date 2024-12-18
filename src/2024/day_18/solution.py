from utilities import load_file, load_file_single, timing_val
from pathlib import Path
from collections import deque
CURRENT_FOLDER = Path(__file__).parent.resolve()


def is_valid(point, dimension):
    return (0 <= point[0] <= dimension[0]) and (0 <= point[1] <= dimension[1])

def find_shortest_path(
    start: tuple[int,int],
    goal: tuple[int,int],
    dimension: tuple[int, int],
    walls: set[tuple[int,int]]
):
    paths_to_check = deque()
    paths_to_check.append([start])
    seen_points = set()
    solution = None
    while paths_to_check:
        # print('hey')
        # print(paths_to_check)
        current_path = paths_to_check.popleft()
        current_point = current_path[-1]
        # this is the most important path because it leads to super fast convergence
        if current_point in seen_points:
            continue
        else:
            seen_points.add(current_point)
        # check up
        if (up:=(current_point[0], current_point[1]-1)) not in walls and is_valid(up, dimension):
            if up == goal:
                solution = current_path
                break
            if up not in current_path:
                temp = current_path[:]
                temp.append(up)
                paths_to_check.append(temp)

        if (down:=(current_point[0], current_point[1]+1)) not in walls and is_valid(down, dimension):
            if down == goal:
                solution = current_path
                break
            if down not in current_path:
                temp = current_path[:]
                temp.append(down)
                paths_to_check.append(temp)

        if (left:=(current_point[0]-1, current_point[1])) not in walls and is_valid(left, dimension):
            if left == goal:
                solution = current_path
                break
            if left not in current_path:
                temp = current_path[:]
                temp.append(left)
                paths_to_check.append(temp)

        if (right:=(current_point[0]+1, current_point[1])) not in walls and is_valid(right, dimension):
            if right == goal:
                solution = current_path
                break
            if right not in current_path:
                temp = current_path[:]
                temp.append(right)
                paths_to_check.append(temp)
    return solution


def part_01(task_input, dimension, number_bytes) -> int:
    result = 0
    # dimension = (6,6)
    position = (0,0)
    walls = set(task_input[:number_bytes])

    solution = find_shortest_path(position, dimension, walls)
    # print(current_path)
    # put logic here
    if solution is not None:
        result = len(solution)
    return result


def part_02(task_input, dimension, number_bytes) -> tuple[int, int]:
    # put logic here
    overall_index = number_bytes
    walls = set(task_input[:overall_index])
    last_point=(0,0)
    while True:
        path = find_shortest_path((0,0), dimension, walls)
        if path is None:
            break

        path_set = set(path)
        for index, point in enumerate(task_input[overall_index:]):
            walls.add(point)
            if point in path_set:
                last_point = point
                overall_index += index
                break
    return last_point[1], last_point[0]

def parse_input(task_input):
    output = []
    for line in task_input:
        a,b = line.strip().split(',')
        output.append((int(b),int(a)))
    return output

@timing_val
def main():
    print("Start")
    # task_input = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file(CURRENT_FOLDER / 'input'))
    # result_part1 = part_01(task_input, (6,6), 12)
    result_part1 = part_01(task_input, (70, 70), 1024)
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(task_input, (70,70), 1024)
    # result_part2 = part_02(task_input, (6,6), 12)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    result = part_01(content, (6,6), 12)
    # put test result here
    assert result == 22

def test_part2():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 0
