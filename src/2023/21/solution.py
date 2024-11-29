from utilities import load_file, timing_val

def parse_input(task_input: list[str]):
    parsed_input = []
    for line in task_input:
        parsed_line = []
        print([0 if char == '#' else 1 for char in line.strip()])


def draw_map(raw_map: list[str]):
    pass

class Map:
    def __init__(self, raw_map):
        self.raw_map = raw_map
        self.known_points = dict()

    def is_accessible(self, point: tuple):
        if point[0] < 0 or point[0] > 130 or point[1] < 0 or point[1] > 130:
            return False
        return not self.raw_map[point[1]][point[0]] == '#'

    def draw(self, points: dict, current_step: int):
        for line_number, line in enumerate(self.raw_map):
            for char_number, char in enumerate(line.strip()):
                if char == '.' and (char_number, line_number) in points and (current_step % 2 == points[(char_number, line_number)]):
                    char = 'O'
                print(char, end="")
            print("")

    def find_possible_points(self, point):
        points_to_visit = []
        point_left = (point[0] - 1, point[1])
        point_right = (point[0] + 1, point[1])
        point_down = (point[0], point[1] + 1)
        point_up = (point[0], point[1] - 1)
        if self.is_accessible(point_left) and point_left[0] > -1:
            points_to_visit.append(point_left)
        if self.is_accessible(point_right) and point_right[0] < 131:
            points_to_visit.append(point_right)
        if self.is_accessible(point_down) and point_down[1] < 131:
            points_to_visit.append(point_down)
        if self.is_accessible(point_up) and point_up[1] > -1:
            points_to_visit.append(point_up)

        return points_to_visit

@timing_val
def part_01(task_input: list[str]) -> int:
    result = 0
    field = Map(task_input)
    points_to_check = [(65, 65)]
    visited = {}
    number_of_steps = 1
    # field.draw()
    for step in range(0, number_of_steps + 1):
        next_round = []
        for point in points_to_check:
            visited[point] = step % 2
            new_points = [new_point for new_point in field.find_possible_points(point) if new_point not in visited]
            next_round.extend(new_points)
        points_to_check = list(set(next_round))
        # print(f"new points {points_to_check}")
        # print(f"visited points: {visited}")

    field.draw(visited, number_of_steps)
            
    return result


@timing_val
def part_02(task_input: list[str]) -> int:
    result = 0
    # put logic here
    return result


if __name__ == '__main__':
    result_part1 = part_01(load_file('./input'))
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(load_file('./input'))
    print(f"Outcome of part 2 is: {result_part2}.")

def test_part1():
    content = load_file('./tests/input')
    result = part_01(content)
    # put test result here
    assert result == 0

def test_part2():
    content = load_file('./tests/input')
    result = part_02(content)
    # put test result here
    assert result == 0
