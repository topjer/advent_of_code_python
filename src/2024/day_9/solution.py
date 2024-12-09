from collections import deque
from typing import Optional
from utilities import load_file, load_file_single, timing_val
from pathlib import Path
from dataclasses import dataclass  
CURRENT_FOLDER = Path(__file__).parent.resolve()

def part_01(task_input) -> int:
    result = 0
    file_queue, empty_queue = task_input
    result_stack = []
    # this one has id 0 and thus does not contribute to the result
    result_stack.append(file_queue.popleft())
    # print("start")
    # print(file_queue)
    # print(empty_queue)
    # print("loop start")
    while file_queue:
    # for _ in range(13):
        empty_field = empty_queue.popleft()
        filler = file_queue.pop()
        if filler.start < empty_field.start:
            break
        if filler.length > empty_field.length:
            file_queue.append(Position(filler.start, filler.length - empty_field.length, filler.id))
            # empty_queue.append(Position(filler.start + empty_field.length + 1, empty_field.length))
            result_stack.append(Position(empty_field.start, empty_field.length, filler.id))
            if file_queue:
                result_stack.append(file_queue.popleft())
        elif filler.length == empty_field.length:
            # empty_queue.append(Position(filler.start, filler.length))
            result_stack.append(Position(empty_field.start, empty_field.length, filler.id))
            if file_queue:
                result_stack.append(file_queue.popleft())
        else:
            # empty_queue.append(Position(filler.start, filler.length))
            empty_queue.appendleft(Position(empty_field.start + filler.length, empty_field.length - filler.length))
            result_stack.append(Position(empty_field.start, filler.length, filler.id))

    # print(result_stack)
    for file in result_stack:
        result += sum(range(file.start, file.start + file.length)) * file.id
    # put logic here
    return result

def part_02(task_input) -> int:
    result = 0
    file_queue, empty_queue = task_input
    # create dictionary for empty spots
    queue_dict = dict()
    while empty_queue:
        item = empty_queue.popleft()
        if item.length in queue_dict:
            queue_dict[item.length].append(item)
        else:
            queue_dict[item.length] = [item]

    # print(queue_dict)

    result_stack = []

    while file_queue:
        
        element = file_queue.pop()
        # go through all keys that are bigger or equal to the searched length and get start of smalles element
        # also make sure that you only consider fits that are left of element
        possible_fits = [(key, value[0].start) for key, value in queue_dict.items() if key >= element.length 
                          and value and value[0].start < element.start]
        possible_fits.sort(key=lambda x: -x[1])
        if not possible_fits:
            result_stack.append(element)
            continue
        # print(element) 
        # print(possible_fits)
        possible_fit_key = possible_fits.pop()[0]
        possible_fit = queue_dict[possible_fit_key].pop(0)

        # print(possible_fit)
        result_stack.append(Position(possible_fit.start, element.length, element.id))

        if element.length < possible_fit.length:
            new_length = possible_fit.length - element.length
            to_modify = queue_dict[new_length]
            to_modify.append(Position(possible_fit.start + element.length, new_length))
            # possible optimization is to determine the position where to put the new element
            to_modify.sort(key=lambda x: x.start)
            queue_dict[new_length] = to_modify

    # print(result_stack)

    for file in result_stack:
        result += sum(range(file.start, file.start + file.length)) * file.id
    # put logic here
    return result

@dataclass
class Position:
    start: int
    length: int
    id: Optional[int] = None

def parse_input(task_input):
    task_input = list(int(entry) for entry in task_input.strip()[::-1])
    current_position = 0
    current_id = 0
    file_queue = deque()
    empty_queue = deque()

    while task_input:
        file = task_input.pop()
        file_queue.append(Position(current_position, file, current_id))
        current_position += file
        current_id += 1
        try:
            empty = task_input.pop()
        except Exception:
            continue
        empty_queue.append(Position(current_position, empty))
        current_position += empty

    return file_queue, empty_queue

@timing_val
def main():
    # task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'input'))
    result_part1 = part_01(task_input)
    print(f"Outcome of part 1 is: {result_part1}.")
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'input'))
    result_part2 = part_02(task_input)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_01(content)
    # put test result here
    assert result == 1928

def test_part2():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 2858
