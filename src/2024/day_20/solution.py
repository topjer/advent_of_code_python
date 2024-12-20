from utilities import load_file, load_file_single, timing_val, grid_parser
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

DIFFS = [
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1),
]

def generate_diffs(max_value: int):
    """ Generate all diff vectors of manhatten length less `max_value`

    Result is a list of points and their manhatten length
    """
    points = [((x,y), reach)  for x in range(-max_value, max_value+1) for y in range((-1) * (max_value-abs(x)), max_value-abs(x)+1) if (reach:=abs(x)+abs(y)) > 1]
    return points

def number_shortcuts(point, index, path, diffs, min_dist):
    """ Get the numbers of shortcuts that could get you to `point` quicker then trough the path.
    
    Only count shortcuts that give you a minimum improvement of `min_dist`.
    Note: We check here which shortcuts would lead to the point in question and not from the point.

    This function went through quiet a lot of runtime optimization which did not help readability
    """
    new_points = sum(1 for diff, reach in diffs if (new_point:=(point[0] + diff[0], point[1] + diff[1])) in path
                  and index - path[new_point] - reach >= min_dist)
    return new_points

def find_next_point(point, potential_direction, walls, seen):
    follow_direction = (point[0]+potential_direction[0], point[1]+potential_direction[1])
    if (follow_direction not in walls) and (follow_direction not in seen):
        return follow_direction, potential_direction
    else:
        for diff in DIFFS:
            if diff == potential_direction:
                continue
            new_point = (point[0]+diff[0], point[1]+diff[1])
            if (new_point not in walls) and (new_point not in seen):
                return new_point, diff

def part_02(task_input, upper_bound: int) -> tuple[int, int]:
    """ Go through the race track and for each new point check whether you could have reached a previous point through
    a shortcut in less steps then were actually taken.

    Does this for part 1 and 2 simultaneously
    """
    start, walls, goal, _ = task_input['start'], task_input['walls'], task_input['end'], task_input['dimension']
    result2 = 0
    result1 = 0
    steps = 0
    diffs_long = generate_diffs(20)
    diffs_short = generate_diffs(2)
    seen_points = {start: 0}
    current_point = start
    current_direction = DIFFS[0]
    while True:
        next_point, current_direction = find_next_point(current_point, current_direction, walls, seen_points)
        steps += 1
        result1 += number_shortcuts(next_point, steps, seen_points, diffs_short, upper_bound)
        result2 += number_shortcuts(next_point, steps, seen_points, diffs_long, upper_bound)
        seen_points[next_point] = steps
        current_point = next_point
        if next_point == goal:
            break

    return result1, result2


def parse_input(task_input):
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
