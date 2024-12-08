from utilities import load_file, timing_val, load_file_single
from pathlib import Path
import re
CURRENT_FOLDER = Path(__file__).parent.resolve()

def valid_point(point, dimension):
    return (0<=point[0]<dimension) and (0<=point[1]<dimension)

@timing_val
def solution(task_input) -> tuple[int, int]:
    positions = dict()
    cleaned_task_input = task_input.replace('\n', '')
    dimension = task_input.find('\n')
    antinodes = set()
    purely_harmonics = set()
    matches = re.finditer(r'[^\.]', cleaned_task_input)
    for match in matches:
        character = match.group(0)
        position = divmod(int(match.start()), dimension)
        if character in positions:
            positions[character].append(position)
        else:
            positions[character] = [position]
    for character, coordinates in positions.items():
        while coordinates:
            leading_node = coordinates.pop()
            purely_harmonics.add(leading_node)
            for coordinate in coordinates:
                diff_x = leading_node[0] - coordinate[0]
                diff_y = leading_node[1] - coordinate[1]

                for i in range(1,100):
                    antinode1 = (leading_node[0] + i*diff_x, leading_node[1] + i*diff_y)

                    if valid_point(antinode1, dimension):
                        if i == 1:
                            antinodes.add(antinode1)
                        else:
                            purely_harmonics.add(antinode1)
                    else:
                        break

                for i in range(1,100):
                    antinode2 = (coordinate[0] - i*diff_x, coordinate[1] - i*diff_y)
                    if valid_point(antinode2, dimension):
                        if i==1:
                            antinodes.add(antinode2)
                        else:
                            purely_harmonics.add(antinode2)
                    else:
                        break
    return len(antinodes), len(purely_harmonics.difference(antinodes)) + len(antinodes)

def parse_input(task_input):
    return task_input

def main():
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'input'))
    # task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/input'))
    result_part1, result_part2 = solution(task_input)
    print(f"Outcome of part 1 is: {result_part1}.")
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result, _ = solution(content)
    # put test result here
    assert result == 14

def test_part2():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    _, result = solution(content)
    # put test result here
    assert result == 34
