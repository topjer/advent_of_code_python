from utilities import load_file, load_file_single, timing_val
from functools import cache
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

@cache
def calculate_next_number(number: int):
    first_step = ((number * 64) ^ number) % 16777216
    second_step = ((first_step // 32) ^ first_step) % 16777216
    third_step = ((second_step * 2048) ^ second_step) % 16777216
    # first_step = prune(mix(number << 6, number))
    # if not first_step % 32 == 0:
    #     print(first_step % 32)
    # second_step = prune(mix(first_step >> 5, first_step))
    # third_step = prune(mix(second_step << 11, second_step))
    return third_step

def part_01(task_input) -> int:
    result = 0
    for number in task_input:
        current_number = number
        for _ in range(2000):
            current_number = calculate_next_number(current_number)
            # print(current_number)
        result += current_number
        # break
    # for number in range(2000):
    #     print(number, calculate_next_number(number))
    # put logic here
    return result


def part_02(task_input) -> int:
    result = 0
    # put logic here
    return result

def parse_input(task_input):
    return [int(number) for number in task_input.strip().split('\n')]

@timing_val
def main():
    # task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'input'))
    result_part1 = part_01(task_input)
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(task_input)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_01(content)
    # put test result here
    assert result == 37327623

def test_part2():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 0
