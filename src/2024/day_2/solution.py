from utilities import load_file, timing_val
import timeit
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

def levels_are_valid(levels):
    # print(levels)
    diff = levels[0] - levels[1]
    if abs(diff) > 3 or diff == 0:
        return 0

    sign = diff / abs(diff)
    for x,y in zip(levels[1:-1], levels[2:]):
        # diffs = [ x-y for x,y in zip()]
        diff = x-y
        if abs(diff) > 3 or diff == 0:
            return 0

        if sign != diff / abs(diff):
            return 0

        sign = diff / abs(diff)
    return 1

@timing_val
def part_01(task_input: list[str]) -> int:
    result = 0
    for line in task_input:
        levels = [int(number) for number in line.split()]
        result += levels_are_valid(levels)
    # put logic here
    return result


@timing_val
def part_02(task_input: list[str]) -> int:
    result = 0
    # put logic here
    
    for line in task_input:
        numbers = line.split()
        levels = [int(number) for number in numbers]
        if levels_are_valid(levels):
            result += 1
        else:
            for i in range(0, len(numbers)):
                temp_levels = levels.copy()
                del temp_levels[i]
                if levels_are_valid(temp_levels):
                    result += 1
                    break
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
    assert result == 2

def test_part2():
    content = load_file(CURRENT_FOLDER / 'tests/input')
    result = part_02(content)
    # put test result here
    assert result == 4
