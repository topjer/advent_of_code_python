# A - Rock, B - Paper, C - Scissor
# X - Rock, Y - Paper, Z - Scissor
# Rock: 1, Paper: 2, Scissor: 3
# Loss: 0, Draw: 3, Win: 6
RESULTS = {
    ('A', 'X'): 4,
    ('A', 'Y'): 8,
    ('A', 'Z'): 3,
    ('B', 'X'): 1,
    ('B', 'Y'): 5,
    ('B', 'Z'): 9,
    ('C', 'X'): 7,
    ('C', 'Y'): 2,
    ('C', 'Z'): 6,
}

# X - Loss, Y - Draw, Z - Win
RESULTS2 = {
    ('A', 'X'): 3, # Scissor
    ('A', 'Y'): 4, # Rock
    ('A', 'Z'): 8, # Paper
    ('B', 'X'): 1, # Rock
    ('B', 'Y'): 5, # Paper
    ('B', 'Z'): 9, # Scissor
    ('C', 'X'): 2,
    ('C', 'Y'): 6,
    ('C', 'Z'): 7,
}

def load_file(file_path: str):
    with open(file_path) as file:
        content = file.readlines()

    return content

def logic(content, result_dict):
    result = 0

    for line in content:
        # print(line.strip())
        parts = line.split()
        result += result_dict[(parts[0], parts[1])]

    return result

def part_01(task_input: list[str]):
    return logic(task_input, RESULTS)


def part_02(task_input: list[str]):
    return logic(task_input, RESULTS2)


if __name__ == '__main__':
    result_part1 = part_01(load_file('./input/part1'))
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(load_file('./input/part1'))
    print(f"Outcome of part 2 is: {result_part2}.")

def test_part1():
    content = load_file('./tests/part1')
    result = part_01(content)
    assert result == 15

def test_part2():
    content = load_file('./tests/part1')
    result = part_02(content)
    assert result == 12
