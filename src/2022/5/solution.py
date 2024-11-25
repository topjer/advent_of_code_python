LIMIT = -1
def load_file(file_path: str):
    with open(file_path) as file:
        content = file.readlines()

    return content


def parse_input(task_input: list[str]):
    split = task_input.index('\n')
    crate_map = [line.replace('\n', '') for line in task_input[:split-1] ]
    number_fields = int(task_input[split-1].split().pop())
    instruction = [instruction.replace('\n', '') for instruction in task_input[split+1:] ]
    if LIMIT != -1:
        del instruction[5:]
    crate_map = parse_crate_map(crate_map, number_fields)
    instruction = parse_instructions(instruction)
    print(crate_map, instruction)
    return crate_map, instruction

def parse_crate_map(crate_map: list[str], number_fields: int) -> list[list[str]]:
    output = [[] for _ in range(number_fields)]
    converted_crate_map = list(map(lambda line: [line[1 + 4*index] for index in range(0, number_fields)], crate_map))
    converted_crate_map.reverse()

    for line in converted_crate_map:
        for index, crate in enumerate(line):
            if crate != ' ':
                output[index].append(crate)

    return output

def parse_instructions(instructions: list[str]):
    parsed_instructions = list(map(lambda instruction: [int(number) for number in instruction.split()[1::2]], instructions))
    return parsed_instructions

def part_01(task_input: list[str]) -> str:
    crate_map, instructions = parse_input(task_input)

    for number, source, target in instructions:
        print(number, source, target)
        source_list = crate_map[source-1]
        target_list = crate_map[target-1]
        print("source", source_list)
        print("target", target_list)
        target_list.extend(list(reversed(source_list[((-1)*number):])))
        del source_list[((-1)*number):]
        print(crate_map)

    
    result = ''.join([row.pop() for row in crate_map])
    # put logic here
    return result


def part_02(task_input: list[str]) -> str:
    crate_map, instructions = parse_input(task_input)

    for number, source, target in instructions:
        print(number, source, target)
        source_list = crate_map[source-1]
        target_list = crate_map[target-1]
        print("source", source_list)
        print("target", target_list)
        target_list.extend(source_list[((-1)*number):])
        del source_list[((-1)*number):]
        print(crate_map)

    
    result = ''.join([row.pop() for row in crate_map])
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
    assert result == 'CMZ'

def test_part2():
    content = load_file('./tests/input')
    result = part_02(content)
    # put test result here
    assert result == 'MCD'
