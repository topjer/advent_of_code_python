import re
from collections import deque
from typing import Optional

def grid_parser(task_input: str, schema: dict[str, str]):
    """ Parser for 2d grids.

    It is assumed that the grid is provided as a single string with lines separated by '\n'

    Inputs
    ------
    task_input
        raw input string, lines separated by '\n'
    schema
        keys are name of the target variable, values are the search values to be used, only single
        character search values have been tested.

    Returns
    -------
        dictionary that contains the dimension of the grid as a tuple where the first number is the
        number or rows and the second the number of columns
        Additionally, it returns the coordinates of all matches for the search terms provided. If only
        one result is found, it is returned as a single point, else a set of points is returned.
    """
    dimension_col = task_input.find('\n')
    dimension_row = len(task_input.split())
    print(dimension_row, dimension_col)
    cleaned_input = task_input.replace('\n', '')
    result = dict()
    result['dimension'] = (dimension_row, dimension_col)
    for name, search_value in schema.items():
        temp = set(divmod(match.start(), dimension_row) for match in re.finditer(search_value, cleaned_input))
        if len(temp) == 1:
            result[name] = temp.pop()
        else:
            result[name] = temp

    return result


def print_map(
    current_position: tuple[int, int],
    dimension: tuple[int, int],
    walls: set[tuple[int, int]],
    highlights: set[tuple[int, int]],
):
    """ Print a rectangular grid limited by walls

    Inputs
    ------
    current_position
        position to highlight
    dimension
        first entry is number of rows, second entry is number of columns
    walls
        limits of the grid, drawn as '#'
    highlights
        set of points to highlight, use it for objects or the path taken
    """
    for row in range(dimension[0]):
        for col in range(dimension[1]):
            if (row, col) in walls:
                print("#", end="")
            elif (row, col) == current_position:
                print('@', end='')
            elif (row, col) in highlights:
                print('O', end='')
            else:
                print('.', end='')
        print("")
    print("")

def is_valid(point, dimension):
    return (0 <= point[0] <= dimension[0]) and (0 <= point[1] <= dimension[1])

def find_shortest_path(
    start: tuple[int,int],
    goal: tuple[int,int],
    dimension: tuple[int, int],
    walls: set[tuple[int,int]]
) -> Optional[list[tuple[int,int]]]:
    """ Find the shortest path through a 2D grid bounded by `walls`

    :inputs:
    start
        point from where to start the path
    goal
        point to be reached
    dimension
        number of fields in both dimensions, needed to decide whether a point is valid or not
    walls
        set of obstacles one cannot move through

    :return:
    list of points the path consists off
    """
    paths_to_check = deque()
    paths_to_check.append([start])
    seen_points = set()
    solution = None
    while paths_to_check:
        current_path = paths_to_check.popleft()
        current_point = current_path[-1]
        # this is the most important path because it leads to super fast convergence
        if current_point in seen_points:
            continue
        else:
            seen_points.add(current_point)
        # check up
        if (up:=(current_point[0], current_point[1]-1)) not in walls and is_valid(up, dimension):
            if up not in current_path:
                temp = current_path[:]
                temp.append(up)
                paths_to_check.append(temp)
                if up == goal:
                    solution = temp
                    break

        if (down:=(current_point[0], current_point[1]+1)) not in walls and is_valid(down, dimension):
            if down not in current_path:
                temp = current_path[:]
                temp.append(down)
                paths_to_check.append(temp)
                if down == goal:
                    solution = temp
                    break

        if (left:=(current_point[0]-1, current_point[1])) not in walls and is_valid(left, dimension):
            if left not in current_path:
                temp = current_path[:]
                temp.append(left)
                paths_to_check.append(temp)
                if left == goal:
                    solution = temp
                    break

        if (right:=(current_point[0]+1, current_point[1])) not in walls and is_valid(right, dimension):
            if right not in current_path:
                temp = current_path[:]
                temp.append(right)
                paths_to_check.append(temp)
                if right == goal:
                    solution = temp
                    break

    return solution
