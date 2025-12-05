from utilities import load_file, load_file_single, timing_val
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

def part_01(task_input) -> int:
    result = 0
    id_bounds, ids = task_input
    # put logic here
    for id_number in ids:
        # print(id_number)
        for bound in id_bounds:
            # print(bound)
            if id_number < bound[0]:
                continue
            elif id_number <= bound[1]:
                result += 1
                break

    return result


def part_02(task_input) -> int:
    # todo: potential optimization: first optimize bounds from step 2 and then perform check from step 1
    result = 0
    id_bounds, _ = task_input
    valid_bounds = [id_bounds.pop()]
    # put logic here
    while id_bounds:
        unchecked_element = id_bounds.pop()
        valid_element = valid_bounds.pop()
        if unchecked_element[1] >= valid_element[0]:
            if unchecked_element[0] >= valid_element[0]:
                # this means that unchecked_element is contained in valid_element
                valid_bounds.append(valid_element)
            else:
                valid_bounds.append((unchecked_element[0], valid_element[1]))
        else:
            valid_bounds.append(valid_element)
            valid_bounds.append(unchecked_element)

    # print(valid_bounds)

    for valid_bound in valid_bounds:
        result += (valid_bound[1] - valid_bound[0] + 1)

    return result

def parse_input(task_input):
    ranges, ids = task_input.split('\n\n')
    id_bounds = []
    for id_range in ranges.split():
        lower, upper = id_range.split('-')
        id_bounds.append((int(lower), int(upper)))
    # sort list by upper bounds
    id_bounds = sorted(id_bounds, key=lambda x: x[1])
    ids = [int(id_number) for id_number in ids.split()]

    return id_bounds, ids

@timing_val
def main():
    # task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'input'))
    result_part1 = part_01(task_input)
    print(f"Outcome of part 1 is: {result_part1}.")
    # 321373478075864 too low
    # 345755049374932 
    result_part2 = part_02(task_input)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_01(content)
    # put test result here
    assert result == 3

def test_part2():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 14
