from utilities import load_file, load_file_single, timing_val
from pathlib import Path
import re
from collections import defaultdict

CURRENT_FOLDER = Path(__file__).parent.resolve()

def part_01(task_input) -> int:
    result = 0
    # put logic here
    start_position, splitters = task_input
    beams = {start_position}
    for line in splitters:
        # print("incoming: ", beams)
        # print("splitter: ", line)
        activated_splitter = beams.intersection(line)
        result += len(activated_splitter)
        new_beams = set()
        for splitter in activated_splitter:
            new_beams.add(splitter + 1)
            new_beams.add(splitter - 1)

        new_beams = new_beams.union(beams - line)
        beams = new_beams

    return result


def part_02(task_input) -> int:
    result = 0
    # put logic here
    start_position, splitters = task_input
    beams = defaultdict(int)
    beams[start_position] += 1
    for line in splitters:
        # print("incoming: ", beams)
        # print("splitter: ", line)
        activated_splitter = set(beams.keys()).intersection(line)
        continuous_beams = set(beams.keys()) - line
        new_beams = defaultdict(int)
        for splitter in activated_splitter:
            new_beams[splitter + 1] += beams[splitter]
            new_beams[splitter - 1] += beams[splitter]
    
        for element in continuous_beams:
            new_beams[element] += beams[element]

        beams = new_beams
    
    for beam, value in beams.items():
        result += value


    return result

def parse_input(task_input):
    first_line = task_input.pop(0)
    start_position = first_line.find('S')
    splitters = list()
    for line in task_input:
        splitter = list(re.finditer(r'\^', line))
        if splitter:
            splitters.append({split.start() for split in splitter})

    # print(splitters)
    return start_position, splitters

@timing_val
def main():
    # task_input = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file(CURRENT_FOLDER / 'input'))
    # 1651
    result_part1 = part_01(task_input)
    print(f"Outcome of part 1 is: {result_part1}.")
    # 108924003331749
    result_part2 = part_02(task_input)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    result = part_01(content)
    # put test result here
    assert result == 21

def test_part2():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 40
