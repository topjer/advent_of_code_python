from utilities import load_file, load_file_single, timing_val
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

DESIGN_CACHE = dict()

def core(design, patterns):
    result = 0
    if design in DESIGN_CACHE:
        return DESIGN_CACHE[design]
    if design in patterns:
        result += 1

    for i in range(len(design)):
        head = design[:i]
        tail = design[i:]
        if head in patterns:
            result += core(tail, patterns)

    DESIGN_CACHE[design] = result
    return result

def get_all_options(design, patterns):
    """ Core idea is that we start "from the end"

    This way we ensure that we have to compute every combination only once and thus 
    we get the maximum out of caching.
    """
    for i in range(1,len(design)):
        _ = core(design[-i:], patterns)
    result = core(design, patterns)
    return result


def part_02(task_input) -> tuple[int, int]:
    patterns, designs = task_input
    result_p1 = 0
    result_p2 = 0
    for design in list(designs):
        res = get_all_options(design, patterns)
        result_p2 += res
        if res > 0:
            result_p1 += 1

    return result_p1, result_p2

def parse_input(task_input):
    patterns, designs = task_input.split('\n\n')
    patterns = set(patterns.strip().split(', '))
    designs = designs.strip().split()
    return patterns, designs

@timing_val
def main():
    # task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    print("start")
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'input'))
    result_part1, result_part2 = part_02(task_input)
    print(f"Outcome of part 1 is: {result_part1}.")
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part2():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result_p1, result_p2 = part_02(content)
    # put test result here
    assert result_p1 == 6
    assert result_p2 == 16
