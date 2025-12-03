from utilities import load_file, load_file_single, timing_val
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

def part_01(inputs) -> int:
    # print(inputs)
    result = 0
    # put logic here
    for line in inputs:
        max_value = max(line[:-1])
        max_position = line.index(max_value)
        remainder = line[max_position+1:]
        second_max = max(remainder)
        result += 10 * max_value + second_max

    return result


def part_02(inputs) -> int:
    result = 0
    # inputs = inputs[0:1]
    # put logic here
    for line in inputs:
        # print(len(line))
        values = []
        start_position = 0
        for end_position in range(11,-1, -1):
            candidates = line[start_position:(-1) * end_position] if end_position != 0 else line[start_position:]
            # print(candidates)
            max_value = max(candidates)
            max_index = candidates.index(max_value)
            # print(max_index)
            start_position += max_index + 1
            values.append(str(max_value))

        result += int(''.join(values))
        # print(result)
    return result

def parse_input(task_input):
    inputs = []
    for line in task_input:
        inputs.append([int(battery) for battery in line.strip()])
    return inputs

@timing_val
def main():
    # task_input = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file(CURRENT_FOLDER / 'input'))
    result_part1 = part_01(task_input)
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(task_input)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    result = part_01(content)
    # put test result here
    assert result == 357

def test_part2():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 3121910778619
