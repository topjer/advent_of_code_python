from utilities import load_file, load_file_single, timing_val
from collections import defaultdict
from pathlib import Path
CURRENT_FOLDER = Path(__file__).parent.resolve()

def part_01(graph) -> int:
    result = 0
    triplets = set()
    for p1, value in graph.items():
        for p2 in value:
            cycles = value.intersection(graph[p2])
            for p3 in cycles:
                if any(p.startswith('t') for p in [p1,p2,p3]):
                    temp = [p1,p2,p3]
                    temp.sort()
                    temp = tuple(temp)
                    triplets.add(temp)
    # put logic here
    return len(triplets)

def bron_kerbosch(R: set, P: set, X:set , graph, results):
    # print(R,P,X)
    if len(P) == 0 and len(X) == 0:
        # print(R)
        if len(R) > 2:
            results.append(R)
        return True

    while P:
    # for vertex in P:
        vertex = P.pop()
        # print(vertex)
        bron_kerbosch(R.union({vertex}), P.intersection(graph[vertex]), X.intersection(graph[vertex]), graph, results)
        X = X.union({vertex})


def part_02(graph) -> str:
    result = 0
    results = []
    bron_kerbosch(set(), set(graph.keys()), set(), graph, results)
    results.sort(key=len)
    temp = list(results.pop())
    temp.sort()
    return ','.join(temp)

def parse_input(task_input):
    graph = defaultdict(set)
    for line in task_input.strip().split('\n'):
        p1, p2 = line.split('-')
        graph[p1].add(p2)
        graph[p2].add(p1)
    return graph

@timing_val
def main():
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
    assert result == 7

def test_part2():
    content = parse_input(load_file_single(CURRENT_FOLDER / 'tests/test_input'))
    result = part_02(content)
    # put test result here
    assert result == 'co,de,ka,ta'
