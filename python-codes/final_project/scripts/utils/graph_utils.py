from collections import defaultdict
import functools
import signal
import time
import resource  # Import the resource module

from collections import deque, defaultdict

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
                signal.signal(signal.SIGXCPU, signal.SIG_DFL)

        return wrapper_timer_and_memory

    return decorator


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.V = 0
        self.E = 0

    def __iter__(self):
        for node in self.graph:
            yield node

    def add_edge(self, u, v):
        if u != v:
            if v not in self.graph[u]:
                self.graph[u].append(v)

            if u not in self.graph[v]:
                self.graph[v].append(u)
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
                    if random.random() < 0.2:
                        self.add_edge(i, j)
        print(f"Total nodes: {nodes}")
        print(f"Total edges: {self.E}")

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

    def get_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]

        paths = []
        for neighbor in self.graph[start]:
            if neighbor not in path:
                new_paths = self.get_all_paths(neighbor, end, path)
                paths.extend(new_paths)

        return paths

    @timer_and_memory(1200, 10240)
    def brute_force_longest_path(self):
        max_path_length = 0
        max_path = []

        # Gera todas as combinações possíveis de caminhos
        for start_node in self.graph:
            for end_node in self.graph:
                if start_node != end_node:
                    paths = self.get_all_paths(start_node, end_node)
                    for path in paths:
                        path_length = len(path)
                        if path_length > max_path_length:
                            max_path_length = path_length
                            max_path = path

        print("Longest path Brute Force:", max_path)
        print("Length:", max_path_length)

        return max_path