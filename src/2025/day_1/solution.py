from utilities import load_file, load_file_single, timing_val
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

def part_01(task_input) -> int:
    current_position = 50
    result = 0
    for number in task_input:
        current_position += number
        if current_position % 100 == 0:
            result += 1
    # put logic here
    return result


def part_02(task_input) -> int:
    current_position = 50
    result = 0
    for number in task_input:
        result += abs(number) // 100
        increment = int(number / abs(number) * (abs(number) % 100))
        print(current_position, number, result, increment)
        if current_position != 0:
            if increment > 0 and increment + current_position >= 100:
                result += 1
                # print("foo")
            if increment < 0 and current_position + increment <= 0:
                result += 1
                # print("bar")
        current_position = (current_position + increment) % 100
    # put logic here
    return result

def parse_input(task_input):
    numbers=[]
    for line in task_input:
        sign = 1 if line.startswith('R') else -1
        number = int(line[1:])
        numbers.append(sign*number)
    return numbers

@timing_val
def main():
    #task_input = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file(CURRENT_FOLDER / 'input'))
    result_part1 = part_01(task_input)
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(task_input)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    result = part_01(content)
    # put test result here
    assert result == 3

def test_part2():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 6
