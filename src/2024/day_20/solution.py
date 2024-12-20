from utilities import load_file, load_file_single, timing_val, grid_parser, print_map, find_shortest_path
from pathlib import Path
from collections import Counter
CURRENT_FOLDER = Path(__file__).parent.resolve()


def generate_diffs(max_value: int):
    points = [(x,y)  for x in range(-max_value, max_value+1) for y in range((-1) * (max_value-abs(x)), max_value-abs(x)+1) if abs(x)+abs(y) > 1]
    # print(points)
    return points

def find_shortcut(point, index, path, diffs):
    new_points = [((point[0] + diff[0], point[1] + diff[1]), abs(diff[0])+abs(diff[1])) for diff in diffs]
    shortcuts = [(path[point] - index - reach) for point, reach in new_points if (point in path) and (path[point] > index + reach)]
    return shortcuts


def part_01(task_input) -> int:
    # 4096 too high
    result = 0
    start, walls, goal, dimension = task_input['start'], task_input['walls'], task_input['end'], task_input['dimension']
    result = Counter()
    path = find_shortest_path(start, goal, dimension, walls)
    path = {point: index for index, point in enumerate(path)}
    diffs = generate_diffs(2)
    # print_map(goal, dimension, walls, path.keys())
    # print(path)
    for point, index in path.items():
        shortcuts = find_shortcut(point, index, path, diffs)
        result.update(shortcuts)
    # put logic here
    print(result)
    return sum(val for key, val in result.items() if key >= 100)

def part_02(task_input) -> int:
    result = 0
    start, walls, goal, dimension = task_input['start'], task_input['walls'], task_input['end'], task_input['dimension']
    result = Counter()
    diffs = generate_diffs(20)
    path = find_shortest_path(start, goal, dimension, walls)
    path = {point: index for index, point in enumerate(path)}
    for point, index in path.items():
        shortcuts = find_shortcut(point, index, path, diffs)
        result.update(shortcuts)
        # break
    # put logic here
    # print(result)
    # for key, val in result.items():
    #     if key >= 50:
    #         print(key, val)
    return sum(val for key, val in result.items() if key >= 100)

def parse_input(task_input):
    # print(task_input)
    task_input = grid_parser(task_input, {'walls': '#', 'start': 'S', 'end': 'E'})
    return task_input

@timing_val
def main():
    # task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'input'))
    # result_part1 = part_01(task_input)
    # print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(task_input)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    result = part_01(content)
    # put test result here
    assert result == 0

def test_part2():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 0
