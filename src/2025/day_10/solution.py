from utilities import load_file, load_file_single, timing_val
from pathlib import Path
from collections import deque, Counter
import re

CURRENT_FOLDER = Path(__file__).parent.resolve()

def part_01(machines) -> int:
    """ It should be sufficient to press every button only once, because pressing any button even number of times
    will just cancel out.
    """
    result = 0
    print("----- start part 1 -----")
    # put logic here
    for target_position, button_numbers, joltage  in machines:
        # print(target_position, button_numbers, joltage)
        combinations = deque()
        combinations.append([0]*len(button_numbers))
        # print(combinations)
        while combinations:
            combination = combinations.popleft()
            # print(combination)
            check = Counter()
            buttons_to_press = [entry for flag, entry in zip(combination, button_numbers) if flag == 1]
            for button in buttons_to_press:
                check.update(button)

            # check for solution
            state = {index for index, value in check.items() if value % 2 == 1}
            if target_position == state:
                # print(combination, sum(combination))
                result += sum(combination)
                break
            else:
                for position in range(len(button_numbers)):
                    if combination[position] == 1:
                        continue
                    else:
                        new_combination = combination[:]
                        new_combination[position] = 1
                        if new_combination not in combinations:
                            combinations.append(new_combination)
            # print(check, state)
            # print(combinations)
        # print(button_numbers)
        
    return result


def part_02(task_input) -> int:
    result = 0
    # put logic here
    for _, button_numbers, joltage in task_input:
        print(button_numbers, joltage)
        known_positions = set()
        position_to_check = deque()
        position_to_check.append((0, joltage))
        while position_to_check:
            partial_result = 0
            number_presses, state = position_to_check.popleft()
            for button in button_numbers:
                new_position = state.copy()
                for position in button:
                    new_position[position] += -1

                print(number_presses, new_position)
                if any(position == -1 for position in new_position):
                    continue

                if all(position == 0 for position in new_position):
                    partial_result = number_presses + 1
                    break

                if tuple(new_position) not in known_positions:
                    position_to_check.append((number_presses + 1, new_position))
                    known_positions.add(tuple(new_position))
            if partial_result > 0:
                result += partial_result
                break
    return result

def parse_input(task_input):
    machines = []
    for line in task_input:
        # print(line)
        split_line = line.split()
        target_position = split_line.pop(0)[1:-1]
        target_positions = {match.start() for match in re.finditer(r"#", target_position)}
        # target_positions = [0 if char == '.' else 1 for char in split_line.pop(0)[1:-1]]
        joltage = [int(number) for number in split_line.pop(-1)[1:-1].split(',')]
        button_numbers = [{int(number) for number in button[1:-1].split(',')} for button in split_line ]
        machines.append((target_positions, button_numbers, joltage))
    # print(machines)
    return machines

@timing_val
def main():
    # task_input = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file(CURRENT_FOLDER / 'input'))
    # 506 too low
    # result_part1 = part_01(task_input)
    # print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(task_input)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    result = part_01(content)
    # put test result here
    assert result == 7

def test_part2():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 33
