from utilities import load_file, load_file_single, timing_val, grid_parser, print_map, find_shortest_path
from pathlib import Path
from collections import Counter
CURRENT_FOLDER = Path(__file__).parent.resolve()

DIFFS = [
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1),
]

def generate_diffs(max_value: int):
    points = [(x,y)  for x in range(-max_value, max_value+1) for y in range((-1) * (max_value-abs(x)), max_value-abs(x)+1) if abs(x)+abs(y) > 1]
    return points

def find_shortcut(point, index, path, diffs):
    new_points = [((point[0] + diff[0], point[1] + diff[1]), abs(diff[0])+abs(diff[1])) for diff in diffs]
    # keep all points already visited that could be reached through a shortcut faster
    shortcuts = [(index - path[point] - reach) for point, reach in new_points if (point in path) and (index - path[point] > reach)]
    return shortcuts

def find_next_point(point, walls, seen):
    for diff in DIFFS:
        new_point = (point[0]+diff[0], point[1]+diff[1])
        if (new_point not in walls) and (new_point not in seen):
            return new_point

def part_02(task_input, upper_bound: int) -> tuple[int, int]:
    """ Go through the race track and for each new point check whether you could have reached a previous point through
    a shortcut in less steps then were actually taken.

    Does this for part 1 and 2 simultaneously
    """
    start, walls, goal, _ = task_input['start'], task_input['walls'], task_input['end'], task_input['dimension']
    result2 = Counter()
    result1 = Counter()
    steps = 0
    diffs_long = generate_diffs(20)
    diffs_short = generate_diffs(2)
    seen_points = {start: 0}
    current_point = start
    while True:
        next_point = find_next_point(current_point, walls, seen_points)
        steps += 1
        shortcuts1 = find_shortcut(next_point, steps, seen_points, diffs_short)
        result1.update(shortcuts1)
        shortcuts2 = find_shortcut(next_point, steps, seen_points, diffs_long)
        result2.update(shortcuts2)
        seen_points[next_point] = steps
        current_point = next_point
        if next_point == goal:
            break

    return sum(val for key, val in result1.items() if key >= upper_bound), sum(val for key, val in result2.items() if key >= upper_bound)


def parse_input(task_input):
    # print(task_input)
    task_input = grid_parser(task_input, {'walls': '#', 'start': 'S', 'end': 'E'})
    return task_input

@timing_val
def main():
    # task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'input'))
    result_part1, result_part2 = part_02(task_input, 100)
    print(f"Outcome of part 1 is: {result_part1}.")
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result1, _ = part_02(content, 0)
    # put test result here
    assert result1 == 44

def test_part2():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    _, result2 = part_02(content, 50)
    # put test result here
    assert result2 == 285
