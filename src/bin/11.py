from collections import deque

def count_paths(graph, source, dest, required_nodes=None, path=None, memo=None):
    """Count all paths from source to dest in a DAG that contain required_nodes"""
    if path is None:
        path = set()
    if memo is None:
        memo = {}
    if required_nodes is None:
        required_nodes = set()

    # Add current node to path
    path = path | {source}

    # Base case: reached destination
    if source == dest:
        # Check if path contains all required nodes
        if required_nodes.issubset(path):
            return 1
        return 0

    # Create memo key with current node and which required nodes we've seen
    seen_required = frozenset(path & required_nodes)
    memo_key = (source, seen_required)

    # Return cached result if available
    if memo_key in memo:
        return memo[memo_key]

    # Count paths through all neighbors
    total_paths = 0
    for neighbor in graph.get(source, []):
        total_paths += count_paths(graph, neighbor, dest, required_nodes, path, memo)

    memo[memo_key] = total_paths
    return total_paths

def parse_input(filename):
    """Parse input file to get graph"""
    with open(filename) as f:
        graph = {}
        for line in f:
            line = line.strip()
            if line:
                src, dst = line.split(':')
                graph[src] = dst.strip().split(' ')
        graph["out"] = []
        return graph


def part_one(filename):
    """Find the number of paths from you to out in the input DAG"""
    graph = parse_input(filename)
#    print(graph)
    print(count_paths(graph, "you", "out"))

def part_two(filename):
    """Find the number of paths from svr to out with dac and fft in the input DAG"""
    graph = parse_input(filename)
#    print(graph)
    print(count_paths(graph, "svr", "out", required_nodes={"dac", "fft"}))

part_one("data/examples/11.txt")
part_one("data/inputs/11.txt")

part_two("data/examples/11_2.txt")
part_two("data/inputs/11.txt")

