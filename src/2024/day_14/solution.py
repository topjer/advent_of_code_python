from utilities import load_file, load_file_single, timing_val
import re
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

def part_01(task_input) -> int:
    robots, dimensions = task_input
    middle = ((dimensions[0] - 1) // 2, (dimensions[1] - 1) //2)
    steps = 100
    q1, q2, q3, q4 = 0, 0, 0, 0
    for (p,v) in robots:
        new_position = ((p[0] + steps * v[0]) % dimensions[0], (p[1] + steps * v[1]) % dimensions[1])

        if new_position[0] < middle[0] and new_position[1] < middle[1]:
            q1 += 1

        if new_position[0] > middle[0] and new_position[1] < middle[1]:
            q2 += 1

        if new_position[0] < middle[0] and new_position[1] > middle[1]:
            q3 += 1

        if new_position[0] > middle[0] and new_position[1] > middle[1]:
            q4 += 1
    # print(q1, q2, q3 , q4)
    return q1 * q2 * q3 * q4


def part_02(task_input) -> int:
    robots, dimensions = task_input
    result = 0
    x_vars, y_vars = [], []
    for step in range(104):
        x_pos, y_pos = [], []
        for (p,v) in robots:
            new_position = ((p[0] + step * v[0]) % dimensions[0], (p[1] + step * v[1]) % dimensions[1])
            x_pos.append(new_position[0])
            y_pos.append(new_position[1])

        # calculate variance for x and y positions seperately in order to find the index
        # when the variance becomes minimal in each dimension. By the definition of the problem
        # this minimum reoccurs periodically. For x the period is the x dimension and for y respectively.
        # Then we have to find the step when both minima are attained at the same time. One could use
        # chinese remainder theorem for that or brute fore it.
        x_mean = sum(x_pos) / len(x_pos)
        x_var = sum((xi - x_mean) ** 2 for xi in x_pos) / len(x_pos)
        x_vars.append(x_var)
        y_mean = sum(y_pos) / len(y_pos)
        y_var = sum((yi - y_mean) ** 2 for yi in y_pos) / len(y_pos)
        y_vars.append(y_var)
    x_cand = x_vars.index(min(x_vars))
    y_cand = y_vars.index(min(y_vars))
    # brute force indexes, luckily we only have to check until the product of dimensions which is 
    # manageable for a 2 dimensional problem
    for i in range(dimensions[0] * dimensions[1] + 1):
        if i % dimensions[0] == x_cand and i % dimensions[1] == y_cand:
            result = i
            break
    
    # put logic here
    return result

def parse_input(task_input, dimensions):
    # print(task_input)
    robots = []
    for match in re.finditer(r'p=(\d*),(\d*)\sv=(-?\d*),(-?\d*)', task_input):
        # print(match.group(1), match.group(2), match.group(3), match.group(4))
        p = (int(match.group(1)), int(match.group(2)))
        v = (int(match.group(3)), int(match.group(4)))
        # print(p,v)
        robots.append((p,v))
    return robots, dimensions

@timing_val
def main():
    print("Start")
    # task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'), (11,7))
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'input'), (101, 103))
    result_part1 = part_01(task_input)
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(task_input)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'), (11,7))
    result = part_01(content)
    # put test result here
    assert result == 12

def test_part2():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'), (11,7))
    result = part_02(content)
    # put test result here
    assert result == 0
