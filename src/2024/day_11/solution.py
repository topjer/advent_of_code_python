from utilities import load_file, load_file_single, timing_val
from collections import deque, Counter
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()


NUMBER_CACHE = dict()

def process_number(number: int):
    if number in NUMBER_CACHE:
        return NUMBER_CACHE[number]

    if number == 0:
        return [1]

    number_str = str(number)
    index_number_str = int(len(number_str) / 2)
    if len(number_str) % 2 == 0:
        result = [int(number_str[:index_number_str]), int(number_str[index_number_str:])]
        NUMBER_CACHE[number] = [int(number_str[:index_number_str]), int(number_str[index_number_str:])]
        return result

    result = [number * 2024]
    NUMBER_CACHE[number] = result
    return result

def part_01(old_queue: deque) -> int:

    new_queue = deque()
    for _ in range(25):
        new_queue = deque()
        while old_queue:
            element = old_queue.popleft()
            new_queue.extend(process_number(element))

        old_queue = new_queue
        # print(new_queue)
        # print(index, len(old_queue))
    # put logic here
    # print(Counter(old_queue))
    return len(new_queue)


def part_02(task_input) -> int:
    old_counter = Counter(task_input)
    for _ in range(75):
        # print(index)
        new_counter = Counter()
        for key, value in old_counter.items():
            new_values = process_number(key)
            for new_value in new_values:
                new_counter.update({new_value: old_counter[key]})
        old_counter = new_counter
        # print(index, sum(value for _, value in old_counter.items()))
    # put logic here

    # print(old_counter)
    return sum(value for _, value in old_counter.items())

def parse_input(task_input):
    numbers = deque(int(number) for number in task_input.strip().split())
    return numbers

@timing_val
def main():
    # task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'input'))
    result_part1 = part_01(task_input.copy())
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(task_input)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_01(content)
    # put test result here
    assert result == 55312

def test_part2():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 0
