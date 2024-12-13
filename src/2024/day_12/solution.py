from utilities import load_file, load_file_single, timing_val
from collections import defaultdict, Counter
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

def get_new_points(point, available_points, garden_map):
    # print("current point" ,point)
    current_value= garden_map[point]
    valid_points = set()
    edges = defaultdict(list)
    N = (point[0] - 1, point[1])
    N_val = garden_map.get(N)
    E = (point[0], point[1] + 1)
    E_val = garden_map.get(E)
    S = (point[0] + 1, point[1])
    S_val = garden_map.get(S)
    W = (point[0], point[1] - 1)
    W_val = garden_map.get(W)

    # print(N, E, S, W)
    if N in available_points:
        if N_val == current_value:
            valid_points.add((point[0] - 1, point[1]))

    if S in available_points:
        if S_val == current_value:
            valid_points.add((point[0] + 1, point[1]))

    if W in available_points:
        if W_val == current_value:
            valid_points.add((point[0], point[1] - 1))

    if E in available_points:
        if E_val == current_value:
            valid_points.add((point[0], point[1] + 1))

    # print(valid_points)
    return valid_points, edges

def find_edges(points):
    print(points)
    draw_region(points)
    edges = Counter()
    for point in points:
        N = (point[0] - 1, point[1])
        NE = (point[0] - 1, point[1] + 1)
        E = (point[0], point[1] + 1)
        SE = (point[0] + 1, point[1] + 1)
        S = (point[0] + 1, point[1])
        SW = (point[0] + 1, point[1] -1 )
        W = (point[0], point[1] - 1)
        NW = (point[0] - 1 , point[1] - 1)

        if (N not in points) and (W not in points):
            edges.update( [ point ] )

        if (N in points) and (W in points) and (NW not in points):
            edges.update( [ point ] )

        if (W not in points) and (S not in points):
            edges.update( [ point ] )

        if (W in points) and (S in points) and (SW not in points):
            edges.update( [ point ] )

        if (E not in points) and (S not in points):
            edges.update( [ point ] )

        if (E in points) and (S in points) and (SE not in points):
            edges.update( [ point ] )

        if (E not in points) and (N not in points):
            edges.update( [ point ] )

        if (E in points) and (N in points) and (NE not in points):
            edges.update( [ point ] )

    print(edges)
    return edges


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
            # print(new_points)
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

def edge_reduction():
    # this function contains code that takes the outline of a polygon of 
    # squares in steps of the individual squares and identifies longer edges
        # edges_to_iterate = list(sorted(edge_dict.keys()))
        # # print(edges_to_iterate)
        # while edges_to_iterate:
        #     edge = edges_to_iterate.pop()
        #     # if not edge in edge_dict:
        #     #     # might happen if this point has been removed in a previous step
        #     #     continue
        #     print(edge_dict)
        #     middle_points = edge_dict[edge]
        #     # print(edge)
        #     # print("middle point", middle_point)
        #     for middle_point in middle_points:
        #         print("middle",middle_point)
        #         if middle_point in edge_dict:
        #             target_points = edge_dict[middle_point]
        #             print("target",target_points)
        #             for target_point in target_points:
        #                 if (edge[0] - middle_point[0] == target_point[0] - middle_point[0]) or (edge[1] - middle_point[1] == target_point[1] - middle_point[1]):
        #                     edge_dict[edge] = target_point
        #                     del edge_dict[middle_point]
        #                     try:
        #                         edges_to_iterate.remove(middle_point)
        #                     except Exception:
        #                         pass
        #                     edges_to_iterate.append(edge)
        #
        #     # print(edge_dict)
        #     # print("iterate list", edges_to_iterate)
        #     # break
        # print("number edges", len(edge_dict))
        # draw_region(current_region)
        # print(current_region.pop())
        # print("End\n")
        # print(edge_dict)
        # print(len(edge_dict), len(current_region))
    pass

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
            new_points, _ = get_new_points(point, available_points, task_input)
            # edge_dict.update(edges)
            # print(new_points)
            # boundary += 4 - len(new_points)
            for new_point in new_points:
                if new_point in current_region:
                    continue
                else:
                    points_to_check.add(new_point)
                    # available_points.remove(point)
            # break
        edges = find_edges(current_region)
        # print(current_region)
        available_points= available_points.difference(current_region)
        # print(edge_dict)
        result += sum(val for _, val in edges.items()) * len(current_region)
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
    print("STart")
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
    assert result == 1930

def test_part2():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 1206
