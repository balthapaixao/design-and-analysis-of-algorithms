from collections import defaultdict
from itertools import permutations
import functools


import signal
import functools
import time


import resource  # Import the resource module


class TimeoutMemoryError(Exception):
    pass


def timeout_memory_handler(signum, frame):
    raise TimeoutMemoryError("Function execution timed out due to memory limit")


def timer_and_memory(timeout_seconds, memory_limit_mb):
    def decorator(func):
        @functools.wraps(func)
        def wrapper_timer_and_memory(*args, **kwargs):
            # Set the signal handler for timeout
            signal.signal(signal.SIGALRM, timeout_memory_handler)
            # Set the timer
            signal.alarm(timeout_seconds)

            # Set the signal handler for memory limit
            resource.setrlimit(
                resource.RLIMIT_AS,
                (memory_limit_mb * 1024 * 1024, resource.RLIM_INFINITY),
            )
            signal.signal(signal.SIGXCPU, timeout_memory_handler)
            signal.alarm(timeout_seconds)

            try:
                start_time = time.perf_counter()
                value = func(*args, **kwargs)
                end_time = time.perf_counter()
                run_time = end_time - start_time
                print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
                return value, run_time
            except (TimeoutError, TimeoutMemoryError) as e:
                print(
                    f"Function {func.__name__!r} timed out after {timeout_seconds} seconds due to {type(e).__name__}"
                )
                return None, None
            finally:
                signal.alarm(0)
                signal.signal(
                    signal.SIGXCPU, signal.SIG_DFL
                )  # Reset the signal handler for memory limit

        return wrapper_timer_and_memory

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

    @timer_and_memory(120, 14000)
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

    @timer_and_memory(120, 14000)
    def dynamic_programming_lgp(self):
        def dfs(node, dp, visited):
            visited[node] = True

            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, dp, visited)
                    dp[node] = max(dp[node], 1 + dp[neighbor])
                    print(f"dp[{node}] = {dp[node]}")

            visited[node] = False

        dp = [0] * (self.V + 1)
        for node in self:
            print(node)
            visited = [False] * (self.V + 1)
            dfs(node, dp, visited)

        print("Longest path Dynamic Programming:", dp)
        print("Length:", len(dp))

    @timer_and_memory(120, 14000)
    def dfs_lgp_all_nodes(self):
        max_paths = []
        for start_node in range(1, self.V + 1):
            seen = []
            path = [start_node]
            paths = self.DFS(self.graph, start_node, seen, path)
            longest_path = max(paths, key=len)

            max_paths.append(longest_path)

        max_path = max(max_paths, key=len)
        print("Longest path DFS:", max_path)
        print("Length:", len(max_path))

    def DFS(self, G, v, seen=None, path=None):
        if seen is None:
            seen = []
        if path is None:
            path = [v]

        seen.append(v)

        paths = []
        for t in G[v]:
            if t not in seen:
                t_path = path + [t]
                paths.append(tuple(t_path))
                paths.extend(self.DFS(G, t, seen[:], t_path))
        return paths
