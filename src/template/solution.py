def load_file(file_path: str):
    with open(file_path) as file:
        content = file.readlines()

    return content


def part_01(task_input: list[str]) -> int:
    result = 0
    # put logic here
    return result


def part_02(task_input: list[str]) -> int:
    result = 0
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
    assert result == 0

def test_part2():
    content = load_file('./tests/input')
    result = part_02(content)
    # put test result here
    assert result == 0
