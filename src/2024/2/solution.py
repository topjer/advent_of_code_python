from utilities import load_file, timing_val
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

@timing_val
def part_01(task_input: list[str]) -> int:
    result = 0
    for line in task_input:
        levels = [int(number) for number in line.split()]
        diffs = [ x-y for x,y in zip(levels[0:-1], levels[1:])]
        if not all(abs(x) < 4 and abs(x) > 0 for x in diffs):
            continue
        if all(x < 0 for x in diffs):
            result += 1
        if all(x > 0 for x in diffs):
            result += 1
    # put logic here
    return result


@timing_val
def part_02(task_input: list[str]) -> int:
    result = 0
    # put logic here
    result = 0
    
    for line in task_input:
        faulty_indices = set()
        levels = [int(number) for number in line.split()]
        diffs = [ x-y for x,y in zip(levels[0:-1], levels[1:])]
        exceeded_increases = [faulty_indices.add(ind) for ind, x in enumerate(diffs) if abs(x) > 3 or abs(x) < 0]
        positive_numbers = [ ind for ind, x in enumerate(diffs) if x>0]
        negative_numbers = [ ind for ind, x in enumerate(diffs) if x<0]
        if len(positive_numbers) == 1:
            faulty_indices.add(positive_numbers.pop())

        if len(negative_numbers) == 1:
            faulty_indices.add(negative_numbers.pop())


        print(faulty_indices)
    return result

def main():
    result_part1 = part_01(load_file(CURRENT_FOLDER / 'input'))
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(load_file(CURRENT_FOLDER / 'tests/input'))
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = load_file(CURRENT_FOLDER / 'tests/input')
    result = part_01(content)
    # put test result here
    assert result == 2

def test_part2():
    content = load_file(CURRENT_FOLDER / 'tests/input')
    result = part_02(content)
    # put test result here
    assert result == 4
