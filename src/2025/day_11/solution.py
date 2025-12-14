from utilities import load_file, load_file_single, timing_val
from pathlib import Path
from collections import deque, defaultdict
CURRENT_FOLDER = Path(__file__).parent.resolve()

def part_01(connections) -> int:
    """Brute-force breadth first search.

    Surprisingly works in part 1 but totally breaks down in part 2. Generic solution for part 2 also solves
    part 1. But we keep this for documentation purposes
    """
    result = 0
    # put logic here
    paths = deque()
    paths.append(['you'])
    while paths:
        path = paths.popleft()
        targets = connections[path[-1]]
        if targets == ['out']:
            result += 1
            continue

        for target in targets:
            paths.append([*path, target])

        # print(paths, "\n")
    return result

def reverse_dict(connections):
    """Reverse a dict

    Was an idea of mine, but did not follow throug.
    """
    reverse_connections = defaultdict(list)
    for key, values in connections.items():
        for value in values:
            reverse_connections[value].append(key)
    print(reverse_connections)
    return reverse_connections

PATH_CACHE = dict()

def get_number_paths(start, end, connections) -> int:
    """Get number of paths from start point to end point

    Find all points connected to start and sum up number of paths from those to end.
    If one connected point is end, then we have found a path.
    In order to properly treat paths that should not end in end, we have to check whether we encountered 'out'
    and ignore that.
    """
    if (start, end) in PATH_CACHE:
        return PATH_CACHE[(start, end)]
    connected_points = connections[start]
    number_paths = 0
    for point in connected_points:
        if point == end:
            number_paths += 1
        elif point == 'out':
            continue
        else:
            number_paths += get_number_paths(point, end, connections)

    # print(start, number_paths)
    PATH_CACHE[(start, end)] = number_paths
    
    return number_paths


def part_02(connections) -> int:
    """ Get all paths going through dac and fft

    One assumption that is bein made is that there should be no cycles, else, the whole task would make no sense.
    Thus, you either reach fft from dac or the other way around. So, our first step is to determine which case it is.

    Then we determine the number of paths from 'svr' to the first point and from the second point to 'out'. All that
    is left to do, is to multiply all paths and we are done.
    """
    result = 0
    # print(connections)
    fft_to_dac = get_number_paths('fft', 'dac', connections)
    dac_to_fft = get_number_paths('dac', 'fft', connections)

    if fft_to_dac == 0:
        start_first_stop = get_number_paths('svr', 'dac', connections)
        bridge = dac_to_fft
        second_stop_end = get_number_paths('fft', 'out', connections)
    else:
        start_first_stop = get_number_paths('svr', 'fft', connections)
        bridge = fft_to_dac
        second_stop_end = get_number_paths('dac', 'out', connections)

    return start_first_stop * bridge * second_stop_end

def parse_input(task_input):
    connections = dict()
    for line in task_input:
        source, targets = line.split(':')
        connections[source] = targets.split()
    # print(connections)
    return connections

@timing_val
def main():
    # task_input = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input2'))
    task_input = parse_input(load_file(CURRENT_FOLDER / 'input'))
    # 555
    result_part1 = get_number_paths('you', 'out', task_input)
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(task_input)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    result = part_01(content)
    # put test result here
    assert result == 5

def test_part2():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input2'))
    result = part_02(content)
    # put test result here
    assert result == 2
