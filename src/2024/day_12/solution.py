import enum
from utilities import load_file, load_file_single, timing_val
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

def get_new_points(point, available_points, garden_map):
    # print("current point" ,point)
    current_value= garden_map[point]
    valid_points = set()
    edges = dict()
    up = (point[0] - 1, point[1])
    down = (point[0] + 1, point[1])
    left = (point[0], point[1] - 1)
    right = (point[0], point[1] + 1)
    if up in available_points:
        if garden_map[up] == current_value:
            valid_points.add(up)
        else:
            edges[point] = (point[0], point[1] + 1)
    else:
            edges[point] = (point[0], point[1] + 1)

    if down in available_points:
        if garden_map[down] == current_value:
            valid_points.add(down)
        else:
            edges[(point[0] + 1, point[1] + 1)] = (point[0] + 1, point[1])
    else:
        edges[(point[0] + 1, point[1] + 1)] = (point[0] + 1, point[1])

    if left in available_points:
        if garden_map[left] == current_value:
            valid_points.add(left)
        else:
            edges[(point[0] + 1, point[1])] = point
    else:
        edges[(point[0] + 1, point[1])] = point
    if right in available_points:
        if garden_map[right] == current_value:
            valid_points.add(right)
        else:
            edges[(point[0], point[1] + 1)] = (point[0] + 1, point[1] + 1)
    else:
        edges[(point[0], point[1] + 1)] = (point[0] + 1, point[1] + 1)
    # print(valid_points)
    return valid_points, edges

def part_01(task_input) -> int:
    result = 0
    available_points = set(task_input.keys())
    regions = set()
    for point, _ in task_input.items():
        if point not in available_points:
            continue
        points_to_check = set([point])
        current_region = set()
        boundary = 0
        # print(points_to_check)
        while points_to_check:
            point = points_to_check.pop()
            # print("current point",point)
            current_region.add(point)
            new_points, edges = get_new_points(point, available_points, task_input)
            print(new_points)
            # print(new_points)
            boundary += 4 - len(new_points)
            for new_point in new_points:
                if new_point in current_region:
                    continue
                else:
                    points_to_check.add(new_point)
                    # available_points.remove(point)
            # break
        # print(current_region)
        result += boundary * len(current_region)
        available_points= available_points.difference(current_region)
        # break

    # put logic here
    return result


def draw_region(current_region):
    # print(current_region)
    min_y = min(point[0] for point in current_region)
    max_y = max(point[0] for point in current_region)
    min_x= min(point[1] for point in current_region)
    max_x = max(point[1] for point in current_region)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (y,x) in current_region:
                print("X", end="")
            else:
                print(".", end="")
        print("")

    # print("")
    # print(min_y, max_y)
    # print(min_x, max_x)


def part_02(task_input) -> int:
    result = 0
    available_points = set(task_input.keys())
    regions = set()
    for point, _ in task_input.items():
        if point not in available_points:
            continue
        points_to_check = set([point])
        current_region = set()
        edge_dict = dict()
        # boundary = 0
        # print(points_to_check)
        while points_to_check:
            point = points_to_check.pop()
            # print("current point",point)
            current_region.add(point)
            new_points, edges = get_new_points(point, available_points, task_input)
            edge_dict.update(edges)
            # print(new_points)
            # boundary += 4 - len(new_points)
            for new_point in new_points:
                if new_point in current_region:
                    continue
                else:
                    points_to_check.add(new_point)
                    # available_points.remove(point)
            # break
        # print(current_region)
        # result += boundary * len(current_region)
        available_points= available_points.difference(current_region)
        # break

        print(edge_dict)
        edges_to_iterate = list(sorted(edge_dict.keys()))
        # print(edges_to_iterate)
        while edges_to_iterate:
            edge = edges_to_iterate.pop()
            # if not edge in edge_dict:
            #     # might happen if this point has been removed in a previous step
            #     continue
            middle_point = edge_dict[edge]
            # print(edge)
            # print("middle point", middle_point)
            if middle_point in edge_dict:
                target_point = edge_dict[middle_point]
                if (edge[0] - middle_point[0] == target_point[0] - middle_point[0]) or (edge[1] - middle_point[1] == target_point[1] - middle_point[1]):
                    edge_dict[edge] = target_point
                    del edge_dict[middle_point]
                    try:
                        edges_to_iterate.remove(middle_point)
                    except Exception:
                        pass
                    edges_to_iterate.append(edge)

            # print(edge_dict)
            # print("iterate list", edges_to_iterate)
            # break
        print("number edges", len(edge_dict))
        draw_region(current_region)
        print(current_region.pop())
        print("End\n")
        # print(edge_dict)
        # print(len(edge_dict), len(current_region))
        result += len(edge_dict) * len(current_region)
        break
    # put logic here
    return result

def parse_input(task_input: str) -> dict[tuple[ int, int ], str]:
    # print(task_input)
    garden_map = dict()
    dimension = task_input.find('\n')
    for index, char in enumerate(task_input.replace('\n', '')):
        garden_map[divmod(index, dimension)] = char
    # print(garden_map)
    return garden_map

@timing_val
def main():
    # part 2: 874361 too low
    print("STart")
    task_input = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
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
    assert result == 1930

def test_part2():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 1206
