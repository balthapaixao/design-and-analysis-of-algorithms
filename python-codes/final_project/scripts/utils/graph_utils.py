from collections import defaultdict
from itertools import permutations
import functools


import signal
import functools
import time


class TimeoutError(Exception):
    pass


def timeout_handler(signum, frame):
    raise TimeoutError("Function execution timed out")


def timer(timeout_seconds):
    def decorator(func):
        @functools.wraps(func)
        def wrapper_timer(*args, **kwargs):
            # Set the signal handler
            signal.signal(signal.SIGALRM, timeout_handler)
            # Set the timer
            signal.alarm(timeout_seconds)

            try:
                start_time = time.perf_counter()
                value = func(*args, **kwargs)
                end_time = time.perf_counter()
                run_time = end_time - start_time
                print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
                return value, run_time
            except TimeoutError:
                print(
                    f"Function {func.__name__!r} timed out after {timeout_seconds} seconds"
                )
                return None, None
            finally:
                signal.alarm(0)

        return wrapper_timer

    return decorator


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

    @timer(120)
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
                max_path = path
                max_length = len(max_path)

        print("Longest path Brute Force:", max_path)
        print("Length:", max_length)

    @timer(120)
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

        for s in range(self.V - 1, 0, -1):
            for v in self.graph[s]:
                if v > s and len([s] + L[v]) > len(L[s]):
                    L[s] = [s] + L[v]

            if not L[s]:  # If L[s] is empty, there is no outgoing edge from s
                L[s] = [s]

        longest_path = max(L.values(), key=len)
        print("Longest path Dynamic Programming:", longest_path)
        print("Length:", len(longest_path))
