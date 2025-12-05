from utilities import load_file, load_file_single, timing_val
from pathlib import Path
import math
CURRENT_FOLDER = Path(__file__).parent.resolve()

def part_01(ranges) -> int:
    """
    Idea is here that we do not have to check all numbers but only the numbers starting by the "first half" of the digits
    of the lower bound until we exceed the upper bound.

    For example:
    1234 - 1567
    first half is 12, so we check 1212, 1313, 1414, 1515, 1616 and now the upper bound is exceeded.

    if the lower bound has an odd number of digits, we take the "smaller" half

    """
    result = 0
    # put logic here
    for lower, upper in ranges:
        # print(lower, upper)
        positions = math.ceil(len(lower) / 2)
        # print(positions)
        current_number = 1 if positions == 1 else max(int(lower[:-positions]), 10**(positions -1 ))
        lower_bound = int(lower)
        upper_bound = int(upper)
        # print(current_number)
        while True:
            number_to_check = int(str(current_number) * 2)
            # print("number to check" , number_to_check)
            if lower_bound <= number_to_check <= upper_bound:
                result += number_to_check
                # print("invalid", number_to_check)
            elif number_to_check > upper_bound:
                break
            current_number += 1


    return result


def part_02(ranges) -> int:
    """
    Idea is the following: We want to iterate through the possible lenghts of building blocks for invalid invalid_ids

    For example: length one would be an ID like 111111
    length two would be 12121212
    length three would be 123123123 etc.
    We only have to look for those lenghts until half of the lenght of the upper bound (because we want to have at least
    one repition, i.e. 2 times one building block)

    Then we check whether this number divides the length of the lower or upper bound. If it is the case for neither, Then
    we do not expect to construct a solution from that. Here is the implicit assumption that len(upper) - len(lower) == 1

    For example, if we look at 100 - 200, then I will not find an ID in it from a building block of length two, because the
    smallest such id would be of lenght 2 * 2 = 4

    For each number, we determine the smallest possible building block. If lower bound is divisible by number, then the 
    smallest building block are the first number digits of lower, e.g. 123456 for a lenght of 3 the building block would
    be 123.
    If lower is not divisible, then we use the smallest integer with number digits, which is 10 to the power of number - 1

    Next we determine how often we want to repeat the building block. We need at least 2 repetitions or else it is linked
    how of number fits into the length of lower.

    Then iteration looks like this: assuming we have our starting point and our multiplier, we check the number that
    consists of `multiplier` copies of `starting point` and check whether that is in range between lower and upper, if yes
    we found an invalid id and we continue by increasing our starting point by one.

    Once we have exceed the upper limit, we can stop the iteration.

    Whenever the starting point exceeds 10 to the power of number - 1 we reset it to the smallest possible number and 
    instead increase the multiplier by one.

    for example: 997 - 1004
    when we want to check for blocks of length 1, we will start with '9' and multiply by 3. The next step would not be to 
    take '10' and multiply by 3 but instead take 1 and multiply by 4
    """
    result = 0
    # put logic here
    for lower, upper in ranges:
        lower_len = len(lower)
        upper_len = len(upper)
        invalid_ids = set()
        for number in range(1, math.ceil(upper_len / 2) + 1):
            # print(f"Number is: {number}")
            lower_multiplier = lower_len / number
            upper_multiplier = upper_len / number
            if not lower_multiplier.is_integer() and not upper_multiplier.is_integer():
                # print(f"skipped: {number}")
                continue

            start_number = lower[0:number] if lower_multiplier.is_integer() else 10 ** (number - 1)
            current_seed = int(start_number)
            current_multiplier = max(2, math.ceil(lower_multiplier))
            # print(start_number, current_multiplier)
            while True:
                # print(current_seed, current_multiplier)
                if current_multiplier == 1:
                    break
                number_to_check =  int(str(current_seed) * current_multiplier)
                # print(number_to_check)
                if number_to_check > int(upper):
                    break
                elif number_to_check >= int(lower) and (number_to_check not in invalid_ids):
                    result += number_to_check
                    invalid_ids.add(number_to_check)
                    # print(f"Invalid number found: {number_to_check}")

                current_seed += 1
                if current_seed >= 10 ** number:
                    current_multiplier += 1
                    current_seed = 10 ** (number - 1)

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
    result_part1 = part_01(task_input)
    print(f"Outcome of part 1 is: {result_part1}.")
    # 20077272987
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
