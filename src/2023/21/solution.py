from utilities import load_file, timing_val

MULTIPLIER = 1


# Solution thoughts
# 26501365 = 65 + 202300 * 131
# After 65 steps: The middle field is populated (3759)
# After 65 + 1 * 131 steps
    # * center is fully populated
    # * 131 steps where done in fields where it entered along the middle axis
    # * 65 steps where done in fields where it entered in the corner
    # 1 fully, 4 pyramids, 4 wedges
# after 65 + 2 * 131 steps
# after n steps:
# we got the 4 "spearheads", we got n times field starting in each corner going for (dim - 1) / 2 number_of_steps (small wedges)
# we got n-1 times field starting in each corner going for dim + (dim -1) / 2 = (3 * dim - 1) / 2 (big wedges)
# we got n ^ 2 populated fields in state 0 and (n-1)^2 fields in state 1

 

class Map:
    def __init__(self, raw_map):
        self.raw_map = [MULTIPLIER * line.strip() for line in raw_map] * MULTIPLIER
        self.dimensions = len(raw_map)
        self.known_points = dict()

    def is_accessible(self, point: tuple):
        return not self.raw_map[point[1] % self.dimensions][point[0] % self.dimensions] == '#'

    def is_in_field(self, point: tuple):
        return point[0] >= 0 and point[1] >= 0 and point[0] < self.dimensions and point[1] < self.dimensions

    def count_points_in_field(self, points: dict[tuple, int], number_of_steps) -> int:
        active_fields = 0
        for point, value in points.items():
            if value == number_of_steps % 2 and self.is_in_field(point):
                active_fields += 1
        return active_fields


    def draw(self, points: dict, current_step: int):
        for line_number, line in enumerate(self.raw_map):
            for char_number, char in enumerate(line.strip()):
                if char == '.' and (char_number, line_number) in points and (current_step % 2 == points[(char_number, line_number)]):
                    char = 'O'
                print(char, end="")
                if char_number % self.dimensions == self.dimensions - 1:
                    print(" ", end="")
            print("")
            if line_number % self.dimensions == self.dimensions - 1:
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
    # set starting point
    # points_to_check = [(65, 65)]
    # points_to_check = [(-1, 65)]
    points_to_check = [(-1, 0)]
    visited = {}
    number_of_steps = 65
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
    active_fields = 0
    for _, value in visited.items():
        if value == number_of_steps % 2:
            active_fields += 1

    print(f"Number of active points: {active_fields}")
    return result


def visit_points(field, points_to_check, number_of_steps):
    visited = {}
    for step in range(0, number_of_steps + 1):
        next_round = []
        for point in points_to_check:
            visited[point] = step % 2
            new_points = [new_point for new_point in field.find_possible_points(point) if new_point not in visited]
            next_round.extend(new_points)
        points_to_check = list(set(next_round))

    return visited


@timing_val
def part_02(task_input: list[str]) -> int:
    # general idea is described in the header comment
    result = 0
    # put logic here
    field = Map(task_input)
    # set starting point
    starting_point = int((field.dimensions * MULTIPLIER -1 ) / 2)
    points_to_check = [(starting_point, starting_point)]
    iterations = 202300
    # number_of_steps = int((field.dimensions - 1) / 2) + iterations * field.dimensions
    # visited = visit_points(field, points_to_check, number_of_steps)

    # points in "spearheads"
    middle_lane = int((field.dimensions + 1) / 2) - 1
    spearhead_steps = field.dimensions
    draw_details = False
    spearheads_left = visit_points(field, [(-1, middle_lane)], spearhead_steps)
    number_spearheads_left = field.count_points_in_field(spearheads_left, spearhead_steps)
    if draw_details:
        field.draw(spearheads_left, spearhead_steps)
    print(f"spearheads_left {number_spearheads_left}")
    spearheads_right = visit_points(field, [(field.dimensions, middle_lane)], spearhead_steps)
    number_spearheads_right = field.count_points_in_field(spearheads_right, spearhead_steps)
    if draw_details:
        field.draw(spearheads_right, spearhead_steps)
    print(f"spearheads_right {number_spearheads_right}")
    spearheads_up = visit_points(field, [(middle_lane, field.dimensions)], spearhead_steps)
    number_spearheads_up = field.count_points_in_field(spearheads_up, spearhead_steps)
    if draw_details:
        field.draw(spearheads_up, spearhead_steps)
    print(f"spearheads_up {number_spearheads_up}")
    spearheads_down = visit_points(field, [(middle_lane, -1)], spearhead_steps)
    number_spearheads_down = field.count_points_in_field(spearheads_down, spearhead_steps)
    if draw_details:
        field.draw(spearheads_down, spearhead_steps)
    print(f"spearheads_down {number_spearheads_down}")

    # points in state 0
    state_zero = visit_points(field, [(middle_lane, middle_lane)], field.dimensions + 1)
    number_state_zero = field.count_points_in_field(state_zero, field.dimensions + 1)
    if draw_details:
        field.draw(state_zero, field.dimensions+1)
    print(f"state_zero {number_state_zero}")

    state_one = visit_points(field, [(middle_lane, middle_lane)], field.dimensions)
    number_state_one = field.count_points_in_field(state_one, field.dimensions)
    if draw_details:
        field.draw(state_one, field.dimensions)
    print(f"state_one {number_state_one}")

    # wedges
    wedge_big_steps = int((3 * field.dimensions -1) / 2)

    wedge_left_low_big = visit_points(field, [(0, field.dimensions)], wedge_big_steps)
    if draw_details:
        field.draw(wedge_left_low_big, wedge_big_steps)
    number_wedge_llb = field.count_points_in_field(wedge_left_low_big, wedge_big_steps)
    print(f"wllb {number_wedge_llb}")

    wedge_left_high_big = visit_points(field, [(0, -1)], wedge_big_steps)
    if draw_details:
        field.draw(wedge_left_high_big, wedge_big_steps)
    number_wedge_lhb = field.count_points_in_field(wedge_left_high_big, wedge_big_steps)
    print(f"wlhb {number_wedge_lhb}")

    wedge_right_low_big = visit_points(field, [(field.dimensions-1, field.dimensions)], wedge_big_steps)
    if draw_details:
        field.draw(wedge_right_low_big, wedge_big_steps)
    number_wedge_rlb = field.count_points_in_field(wedge_right_low_big, wedge_big_steps)
    print(f"wrlb {number_wedge_rlb}")

    wedge_right_high_big = visit_points(field, [(field.dimensions, 0)], wedge_big_steps)
    if draw_details:
        field.draw(wedge_right_high_big, wedge_big_steps)
    number_wedge_rhb = field.count_points_in_field(wedge_right_high_big, wedge_big_steps)
    print(f"wrhb {number_wedge_rhb}")

    wedge_small_steps = int((field.dimensions -1) / 2)

    wedge_left_low_small = visit_points(field, [(0, field.dimensions)], wedge_small_steps)
    if draw_details:
        field.draw(wedge_left_low_small, wedge_small_steps)
    number_wedge_lls = field.count_points_in_field(wedge_left_low_small, wedge_small_steps)
    print(f"wllb {number_wedge_lls}")

    wedge_left_high_small = visit_points(field, [(0, -1)], wedge_small_steps)
    if draw_details:
        field.draw(wedge_left_high_small, wedge_small_steps)
    number_wedge_lhs = field.count_points_in_field(wedge_left_high_small, wedge_small_steps)
    print(f"wlhb {number_wedge_lhs}")

    wedge_right_low_small = visit_points(field, [(field.dimensions-1, field.dimensions)], wedge_small_steps)
    if draw_details:
        field.draw(wedge_right_low_small, wedge_small_steps)
    number_wedge_rls = field.count_points_in_field(wedge_right_low_small, wedge_small_steps)
    print(f"wrlb {number_wedge_rls}")

    wedge_right_high_small = visit_points(field, [(field.dimensions, 0)], wedge_small_steps)
    if draw_details:
        field.draw(wedge_right_high_small, wedge_small_steps)
    number_wedge_rhs = field.count_points_in_field(wedge_right_high_small, wedge_small_steps)
    print(f"wrhb {number_wedge_rhs}")

    total_number_active = (
        number_spearheads_left + number_spearheads_right + number_spearheads_up + number_spearheads_down +
        (iterations - 1) * (number_wedge_llb + number_wedge_lhb + number_wedge_rhb + number_wedge_rlb) +
        iterations * (number_wedge_rhs + number_wedge_rls + number_wedge_lls + number_wedge_lhs) +
        iterations * iterations * number_state_zero + 
        (iterations -1) * (iterations - 1) * number_state_one
    )

    print(f"Calculated_total_number {total_number_active}")

    #####
    # field.draw(visited, number_of_steps)
    #
    # active_fields = 0
    # for _, value in visited.items():
    #     if value == number_of_steps % 2:
    

    # print(f"Number of active points: {active_fields}")
    return result


if __name__ == '__main__':
    # part1 was not properly implemented here, instead I used it to visualize what is going on
    # result_part1 = part_01(load_file('./input'))
    # print(f"Outcome of part 1 is: {result_part1}.")
    # result_part2 = part_02(load_file('./tests/input'))
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
