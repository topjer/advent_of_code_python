from utilities import load_file, timing_val
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

@timing_val
def part_01(task_input: list[str]) -> int:
    result = 0
    # put logic here
    return result


@timing_val
def part_02(task_input: list[str]) -> int:
    result = 0
    # put logic here
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
    assert result == 0

def test_part2():
    content = load_file(CURRENT_FOLDER / 'tests/input')
    result = part_02(content)
    # put test result here
    assert result == 0
