from utilities import load_file, load_file_single, timing_val
from pathlib import Path
import math
CURRENT_FOLDER = Path(__file__).parent.resolve()

def part_01(points, number_of_pairs:int) -> tuple[int, int]:
    result_part1 = 1
    result_part2 = 0
    # put logic here
    distances = list()
    for index, x, y, z in points:
        for other_index, other_x, other_y, other_z in points[index+1:]:
            # print(index, other_index)
            distance = (x-other_x) ** 2 + (y-other_y) ** 2 + (z-other_z) ** 2
            distances.append((set((index, other_index)), distance))

    # print(distances)
    distances = sorted(distances, key=lambda x: x[1])
    # print(distances)
    circuits = list()
    # circuits.append(set(distances.pop(0)[0]))
    # print(distances)
    for outer_index, pair in enumerate(distances[0:number_of_pairs]):
        # print("Pair:", pair)
        # print(circuits)
        affected_indexes = list()
        for index, circuit in enumerate(circuits):
            if circuit.intersection(pair[0]):
                affected_indexes.append(index)
        # print(affected_indexes)
        if len(affected_indexes) == 1:
            index = affected_indexes[0]
            circuits[index] = circuits[index].union(pair[0])
        elif len(affected_indexes) == 2:
            # todo: there must be a smarter way for this
            if affected_indexes[0] > affected_indexes[1]:
                set1 = circuits.pop(affected_indexes[0])
                set2 = circuits.pop(affected_indexes[1])
            else:
                set2 = circuits.pop(affected_indexes[1])
                set1 = circuits.pop(affected_indexes[0])
            circuits.append(set1.union(set2))
        else:
            circuits.append(pair[0])
        # print(len(circuits), outer_index)
        if len(circuits) == 1 and len(next(iter(circuits))) == len(points):
            # print("Final pair", pair)
            last_points = list(pair[0])
            result_part2 = points[last_points[0]][1] * points[last_points[1]][1]
            break

        if outer_index == 1000:
            lengths = [len(el) for el in circuits]
            lengths = sorted(lengths, reverse=True)
            # print(lengths)
            for length in lengths[0:3]:
                result_part1 *= length

    return result_part1, result_part2


def part_02(task_input) -> int:
    result = 0
    # put logic here
    return result

def parse_input(task_input):
    points = list()
    for index, line in enumerate(task_input):
        x,y,z = line.split(',')
        points.append((index, int(x), int(y), int(z)))
    # print(points)
    return points

@timing_val
def main():
    # task_input = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    task_input = parse_input(load_file(CURRENT_FOLDER / 'input'))
    # 133574
    # 2435100380
    result_part1, result_part2 = part_01(task_input, 10000)
    print(f"Outcome of part 1 is: {result_part1}.")
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    result, _ = part_01(content, 10)
    # put test result here
    assert result == 40

def test_part2():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    _, result = part_01(content, 100)
    # put test result here
    assert result == 25272
