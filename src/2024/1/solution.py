from utilities import load_file, timing_val


def create_lists(task_input: list[str]) -> tuple[list[int], list[int]]:
    left_list = []
    right_list = []
    for line in task_input:
        parts = list(map(lambda x: int(x), line.strip().split()))
        left_list.append(parts[0])
        right_list.append(parts[1])

    return left_list, right_list

@timing_val
def part_01(task_input: list[str]) -> int:
    result = 0

    left_list, right_list = create_lists(task_input)

    left_list.sort()
    right_list.sort()
    # print(left_list)
    # print(right_list)
    result = sum(map(lambda x: abs(x[0] - x[1]), zip(left_list, right_list)))
    # put logic here
    return result


@timing_val
def part_02(task_input: list[str]) -> int:
    result = 0
    left_list, right_list = create_lists(task_input)
    observed_quantities = dict()
    for number in left_list:
        if number not in observed_quantities:
            observed_quantities[number] = len([lookup for lookup in right_list if lookup == number])

        result += number * observed_quantities[number]
    # put logic here
    return result


if __name__ == '__main__':
    result_part1 = part_01(load_file('./input'))
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(load_file('./input'))
    print(f"Outcome of part 2 is: {result_part2}.")

def test_part1():
    content = load_file('./tests/input')
    result = part_01(content)
    # put test result here
    assert result == 11

def test_part2():
    content = load_file('./tests/input')
    result = part_02(content)
    # put test result here
    assert result == 31
