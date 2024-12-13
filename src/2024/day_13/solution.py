from utilities import load_file, load_file_single, timing_val
import re
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

def solution(task_input, increase=0) -> int:
    result = 0
    for (x1, y1), (x2, y2), (p1, p2) in task_input:
        p1, p2 = p1 + increase, p2 + increase
        det = x1 * y2 - x2 * y1
        m1 = (p1 * y2 - p2 * x2) / det
        # if not m1.is_integer():
        #     continue
        m2 = (x1 * p2 - y1 * p1) / det
        if m1.is_integer() and m2.is_integer():
            result += 3*m1 + m2
    return int(result)

@timing_val
def parse_input(task_input):
    games = []
    for crane in task_input.split('\n\n'):
        parts = crane.split('\n')
        # print(crane)
        match = re.findall(r'X\+(\d*),\sY\+(\d*)', parts[0])
        crane_1 = (int(match[0][0]), int(match[0][1]))
        match = re.findall(r'X\+(\d*),\sY\+(\d*)', parts[1])
        crane_2 = (int(match[0][0]), int(match[0][1]))
        match = re.findall(r'X=(\d*), Y=(\d*)', parts[2])[0]
        prize = (int(match[0]), int(match[1]))
        
        # print(crane_1, crane_2, prize)
        games.append((crane_1, crane_2, prize))
    return games

@timing_val
def main():
    print("Start")
    # task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'input'))
    result_part1 = solution(task_input)
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = solution(task_input, 10000000000000)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = solution(content)
    # put test result here
    assert result == 480

