from utilities import load_file, load_file_single, timing_val
from pathlib import Path
from typing import Optional
import re
CURRENT_FOLDER = Path(__file__).parent.resolve()

def print_map(current_position, dimension: tuple[int, int], walls, boxes):
    for row in range(dimension[0]):
        for col in range(dimension[1]):
            if (row, col) in walls:
                print("#", end="")
            elif (row, col) in boxes:
                if isinstance(boxes, dict):
                    box2 = boxes[(row, col)]
                    if col < box2[1]:
                        print('[', end='')
                    else:
                        print(']', end='')
                else:
                    print('O', end='')
            elif (row, col) == current_position:
                print('@', end='')
            else:
                print('.', end='')
        print("")
    print("")

MOVES = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
    }

def next_free_field(position, diff, walls, boxes):
    if position in walls:
        return None
    if position in boxes:
        new_point = (position[0] + diff[0], position[1] + diff[1])
        return next_free_field(new_point, diff, walls, boxes)
    return position


def part_01(task_input) -> int:
    result = 0
    current_position, dimension, walls, boxes, moves = task_input
    # print_map(current_position, dimension, walls, boxes)
    for move in moves:
        # print(move)
        diff = MOVES[move]
        new_point = (current_position[0] + diff[0], current_position[1] + diff[1])
        free_field = next_free_field(new_point, diff, walls, boxes)
        if free_field is None:
            continue

        if new_point != free_field:
            boxes.remove(new_point)
            boxes.add(free_field)

        current_position = new_point
        # print_map(current_position, dimension, walls, boxes)

    # put logic here
    return sum(100 * row + col for (row, col) in boxes)

def double_map(task_input):
    current_position, dimension, walls, boxes, moves = task_input
    current_position = (current_position[0], current_position[1] * 2)
    new_walls = set()
    new_boxes = dict()
    for wall in walls:
        new_walls.add((wall[0], wall[1] * 2))
        new_walls.add((wall[0], wall[1] * 2 + 1))

    for box in boxes:
        box1 = (box[0], box[1] * 2)
        box2 = (box[0], box[1] * 2 + 1)
        new_boxes[box1] = box2
        new_boxes[box2] = box1


    return current_position, (dimension[0], dimension[1]*2), new_walls, new_boxes, moves


def valid_horizontal_move(position, diff, walls, boxes) -> Optional[list]:
    # print(position)
    points_to_move = []
    points_to_move.append(position)
    if position in walls:
        return None
    if position in boxes:
        new_point = (position[0] + diff[0], position[1] + diff[1])
        foo = valid_horizontal_move(new_point, diff, walls, boxes)
        # print(foo)
        if foo is not None:
            points_to_move.extend(foo)
            # print(points_to_move)
        else:
            return None
    else:
        return []
    return points_to_move

def valid_vertical_move(positions, diff, walls, boxes) -> Optional[set]:
    points_to_move = set()
    for position in positions:
        if position in walls:
            return None
        if position in boxes:
            box2 = boxes[position]
            points_to_move.add(position)
            points_to_move.add(box2)
            # print(points_to_move)
            nbox1 = (position[0] + diff[0], position[1] + diff[1])
            nbox2 = (box2[0] + diff[0], box2[1] + diff[1])
            # print(nbox1, nbox2)
            foo = valid_vertical_move([nbox1], diff, walls, boxes)
            bar = valid_vertical_move([nbox2], diff, walls, boxes)
            if foo is not None:
                points_to_move = points_to_move.union(foo)
            else:
                return None
            if bar is not None:
                points_to_move = points_to_move.union(bar)
            else:
                return None
        else:
            return set()
    return points_to_move

def part_02(task_input) -> int:
    result = 0
    current_position, dimension, walls, boxes, moves = double_map(task_input)
    # print_map(current_position, dimension, walls, boxes)
    for index, move in enumerate(moves):
        # if index > 414:
        #     break
        # print("Current Move:", index, move)
        # print(move)
        diff = MOVES[move]
        new_point = (current_position[0] + diff[0], current_position[1] + diff[1])
        # print(boxes)
        if move in ('<', '>'):
            boxes_to_move = valid_horizontal_move(new_point, diff, walls, boxes)
            # print(boxes_to_move)
            if boxes_to_move is not None:
                sorted(boxes_to_move)
                # print(boxes_to_move)
                temp_dict = dict()
                while boxes_to_move:
                # for box1 in boxes_to_move:
                    box1 = boxes_to_move.pop()
                    box2 = boxes.pop(box1)
                    # print(box1)
                    # print(box2)
                    # print(box1, box2)
                    _ = boxes.pop(box2)
                    _ = boxes_to_move.remove(box2)
                    nbox1 = (box1[0] + diff[0], box1[1] + diff[1])
                    nbox2 = (box2[0] + diff[0], box2[1] + diff[1])
                    temp_dict[nbox1] = nbox2
                    temp_dict[nbox2] = nbox1
                    # print(boxes)
                boxes.update(temp_dict)
                current_position = new_point
        if move in ('^', 'v'):
            boxes_to_move = valid_vertical_move([new_point], diff, walls, boxes)
            if boxes_to_move is not None:
                boxes_to_move = list(boxes_to_move)
                sorted(boxes_to_move)
                # print(boxes_to_move)
                temp_dict = dict()
                while len(boxes_to_move) > 0:
                # for box1 in boxes_to_move:
                    box1 = boxes_to_move.pop()
                    box2 = boxes.pop(box1)
                    # print(box1, box2)
                    _ = boxes.pop(box2)
                    _ = boxes_to_move.remove(box2)
                    nbox1 = (box1[0] + diff[0], box1[1] + diff[1])
                    nbox2 = (box2[0] + diff[0], box2[1] + diff[1])
                    temp_dict[nbox1] = nbox2
                    temp_dict[nbox2] = nbox1
                boxes.update(temp_dict)
                current_position = new_point
        # break

        # print_map(current_position, dimension, walls, boxes)

    points = dict()
    for box1 in boxes:
        box2 = boxes[box1]
        if box2 in points:
            continue
        points[box1] = 100 * box1[0] + min(box1[1], box2[1])

    result = sum(val for _, val in points.items())
    # put logic here
    return result

def parse_input(task_input):
    # print(task_input)
    dimension = task_input.find('\n')
    warehouse, moves = task_input.split('\n\n')
    warehouse = warehouse.replace('\n', '')
    moves = moves.strip().replace('\n', '')
    start = divmod(warehouse.find('@'), dimension)
    walls = set(divmod(m.start(), dimension) for m in re.finditer(r'#', warehouse))
    boxes = set(divmod(m.start(), dimension) for m in re.finditer(r'O', warehouse))
    return start, (dimension, dimension), walls, boxes, moves

@timing_val
def main():
    print("start")
    # task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/small_test_part2'))
    # task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'input'))
    result_part1 = part_01(task_input)
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(task_input)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_01(content)
    # put test result here
    assert result == 10092

def test_part2():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 9021 
