from utilities import load_file, load_file_single, timing_val
from pathlib import Path
from collections import deque, defaultdict
CURRENT_FOLDER = Path(__file__).parent.resolve()

def part_01(connections) -> int:
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


def part_02(connections) -> int:
    """ Doing breadth first search seems like a bad idea because one keeps checking identical paths.
    It seems smarter to check the inverse path because:
    * we will only check relevant paths
    * we do not recheck paths. Point here is that if I get to a point A from point B or point C does not affect
      what happens after point A, so I do not have to check that path (from A) twice
    """
    result = 0
    # invert dictionary
    reverse_connections = defaultdict(list)
    for key, values in connections.items():
        for value in values:
            reverse_connections[value].append(key)
    print(reverse_connections)
    # put logic here
    # paths = deque()
    # paths.append(['fft'])
    # counter = 0
    # while paths:
    #     # if counter == 10000:
    #     #     break
    #     path = paths.popleft()
    #     print(path)
    #     targets = connections[path[-1]]
    #     if targets == ['out']:
    #         # if 'dac' in path and 'fft' in path:
    #         #     result += 1
    #         continue
    #
    #     for target in targets:
    #         paths.append([*path, target])
    #
    #     counter += 1
    #     # print(paths, "\n")

    return result

def parse_input(task_input):
    connections = dict()
    for line in task_input:
        source, targets = line.split(':')
        connections[source] = targets.split()
    # print(connections)
    return connections

@timing_val
def main():
    task_input = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input2'))
    # task_input = parse_input(load_file(CURRENT_FOLDER / 'input'))
    # 555
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
    assert result == 5

def test_part2():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input2'))
    result = part_02(content)
    # put test result here
    assert result == 2
