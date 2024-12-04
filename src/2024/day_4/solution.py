from utilities import load_file, timing_val
from pathlib import Path
import re
CURRENT_FOLDER = Path(__file__).parent.resolve()

@timing_val
def part_01(task_input: list[str]) -> int:
    result = 0
    dimension = len(task_input[0])
    input_string = ''.join(task_input)
    # input_string = ''.join(line.strip() for line in task_input)
    all_positions = re.finditer(r'X', input_string)
    for m in all_positions:
        start_index = m.start(0)
        # print(f"start index {start_index}")
        substrings = [
            input_string[start_index:start_index+4], # horizontal
            input_string[start_index:start_index-4:-1], # horizontal_backwards
            input_string[start_index:start_index + 3*dimension+1:dimension], # vertical
            input_string[start_index:start_index - 3*dimension-1:-dimension], # vertical backwards
            input_string[start_index:start_index + 3*(dimension+1)+1:dimension+1], # diagonal_down_right
            input_string[start_index:start_index + 3*(dimension-1)+1:dimension-1], # diagonal down left
            input_string[start_index:start_index - 3*(dimension+1)-1:-dimension-1], # diagonal up left
            input_string[start_index:start_index - 3*(dimension-1)-1:-dimension+1], # diagonal up right
        ]
        result += sum([sstring == 'XMAS' for sstring in substrings])
    #     print(substrings)
    #
    # print(''.join(task_input))
    return result

@timing_val
def part_02(task_input: list[str]) -> int:
    result = 0
    # put logic here
    dimension = len(task_input[0])
    input_string = ''.join(task_input)
    # input_string = ''.join(line.strip() for line in task_input)
    all_positions = re.finditer(r'A', input_string)
    for m in all_positions:
        start_index = m.start(0)
        # print(f"Start index {start_index}")
        diagonal_one = input_string[start_index - dimension - 1:start_index + dimension + 2:dimension+1]
        diagonal_two = input_string[start_index - dimension + 1:start_index + dimension: dimension-1]
        if (diagonal_one == 'SAM' or diagonal_one == 'MAS') and (diagonal_two == 'SAM' or diagonal_two == 'MAS'):
            result += 1
    #     print(diagonal_two)
    # print(''.join(task_input))
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
    assert result == 18

def test_part2():
    content = load_file(CURRENT_FOLDER / 'tests/input')
    result = part_02(content)
    # put test result here
    assert result == 0
