from utilities import load_file, load_file_single, timing_val
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

COORDS_NUMERIC = {
    '7': (0,0),
    '8': (0,1),
    '9': (0,2),
    '4': (1,0),
    '5': (1,1),
    '6': (1,2),
    '1': (2,0),
    '2': (2,1),
    '3': (2,2),
    '0': (3,1),
    'A': (3,2),
}

COORDS_DIRECTIONAL = {
    '^': (0,1),
    'A': (0,2),
    '<': (1,0),
    'v': (1,1),
    '>': (1,2),
}

def determine_motions(start, goal):
    command = ''
    diff = (goal[0]-start[0], goal[1]-start[1])
    if diff[1] > 0:
        command += '>' * abs(diff[1])
    if diff[0] < 0:
        command += '^' * abs(diff[0])
    if diff[1] < 0:
        command += '<' * abs(diff[1])
    if diff[0] > 0:
        command += 'v' * abs(diff[0])
    command += 'A'
    return command
    # print(command)

def determine_command(command: str, start: tuple[int, int], coords):
    input_sequence = ''
    current_position = start
    for char in command:
        target_position = coords[char]
        if target_position == current_position:
            motions = 'A'
        else:
            motions = determine_motions(current_position, target_position)
        input_sequence += motions
        current_position = target_position
    return input_sequence

def part_01(task_input) -> int:
    result = 0
    print(task_input)
    # for command in task_input[4:]:
    #     initial_sequence = determine_command(command, (3,2), COORDS_NUMERIC)
    #     second_sequence = determine_command(initial_sequence, (0,2), COORDS_DIRECTIONAL)
    #     final_sequence = determine_command(second_sequence, (0,2), COORDS_DIRECTIONAL)
    #     print(initial_sequence)
    #     print(second_sequence)
    #     print(final_sequence)
    #     print(len(final_sequence))
    #     print(int(command[0:3]))
    #     result += len(final_sequence) * int(command[0:3])
    # put logic here
    return result


def part_02(task_input) -> int:
    result = 0
    # put logic here
    return result

def parse_input(task_input):
    return task_input.splitlines()

@timing_val
def main():
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    # task_input = parse_input(load_file(CURRENT_FOLDER / 'input'))
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
    assert result == 0

def test_part2():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 0
