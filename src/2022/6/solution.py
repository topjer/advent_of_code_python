def load_file(file_path: str):
    with open(file_path) as file:
        content = file.readlines()

    return content


def logic(task_input: list[str], number_characters: int) -> int:
    result = 0
    for pos in range(len(task_input[0])):
        character_slice = task_input[0][max(0, pos - number_characters):pos]
        if len(set(character_slice)) == number_characters:
            result = pos
            break
    return result


def part_01(task_input: list[str]) -> int:
    result = 0
    result = logic(task_input=task_input, number_characters=4)
    # put logic here
    return result


def part_02(task_input: list[str]) -> int:
    result = 0
    # put logic here
    result = logic(task_input=task_input, number_characters=14)
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
    assert result == 7

def test_part2():
    content = load_file('./tests/input')
    result = part_02(content)
    # put test result here
    assert result == 19
