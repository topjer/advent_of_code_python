from utilities import load_file, load_file_single, timing_val
from pathlib import Path
from functools import reduce
import re

CURRENT_FOLDER = Path(__file__).parent.resolve()

def part_01(task_input) -> int:
    operations = [op for op in task_input.pop().split()]
    # print(operations)
    numbers = []
    for line in task_input:
        numbers.extend([int(num) for num in line.split()])
    # print(numbers)
    result = 0
    # put logic here
    for index, op in enumerate(operations):
        func = (lambda x, y: x + y) if op == '+' else (lambda x,y: x * y)
        result += reduce(func, numbers[index::len(operations)])
    return result


def part_02(task_input) -> int:
    """
    Saying that math is done from right to left is a red-hering since it does not matter. All operations are
    commutative.

    Base idea: parse the operations column in such a way that you now in which column it starts and where it ends.
    Then determine the numbers by taking the string in its entirety, starting by a position in a task and take the 
    string slice with a step size of the row lenght. This way, we can iterate through the rows
    """
    operations = task_input.pop()
    numbers = ''.join(task_input)
    ops_list = [(el.group().strip(), el.start(), el.end() - 1) for el in re.finditer(r'[/*/+]\s*', operations)]
    # print(ops_list)
    # print(numbers)
    line_length = numbers.find('\n') + 1
    # print("Line length:", line_length)
    result = 0
    # put logic here
    for op in ops_list:
        intermediate_result = 0 if op[0] == '+' else 1
        for position in range(op[1], op[2]):
            num = numbers[position::line_length]
            # print(num)
            if op[0] == '+':
                intermediate_result += int(num)
            else:
                intermediate_result *= int(num)
        # print(intermediate_result)
        result += intermediate_result
    return result

def parse_input(task_input):
    return task_input

@timing_val
def main():
    # task_input = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file(CURRENT_FOLDER / 'input'))
    result_part1 = part_01(task_input.copy())
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(task_input)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    result = part_01(content)
    # put test result here
    assert result == 4277556

def test_part2():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 3263827
