from utilities import load_file, load_file_single, timing_val
from functools import cache
from pathlib import Path
from collections import Counter
CURRENT_FOLDER = Path(__file__).parent.resolve()

@cache
def calculate_next_number(number: int):
    first_step = ((number << 6) ^ number) & 16777215
    second_step = ((first_step >> 5) ^ first_step) & 16777215
    third_step = ((second_step << 11) ^ second_step) & 16777215
    return third_step

def part_01(task_input):
    """ For each input, get the 2000 prices, compute price changes and for each tuple of 4 consecutive changes
    store the number of bananas to buy (only remember first occurence)

    Update global counter that stores the results over all buyers
    """
    result = 0
    number_prices = 2000
    banana_counter = Counter()
    for number in task_input:
        current_number = number
        prices = [number % 10]
        for _ in range(number_prices):
            current_number = calculate_next_number(current_number)
            prices.append(current_number % 10)
        diffs = [prices[i+1]-prices[i] for i in range(number_prices)]
        four_consecutive = [tuple(diffs[i:i+4]) for i in range(len(diffs)-4)]
        update_dict = {}
        for key, value in zip(four_consecutive, prices[4:]):
            # print(key, value)
            if key in update_dict:
                continue
            update_dict[key] = value
        banana_counter.update(update_dict)
        result += current_number
    return result, banana_counter.most_common(1)[0][1]

def parse_input(task_input):
    return [int(number) for number in task_input.strip().split('\n')]

@timing_val
def main():
    print("Start")
    # task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'input'))
    result_part1, result_part2 = part_01(task_input)
    print(f"Outcome of part 1 is: {result_part1}.")
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result,_ = part_01(content)
    # put test result here
    assert result == 37327623

def test_part2():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input2'))
    _, result = part_01(content)
    # put test result here
    assert result == 23
