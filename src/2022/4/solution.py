def load_file(file_path: str):
    with open(file_path) as file:
        content = file.readlines()

    return content


def part_01(task_input: list[str]) -> int:
    result = 0
    for line in task_input:
        elf1, elf2 = line.strip().split(',')
        elf1 = [int(number) for number in elf1.split('-') ]
        elf2 = [int(number) for number in elf2.split('-') ]
        if ( elf1[0] <= elf2[0] ) and (elf2[1] <= elf1[1]):
            result += 1
            continue
        if ( elf2[0] <= elf1[0] ) and (elf1[1] <= elf2[1]):
            result += 1
    # put logic here
    return result


def part_02(task_input: list[str]) -> int:
    result = 0
    for line in task_input:
        elf1, elf2 = line.strip().split(',')
        elf1 = [int(number) for number in elf1.split('-') ]
        elf2 = [int(number) for number in elf2.split('-') ]
        if (elf1[1] < elf2[0]) or (elf2[1] < elf1[0]):
            continue

        result += 1
    # put logic here
    return result


if __name__ == '__main__':
    result_part1 = part_01(load_file('./input'))
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(load_file('./input'))
    print(f"Outcome of part 2 is: {result_part2}.")

def test_part1():
    content = load_file('./tests/part1')
    result = part_01(content)
    # put test result here
    assert result == 2

def test_part2():
    content = load_file('./tests/part1')
    result = part_02(content)
    # put test result here
    assert result == 4
