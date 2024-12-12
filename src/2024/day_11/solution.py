from utilities import load_file, load_file_single, timing_val
from functools import cache
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

@cache
def process_number(number: int, depth: int):
    if depth == 0:
        return 1

    if number == 0:
        return process_number(1, depth - 1)

    number_str = str(number)
    index_number_str = int(len(number_str) / 2)

    if len(number_str) % 2 == 0:
        return process_number(int(number_str[:index_number_str]), depth - 1 ) + process_number(int(number_str[index_number_str:]), depth - 1)

    return process_number(number * 2024, depth - 1)

def solution(task_input) -> tuple[int, int]:
    return sum(process_number(number, 75) for number in task_input), sum(process_number(number, 25) for number in task_input)

def parse_input(task_input):
    numbers = list(int(number) for number in task_input.strip().split())
    return numbers

@timing_val
def main():
    # task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'input'))
    result_part2, result_part1 = solution(task_input)
    print(f"Outcome of part 1 is: {result_part1}.")
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result2, result1 = solution(content)
    # put test result here
    assert result1 == 55312

