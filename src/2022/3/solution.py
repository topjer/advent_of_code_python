def load_file(file_path: str):
    with open(file_path) as file:
        content = file.readlines()

    return content


def compute_value(input_string: str):
    if input_string.islower():
        return ord(input_string) - 96
    else:
        return ord(input_string) - 38 


def part_01(task_input: list[str]) -> int:
    result = 0
    for line in task_input:
        compartment_length = int(len(line.strip())/2)
#        print(compartment_length)
        first_half = set(line[:int(compartment_length)])
        second_half = set( line[int(compartment_length):] )
        appears_in_both = first_half.intersection(second_half).pop()
        result += compute_value(appears_in_both)
    # put logic here
    return result


def part_02(task_input: list[str]) -> int:
    result = 0
    while len(task_input) > 0:
        elf1, elf2, elf3 = task_input[:3]
        del task_input[:3]

        badge = set(elf1.strip()).intersection(set(elf2.strip())).intersection(set(elf3.strip())).pop()
        result += compute_value(badge)
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
    assert result == 157

def test_part2():
    content = load_file('./tests/part1')
    result = part_02(content)
    # put test result here
    assert result == 70
