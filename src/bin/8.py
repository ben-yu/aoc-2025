import numpy as np
from scipy.spatial.distance import pdist, squareform
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in same circuit

        # Union by size
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        return True

    def get_circuit_sizes(self):
        circuits = defaultdict(int)
        for i in range(len(self.parent)):
            root = self.find(i)
            circuits[root] = self.size[root]
        return list(circuits.values())

    def num_circuits(self):
        return len(set(self.find(i) for i in range(len(self.parent))))


def part_one(filename='data/examples/08.txt', num_connections=10):
    coordinates = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line:
                pos = line.split(',')
                coordinates.append((int(pos[0]), int(pos[1]), int(pos[2])))

    n = len(coordinates)
    points = np.array(coordinates)

    # Calculate all pairwise distances
    condensed_distances = pdist(points, 'euclidean')

    # Get indices of k smallest distances
    k = min(len(condensed_distances), num_connections)
    smallest_indices = np.argpartition(condensed_distances, k-1)[:k]

    # Sort to get them in order
    smallest_indices = smallest_indices[np.argsort(condensed_distances[smallest_indices])]

    # Initialize union-find
    uf = UnionFind(n)

    # Connect the pairs in order
    connections_made = 0
    for idx in smallest_indices:
        if connections_made >= num_connections:
            break

        # Convert condensed index to pair indices
        # Formula: condensed[k] corresponds to (i, j) where
        # k = n*i - i*(i+1)/2 + j - i - 1
        # Reverse: find i, j from k
        i = 0
        while idx >= (n - i - 1):
            idx -= (n - i - 1)
            i += 1
        j = idx + i + 1

        uf.union(i, j)
        connections_made += 1

    # Get circuit sizes
    circuit_sizes = sorted(uf.get_circuit_sizes(), reverse=True)

    print(f"Circuit sizes: {circuit_sizes}")
    print(f"Three largest: {circuit_sizes[:3]}")

    # Multiply the three largest
    result = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]
    print(f"Result: {result}")
    return result


def part_two(filename='data/examples/08.txt'):
    coordinates = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line:
                pos = line.split(',')
                coordinates.append((int(pos[0]), int(pos[1]), int(pos[2])))

    n = len(coordinates)
    points = np.array(coordinates)

    # Calculate all pairwise distances
    condensed_distances = pdist(points, 'euclidean')

    # Get all distances sorted by size
    sorted_indices = np.argsort(condensed_distances)

    # Initialize union-find
    uf = UnionFind(n)

    # Connect pairs until we have one circuit
    last_i, last_j = None, None
    for idx in sorted_indices:
        # Convert condensed index to pair indices
        i = 0
        temp_idx = idx
        while temp_idx >= (n - i - 1):
            temp_idx -= (n - i - 1)
            i += 1
        j = temp_idx + i + 1

        # Try to union
        if uf.union(i, j):
            last_i, last_j = i, j

            # Check if we have one circuit
            if uf.num_circuits() == 1:
                break

    print(f"Last connection: {coordinates[last_i]} and {coordinates[last_j]}")
    result = coordinates[last_i][0] * coordinates[last_j][0]
    print(f"Product of X coordinates: {coordinates[last_i][0]} * {coordinates[last_j][0]} = {result}")
    return result


# Test with example
print("Example Part 1:")
part_one('data/examples/08.txt', 10)

print("\nPart 1:")
part_one('data/inputs/08.txt', 1000)

print("\nExample Part 2:")
part_two('data/examples/08.txt')

print("\nPart 2:")
part_two('data/inputs/08.txt')

