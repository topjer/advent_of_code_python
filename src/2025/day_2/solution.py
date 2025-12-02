from utilities import load_file, load_file_single, timing_val
from pathlib import Path
import math
CURRENT_FOLDER = Path(__file__).parent.resolve()

def part_01(ranges) -> int:
    print("------------------------Start---------------------")
    result = 0
    # put logic here
    for lower, upper in ranges:
        print(lower, upper)
        positions = math.ceil(len(lower) / 2)
        print(positions)
        current_number = 1 if positions == 1 else max(int(lower[:-positions]), 10**(positions -1 ))
        lower_bound = int(lower)
        upper_bound = int(upper)
        print(current_number)
        while True:
            number_to_check = int(str(current_number) * 2)
            # print("number to check" , number_to_check)
            if lower_bound <= number_to_check <= upper_bound:
                result += number_to_check
                print("invalid", number_to_check)
            elif number_to_check > upper_bound:
                break
            current_number += 1


    return result


def part_02(ranges) -> int:
    print("------------------------Start---------------------")
    # ranges = ranges[0:2]
    result = 0
    # put logic here
    for lower, upper in ranges:
        # print(lower, upper)
        for number in range(int(lower), int(upper)+1):
            # print(number)
            string_repr = str(number)
            for i in range(1, len(string_repr)):
                sub_number = string_repr[:i]
                # print(sub_number)
                multiplier = len(string_repr) / i
                # print("multiplier", multiplier)
                if not multiplier.is_integer():
                    continue
                number_to_check = sub_number * int(multiplier)
                # print("number_to_check", number_to_check)
                if number_to_check == string_repr:
                    result += int(number_to_check)
                    # print("invalid:", number)
                    break
            # print(number)
    return result

def parse_input(task_input):
    ranges = []
    for entry in task_input.strip().split(','):
        lower, upper = entry.split('-')
        ranges.append((lower, upper))
    # print(ranges)
    return ranges

@timing_val
def main():
    # task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'input'))
    # 18700015741 
    # result_part1 = part_01(task_input)
    # print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(task_input)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_01(content)
    # put test result here
    assert result == 1227775554

def test_part2():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 4174379265
