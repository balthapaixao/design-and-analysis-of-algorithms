from collections import defaultdict
from itertools import permutations
import functools


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        import time

        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.V = 0
        self.E = 0

    def __iter__(self):
        for node in self.graph:
            yield node

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.V = max(u, v)
        self.E += 1

    def print_graph(self):
        for i in range(1, self.V + 1):
            print(i, self.graph[i])

    def read_from_file(self, file_name):
        """Reads the graph from a file"""
        get_total_nodes = True
        with open(file_name, "r") as f:
            for line in f:
                if get_total_nodes:
                    n_nodes, n_edges = [int(x) for x in line.split()]
                    get_total_nodes = False
                else:
                    u, v = [int(x) for x in line.split()]
                    self.add_edge(u, v)
        print(f"Total nodes: {n_nodes}")
        print(f"Total edges: {n_edges}")
        print(f"V = {self.V}")

        assert n_nodes == self.V
        assert n_edges == self.E

    @timer
    def brute_force_lgp(self):
        """Brute force algorithm for longest path in graphs"""
        all_paths = list(permutations(range(1, self.V + 1)))

        max_length = 0
        max_path = None
        for path in all_paths:
            length = 0
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                if v in self.graph[u]:
                    length += 1
                else:
                    break
            if length > max_length:
                max_length = length
                max_path = path

        print("Longest path:", max_path)
        print("Length:", max_length)

    @timer
    def greedy_lgp(self):
        """Greedy algorithm for longest path in graphs"""
        visited = set()
        path = []

        def dfs(node):
            nonlocal path
            visited.add(node)
            path.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for node in self:
            if node not in visited:
                path = []
                dfs(node)

        print("Longest path (greedy):", path)
        print("Length:", len(path) - 1)

    @timer
    def dynamic_programming_lgp(self):
        """Dynamic programming algorithm for longest path in graphs"""

        def longest_path_length(node, memo):
            if node in memo:
                return memo[node]

            max_length = 0
            for neighbor in self.graph[node]:
                max_length = max(max_length, 1 + longest_path_length(neighbor, memo))

            memo[node] = max_length
            return max_length

        start_node = next(iter(self))
        memo = {}
        max_length = longest_path_length(start_node, memo)

        path = [start_node]
        while len(path) < max_length + 1:
            neighbors = self.graph[path[-1]]
            next_node = max(neighbors, key=lambda x: memo[x])
            path.append(next_node)

        print("Longest path (dynamic programming):", path)
        print("Length:", len(path) - 1)
