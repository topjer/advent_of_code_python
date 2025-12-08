from utilities import load_file, load_file_single, timing_val
from pathlib import Path
import math
CURRENT_FOLDER = Path(__file__).parent.resolve()

def part_01(points, number_of_pairs:int) -> int:
    print("-------Start Part 1-------")
    result = 1
    # put logic here
    distances = list()
    for index, x, y, z in points:
        for other_index, other_x, other_y, other_z in points[index+1:]:
            # print(index, other_index)
            distance = (x-other_x) ** 2 + (y-other_y) ** 2 + (z-other_z) ** 2
            distances.append((set((index, other_index)), distance))

    # print(distances)
    distances = sorted(distances, key=lambda x: x[1])
    print(distances)
    circuits = list()
    # circuits.append(set(distances.pop(0)[0]))
    # print(distances)
    # print(circuits)
    for pair in distances[0:number_of_pairs]:
        print("Pair:", pair)
        print(circuits)
        for index, circuit in enumerate(circuits):
            if circuit.intersection(pair[0]):
                circuits[index] = circuit.union(pair[0])
                break
        else:
            circuits.append(pair[0])

    lengths = [len(el) for el in circuits]
    lengths = sorted(lengths, reverse=True)
    print(lengths)
    for length in lengths[0:3]:
        result *= length

    return result


def part_02(task_input) -> int:
    result = 0
    # put logic here
    return result

def parse_input(task_input):
    points = list()
    for index, line in enumerate(task_input):
        x,y,z = line.split(',')
        points.append((index, int(x), int(y), int(z)))
    print(points)
    return points

@timing_val
def main():
    print("-------Start-------")
    task_input = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    # task_input = parse_input(load_file(CURRENT_FOLDER / 'input'))
    # 2520
    result_part1 = part_01(task_input, 10)
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(task_input)
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    result = part_01(content)
    # put test result here
    assert result == 40

def test_part2():
    content = parse_input(load_file(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 0
