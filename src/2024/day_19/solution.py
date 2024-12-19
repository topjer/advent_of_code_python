from utilities import load_file, load_file_single, timing_val
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

# def find_essential_patterns(patterns):
#     result = set()
#     patterns.sort(key=len)
#     print(patterns)

DESIGN_CACHE = dict()

def core(design, patterns):
    if design in DESIGN_CACHE:
        return DESIGN_CACHE[design]
    # print(design)
    if design in patterns:
        DESIGN_CACHE[design] = True
        return True

    for i in range(len(design)):
        head = design[:i]
        tail = design[i:]
        if head in patterns:
            if core(tail, patterns):
                DESIGN_CACHE[design] = True
                return True
    DESIGN_CACHE[design] = False
    return False

def is_reproducible(design, patterns):
    # print(patterns)
    # print("in reproducible")
    # for i in range(1,10):
    for i in range(1,len(design)-1):
        # print("foo:", design[-i:])
        # print()
        foo = core(design[-i:], patterns)
        # print(foo)
        print(DESIGN_CACHE)
    result = core(design, patterns)
    # print(result)
    # result = 0
    return result


def part_01(task_input) -> int:
    patterns, designs, max_length = task_input
    # essential_patterns = find_essential_patterns(patterns)
    # print(patterns)
    # print(designs)
    # print(max_length)
    result = 0
    # designs = ['brbwrrruwrrrubrwuugrbuuwuuwrwrbrrgububwurugbwwrb']
    # designs = ['brgr']
    for design in list(designs):
        # print(design)
        if is_reproducible(design, patterns):
        # if is_reproducible(design, patterns, max_length):
            result += 1
            # print('yes')
        else:
            print(design)
        # break

    # put logic here
    return result


def part_02(task_input) -> int:
    patterns, designs, max_length = task_input
    # essential_patterns = find_essential_patterns(patterns)
    # print(patterns)
    # print(designs)
    # print(max_length)
    result = 0
    # designs = ['brbwrrruwrrrubrwuugrbuuwuuwrwrbrrgububwurugbwwrb']
    # designs = ['brgr']
    for design in list(designs):
        # print(design)
        if is_reproducible(design, patterns):
        # if is_reproducible(design, patterns, max_length):
            result += 1
            # print('yes')
        else:
            print(design)
        # break

    # put logic here
    return result

def parse_input(task_input):
    patterns, designs = task_input.split('\n\n')
    patterns = set(patterns.strip().split(', '))
    max_length = max(len(pat) for pat in patterns)
    designs = designs.strip().split()
    return patterns, designs, max_length

@timing_val
def main():
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    print("start")
    # task_input = parse_input(load_file_single(CURRENT_FOLDER / 'input'))
    # result_part1 = part_01(task_input)
    # print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(task_input)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_01(content)
    # put test result here
    assert result == 6

def test_part2():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 0
