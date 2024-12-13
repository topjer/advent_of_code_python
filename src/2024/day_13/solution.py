from utilities import load_file, load_file_single, timing_val
import re
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

def calculation(x1, x2, y1, y2, p1, p2, increase):
    p1, p2 = p1 + increase, p2 + increase
    det = x1 * y2 - x2 * y1
    m1 = (p1 * y2 - p2 * x2) / det
    # if not m1.is_integer():
    #     return 0
    m2 = (x1 * p2 - y1 * p1) / det
    if m1.is_integer() and m2.is_integer():
        return 3 * m1 + m2
    else:
        return 0


def solution(task_input) -> tuple[int, int]:
    result1 = 0
    result2 = 0
    for (x1, y1), (x2, y2), (p1, p2) in task_input:
        result1 += calculation(x1, x2, y1, y2, p1, p2, 0)
        result2 += calculation(x1, x2, y1, y2, p1, p2, 10000000000000)
    return int(result1), int(result2)

@timing_val
def parse_input(task_input):
    match = re.finditer(r'X[\+=](\d*),\sY[\+=](\d*)', task_input)
    while True:
        try:
            crane1 = next(match)
        except Exception:
            break
        crane2 = next(match)
        prize = next(match)
        # games.append(list(((int(el.group(1)), int(el.group(2)))) for el in (crane1, crane2, prize)))
        yield (((int(el.group(1)), int(el.group(2)))) for el in (crane1, crane2, prize))
    # return games

@timing_val
def main():
    print("Start")
    # task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'input'))
    result_part1, result_part2 = solution(task_input)
    print(f"Outcome of part 1 is: {result_part1}.")
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = solution(content)
    # put test result here
    assert result == 480

