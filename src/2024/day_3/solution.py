from utilities import load_file, timing_val
from pathlib import Path
import re as re
CURRENT_FOLDER = Path(__file__).parent.resolve()

def extract_values(input_str: str):
    result = 0
    for m in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', input_str):
        result += int(m.group(1)) * int(m.group(2))
    return result


@timing_val
def part_01(task_input: list[str]) -> int:
    result = 0
    for line in task_input:
        result += extract_values(line) 
    # put logic here
    return result


@timing_val
def part_02(task_input: list[str]) -> int:
    task_input_new = ''.join(task_input)
    result = 0
    for m in re.split(r'do\(\)', task_input_new):
        inner_match = re.split(r"don\'t\(\)", m)
        result += extract_values(inner_match[0])
    return result

def main():
    result_part1 = part_01(load_file(CURRENT_FOLDER / 'input'))
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(load_file(CURRENT_FOLDER / 'input'))
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = load_file(CURRENT_FOLDER / 'tests/input')
    result = part_01(content)
    # put test result here
    assert result == 161

def test_part2():
    content = load_file(CURRENT_FOLDER / 'tests/input_part2')
    result = part_02(content)
    # put test result here
    assert result == 48
