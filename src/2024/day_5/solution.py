from utilities import load_file, timing_val
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

def parse_input(task_input: list[str]):
    """
    For every number, maintain the set of numbers that follow and preced
    """
    parts = ''.join(task_input).split('\n\n')
    # print(parts)
    following = dict()
    preceding = dict()
    # parse the rules
    for rule in parts[0].split('\n'):
        numbers = [int(number) for number in rule.split('|')]
        if not numbers[0] in following:
            following[numbers[0]] = set()

        following[numbers[0]].add(numbers[1])
        
        if not numbers[1] in preceding:
            preceding[numbers[1]] = set()

        preceding[numbers[1]].add(numbers[0])
    # print(preceding)

    # parse the orders
    orders_temp = parts[1].split('\n')
    orders=[]
    for order in orders_temp: 
        # print(order.split(','))
        orders.append([int(number) for number in order.split(',')])
    return following, preceding, orders

def order_is_correct(following, preceding, order):
    """
    For each element check whether the slice of preceding and following elements is a subset 
    of the set of preceding and following elements
    """
    # print(order)
    for i in range(len(order)):
        current_number = order[i]
        # print(current_number)
        test_following = set(order[i+1:])
        test_preceding = set(order[:i])
        # print(test_following, test_preceding)
        if not test_following.issubset(following.get(current_number, set())):
            return 0
        
        if not test_preceding.issubset(preceding.get(current_number, set())):
            return 0

    return order[int((len(order)-1)/2)]

@timing_val
def part_01(task_input: list[str]) -> int:
    following, preceding, orders = parse_input(task_input)
    correctness = list(map(lambda x: order_is_correct(following, preceding, x), orders))
    # print(correctness)
    return sum(correctness)

def fix_order(following, preceding, order):
    """
    As long as the order is not correct, go through the elements and check which element is followed by elements
    it should not be followed by. Get maximum index position of these elements and move number after it.
    """
    # print(order)
    while not order_is_correct(following, preceding, order):
        for i in range(len(order)):
            current_number = order[i]
            test_following = set(order[i+1:])
            # test_preceding = set(order[:i])
            diff_follow = test_following.difference(following.get(current_number, set()))
            if diff_follow:
                last_postion = max([order.index(number) for number in diff_follow])
                # print(last_postion)
                order.pop(i)
                order.insert(last_postion,current_number)
    # print(order)
    return order[int((len(order)-1)/2)]


@timing_val
def part_02(task_input: list[str]) -> int:
    result = 0
    following, preceding, orders = parse_input(task_input)
    for order in orders:
        if not order_is_correct(following, preceding, order):
            # print(order)
            result+=fix_order(following,preceding,order)
    # put logic here
    return result

def main():
    result_part1 = part_01(load_file(CURRENT_FOLDER / 'input'))
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(load_file(CURRENT_FOLDER / 'input'))
    print(f"Outcome of part 2 is: {result_part2}.")

if __name__ == '__main__':
    main()

def test_part1():
    content = load_file(CURRENT_FOLDER / 'tests/input')
    result = part_01(content)
    # put test result here
    assert result == 143

def test_part2():
    content = load_file(CURRENT_FOLDER / 'tests/input')
    result = part_02(content)
    # put test result here
    assert result == 123
