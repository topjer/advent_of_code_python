from types import resolve_bases
from functools import cache
from utilities import load_file, timing_val
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

@timing_val
def part_01(task_input) -> int:
    final_result = 0
    for equation in task_input:
        expected_outcome = equation[0]
        numbers = equation[1]
        numbers = list(reversed(numbers))
        # print(numbers)
        operations = len(equation[1]) - 1
        format_string = f"0{operations}b"
        for i in range(2 ** operations):
            temp_numbers = numbers[:]
            operations = format(i,format_string)
            result = temp_numbers.pop()
            # print(operations)
            for operation in operations:
                operand = temp_numbers.pop()
                if operation == '0':
                    result *= operand
                else:
                    result += operand
                # print(result)

            if result == expected_outcome:
                final_result += expected_outcome
                break

    # put logic here
    return final_result

CACHE = dict()
def base_representation(number, base, length):
    if (number, base) in CACHE:
        return CACHE[number]
    result = ['0'] * length
    remainder = number
    position = 0
    while remainder != 0:
        remainder, value = divmod(remainder, base)
        result[(-1)*position] = str(value)
        position += 1
    result = tuple(reversed(result))
    CACHE[number] = result
    return result

SOLUTION_CACHE = dict()
def compute_solution(numbers, operations, cache):
    print(numbers, operations)
    if (numbers, operations) in cache:
        print("cache hit")
        return cache[(numbers, operations)]
    if len(operations) > 1:
        result = compute_solution(numbers[:-1], operations[:-1], cache)
    else:
        result = numbers[0]

    operand = numbers[-1]
    operation = operations[-1]

    if operation == '0':
        result *= operand
    elif operation == '1':
        result += operand
    else:
        result = int(str(result) + str(operand))

    cache[(numbers, operations)] = result
    return result

@timing_val
def part(task_input, base) -> int:
    final_result = 0
    for equation in task_input[:5]:
        expected_outcome = equation[0]
        numbers = tuple(equation[1])
        # print(expected_outcome, numbers)
        number_operations = len(equation[1]) - 1
        task_cache = dict()
        for i in range(base ** number_operations):
            temp_numbers = numbers[:]
            operations = base_representation(i, base, number_operations)
            result = compute_solution(temp_numbers, operations, task_cache)

            # print(temp_numbers, operations)
            # operations = list(format(i,format_string))
            # result = temp_numbers.pop(0)
            # for operand in temp_numbers:
            #     if operations:
            #         operation = operations.pop()
            #     else:
            #         operation = '0'
            #
            #     if operation == '0':
            #         result *= operand
            #     elif operation == '1':
            #         result += operand
            #     else:
            #         result = int(str(operand) + str(result))
                # print(temp_numbers, result)
            # print(expected_outcome, result)
            if result == expected_outcome:
                final_result += expected_outcome
                print(expected_outcome, numbers)
                break

    # put logic here
    return final_result

@timing_val
def experiment(task_input, allow_concatenation: bool):
    final_result = 0
    for equation in task_input:
        expected_outcome = equation[0]
        numbers = tuple(equation[1][::-1])
        # print(expected_outcome, numbers)
        # number_operations = len(equation[1]) - 1
        # task_cache = dict()
        check = set()
        check.add((numbers[-1], numbers[:-1]))
        while check:
            # print(check)
            current_result, numbers = check.pop()
            next_number = numbers[-1]
            remaining_numbers = numbers[:-1]

            addition = current_result + next_number
            multiplication = current_result * next_number
            concatenation = int(str(current_result) + str(next_number))

            if addition == expected_outcome:
                final_result += expected_outcome
                # print("Possible")
                break

            if multiplication == expected_outcome:
                final_result += expected_outcome
                # print("Possible")
                break

            if ( concatenation == expected_outcome ) and allow_concatenation:
                final_result += expected_outcome
                # print("Possible")
                break

            if not remaining_numbers:
                continue

            if addition < expected_outcome:
                check.add((addition, remaining_numbers))

            if multiplication < expected_outcome:
                check.add((multiplication, remaining_numbers))

            if ( concatenation < expected_outcome ) and allow_concatenation:
                check.add((concatenation, remaining_numbers))

    return final_result

def parse_input(task_input):
    result = []
    for line in task_input:
        parts = line.strip().split(': ')
        outcome = int(parts[0])
        numbers = [int(number) for number in parts[1].split()]
        result.append((outcome, numbers))
    return result

def main():
    print("execution start")
    # task_input = parse_input(load_file(CURRENT_FOLDER / 'tests/input'))
    task_input = parse_input(load_file(CURRENT_FOLDER / 'input'))
    # result_part1 = part(task_input,2)
    # result_part1 = part_01(task_input)
    result_part1 = experiment(task_input, False)
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = experiment(task_input, True)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()


def test_part1():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/input'))
    result = experiment(content, False)
    # put test result here
    assert result == 3749

def test_part2():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/input'))
    result = experiment(content, True)
    # put test result here
    assert result == 11387
