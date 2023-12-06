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
        self.graph = defaultdict(set)
        self.V = 0
        self.E = 0

    def __iter__(self):
        for node in self.graph:
            yield node

    def add_edge(self, u, v):
        if u != v:
            self.graph[u].add(v)
            self.graph[v].add(u)
            self.V = max(u, v)
            self.E += 1
        else:
            pass

    def print_graph(self):
        for i in range(1, self.V + 1):
            print(i, self.graph[i])

    def create_random_graph(self, nodes: int = 20):
        import random

        for i in range(1, nodes + 1):
            for j in range(1, nodes + 1):
                if i != j:
                    if random.random() < 0.5:
                        self.add_edge(i, j)
        print(f"Total nodes: {nodes}")
        print(f"Total edges: {self.E}")
        print(f"V = {self.V}")
        print(f"E = {self.E}")

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
        print(f"E = {self.E}")

    @timer
    def brute_force_lgp(self):
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
    def dynamic_programming_lgp(self):
        """
        longest_path_increasing_nodes():
            L = Hash Map whose keys are nodes and values are paths (list of nodes)
            L[n-1] = [n-1] # base case
            longest_path = L[n-1]
            for s from n-2 to 0: # recursive case
                L[s] = [s]
                for each edge (s,v):
                    if v > s and length([s] + L[v]) > length(L[s]):
                        L[s] = [s] + L[v]
                if length(L[s]) > length(longest_path):
                    longest_path = L[s]
            return longest_path
        """

        L = defaultdict(list)
        L[self.V] = [self.V]
        longest_path = L[self.V]
        for s in range(self.V - 1, 0, -1):
            L[s] = [s]
            for v in self.graph[s]:
                if v > s and len([s] + L[v]) > len(L[s]):
                    L[s] = [s] + L[v]
            if len(L[s]) > len(longest_path):
                longest_path = L[s]

        print("Longest path:", longest_path)
        print("Length:", len(longest_path))
