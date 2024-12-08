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
        cache_hit = cache[(numbers, operations)]
        print(cache_hit)
        return cache_hit
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
    print(result)
    return result

@timing_val
def part(task_input, base) -> int:
    final_result = 0
    for equation in task_input[78:79]:
        expected_outcome = equation[0]
        numbers = tuple(equation[1])
        print(expected_outcome, numbers)
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
                print(operations)
                break

    # put logic here
    return final_result

@timing_val
def unoptimized_solution(task_input, allow_concatenation: bool):
    # the best I could come up with
    final_result = 0
    for equation in task_input:
        expected_outcome = equation[0]
        numbers = equation[1][::-1]
        check = []
        check.append([numbers[-1], numbers[:-1]])
        while check:
            current_result, numbers = check.pop()
            next_number = numbers[-1]
            remaining_numbers = numbers[:-1]

            addition = current_result + next_number
            multiplication = current_result * next_number
            concatenation = int(str(current_result) + str(next_number))

            if len(remaining_numbers) == 0:
                if (addition == expected_outcome):
                    final_result += expected_outcome
                    print(expected_outcome)
                    break

                if (multiplication == expected_outcome):
                    final_result += expected_outcome
                    print(expected_outcome)
                    break

                if ( concatenation == expected_outcome ) and allow_concatenation:
                    final_result += expected_outcome
                    print(expected_outcome)
                    break
            else:
                if addition <= expected_outcome:
                    check.append((addition, remaining_numbers))

                if multiplication <= expected_outcome:
                    check.append((multiplication, remaining_numbers))

                if ( concatenation <= expected_outcome ) and allow_concatenation:
                    check.append((concatenation, remaining_numbers))

    return final_result

def solver(total, numbers, concat=False):
    # inspired by https://github.com/hortonhearsadan/aoc-2024/blob/3ba4f981e2239e8df09680ed2e96b5bc6712202a/aoc_2024/day7.py
    if total < 0:
        return False
    if total == 0 and numbers == []:
        return True
    if total != 0 and numbers == []:
        return False

    last_number = numbers.pop()

    d,r = divmod(total, last_number)
    if r == 0:
        if solver(d, numbers[:], concat):
            return True

    if concat:
        s_total = str(total)
        s_last_number = str(last_number)
        if len(s_total) > len(s_last_number) and s_total[-len(s_last_number):] == s_last_number:
            if solver(int(s_total[:-len(s_last_number)]), numbers[:], concat):
                return True

    return solver(total-last_number, numbers[:], concat)

@timing_val
def solution(task_input, concat):
    final_result = 0
    for equation in task_input:
        expected_outcome = equation[0]
        numbers = equation[1]
        if solver(expected_outcome, numbers[:], concat):
            final_result += expected_outcome

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
    # task_input = parse_input(load_file(CURRENT_FOLDER / 'tests/input'))
    task_input = parse_input(load_file(CURRENT_FOLDER / 'input'))
    result_part1 = solution(task_input, False)
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = solution(task_input, True)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()


def test_part1():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/input'))
    result = solution(content, False)
    # put test result here
    assert result == 3749

def test_part2():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/input'))
    result = solution(content, True)
    # put test result here
    assert result == 11387
