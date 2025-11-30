from utilities import load_file, load_file_single, timing_val
from pathlib import Path
import operator
CURRENT_FOLDER = Path(__file__).parent.resolve()

def iterate(initial_configuration, operations):
    remaining_operations = operations
    current_state = initial_configuration.copy()
    while remaining_operations:
        operations = remaining_operations
        remaining_operations = []
        for left_wire, right_wire, operation, target in operations:
            if (left_wire not in current_state) or (right_wire not in current_state):
                remaining_operations.append((left_wire, right_wire, operation, target))
                continue
            if operation == 'AND':
                current_state[target] = operator.and_(current_state[left_wire], current_state[right_wire]) 
            elif operation == 'OR':
                current_state[target] =  operator.or_(current_state[left_wire], current_state[right_wire]) 
            elif operation == 'XOR':
                current_state[target] = operator.xor(current_state[left_wire], current_state[right_wire])

    return current_state


def part_01(task_input) -> int:
    result = 0
    initial_configuration, operations = task_input

    current_state = iterate(initial_configuration, operations)

    results = sorted([key for key in current_state.keys() if key.startswith('z')])

    for index, value in enumerate(results):
        result += 2**index * current_state[value]

    return result


def part_02(task_input) -> int:
    result = 0
    # put logic here
    initial_configuration, operations = task_input
    x_values = sorted([key for key in initial_configuration.keys() if key.startswith('x')], reverse=True)
    x_string = "0b" + ''.join([str(initial_configuration[x_key]) for x_key in x_values])

    y_values = sorted([key for key in initial_configuration.keys() if key.startswith('y')], reverse=True)
    y_string = "0b" + ''.join([str(initial_configuration[y_key]) for y_key in y_values])
    print(x_string)
    print(y_string)
    foo = bin(int(x_string,2) + int(y_string, 2))
    print(foo)
    return result

def parse_input(task_input):
    part1, part2 = task_input.split('\n\n')
    initial_configuration = dict()
    operations = list()
    for line in part1.splitlines():
        wire, value = line.split(': ')
        initial_configuration[wire] = int(value)

    for line in part2.splitlines():
        left_wire, operator, right_wire, _, target = line.split()
        operations.append((left_wire, right_wire, operator, target))

    # print(initial_configuration)
    # print(operations)
    return initial_configuration, operations

@timing_val
def main():
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    # task_input = parse_input(load_file_single(CURRENT_FOLDER / 'input'))
    result_part1 = part_01(task_input)
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(task_input)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_01(content)
    # put test result here
    assert result == 4

def test_part2():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 0
