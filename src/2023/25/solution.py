import networkx as nx
import random as rd
from src.utilities import load_file, timing_val

def generate_graph(task_input: list[str]) -> nx.Graph:
    G = nx.Graph()
    edge_list = []
    for line in task_input:
        parts = line.strip().split()
        head = parts.pop(0).removesuffix(':')
        # print(head, parts)
        for part in parts:
            edge_list.append((head, part))
    G.add_edges_from(edge_list)
    return G

@timing_val
def part_01(task_input: list[str]) -> int:
    result = 0
    G = generate_graph(task_input)
    list_of_nodes = list(G.nodes)
    # put logic here
    remaining_nodes = set([tuple(sorted(edge)) for edge in G.edges])
    sample_in_different_components = []
    while len(remaining_nodes) > 3:
        sample = rd.sample(list_of_nodes,k = 2)
        temp_G = G.copy()
        if G.has_edge(sample[0], sample[1]):
            continue
        # print(f"Current sample is: {sample}")
        edges_to_keep = set()
        for i in range(0, 4):
            try:
                path = nx.shortest_path(temp_G, sample[0], sample[1])
            except nx.NetworkXNoPath:
                if i == 3:
                    # print(f"Keeping nodes {edges_to_keep}")
                    remaining_nodes = remaining_nodes.intersection(edges_to_keep)
                    # print(f"Edges to keep: {remaining_nodes}")
                    sample_in_different_components = sample
                break
            else:
                intermediary_steps = set([tuple(sorted(edge)) for edge in zip(path[0:-1], path[1:]) ])
                # print(intermediary_steps)
                edges_to_keep= edges_to_keep.union(intermediary_steps)
                temp_G.remove_edges_from(intermediary_steps)
                # print(len(temp_G.edges))

    print(remaining_nodes)
    G.remove_edges_from(remaining_nodes)
    reachable1 = nx.shortest_path(G, sample_in_different_components[0])
    reachable2 = nx.shortest_path(G, sample_in_different_components[1])

    result = len(reachable1) * len(reachable2)
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
    assert result == 54

def test_part2():
    content = load_file('./tests/input')
    result = part_02(content)
    # put test result here
    assert result == 0
