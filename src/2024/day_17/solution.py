from utilities import load_file, load_file_single, timing_val
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

def combo_operand(co, reg_a, reg_b, reg_c):
    if 0 <= co < 4:
        return co
    elif co == 4:
        return reg_a
    elif co == 5:
        return reg_b
    elif co == 6:
        return reg_c
    else:
        raise Exception("Invalid Operand")

def part_01(task_input):
    reg_a, reg_b, reg_c, prog, _ = task_input
    output = run_command(reg_a, reg_b, reg_c, prog)
    return output

def run_command(reg_a, reg_b, reg_c, prog):
    instruction_pointer = 0
    output = []
    while instruction_pointer < len(prog):
        opcode, operand = prog[instruction_pointer]
        if opcode == 0:
            reg_a = reg_a // 2 ** combo_operand(operand, reg_a, reg_b, reg_c)
        elif opcode == 1:
            reg_b = reg_b ^ operand
        elif opcode == 2:
            reg_b = combo_operand(operand, reg_a, reg_b, reg_c) % 8
        elif opcode == 3:
            if reg_a != 0:
                instruction_pointer = operand
                continue
        elif opcode == 4:
            reg_b = reg_b ^ reg_c
        elif opcode == 5:
            output.append(combo_operand(operand, reg_a, reg_b, reg_c) % 8)
        elif opcode == 6:
            reg_b = reg_a // 2 ** combo_operand(operand, reg_a, reg_b, reg_c)
        elif opcode == 7:
            reg_c = reg_a // 2 ** combo_operand(operand, reg_a, reg_b, reg_c)

        instruction_pointer += 1
    return output

def part_02(task_input) -> int:
    """ Values from 0 to 7 are mapped to one character outputs
    Values from 8 to 64 are mapped to two character outputs
    Values from 8 ** (n-1) to 8 ** n are mapped to n character outputs

    If first position is found on 0<=k<=7, then the second position will be found in 
    k*8 till k*8-7 including boundaries
    """
    result = 0
    _, reg_b, reg_c, prog, prog_raw = task_input
    # for i in range(5):
    index = 0
    for i in range(len(prog_raw)):
        for position in range(index * 8, index * 8 + 8):
            result = run_command(position, reg_b, reg_c, prog)
            compare = prog_raw[(-1)*(i + 1):]
            if result == compare:
                index = position
                break
    return index

def parse_input(task_input):
    reg_a = int(task_input[0].split(':')[1].strip())
    reg_b = int(task_input[1].split(':')[1].strip())
    reg_c = int(task_input[2].split(':')[1].strip())
    prog = [int(num) for num in task_input[-1].split(':')[1].strip().split(',')]
    prog_parsed = [(prog[2*i], prog[2*i+1]) for i in range(len(prog)//2)]
    return reg_a, reg_b, reg_c, prog_parsed, prog

@timing_val
def main():
    print("Start")
    # task_input = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file(CURRENT_FOLDER / 'input'))
    result_part1 = part_01(task_input)
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(task_input)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    result = part_01(content)
    # put test result here
    assert result == 0

def test_part2():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 0
