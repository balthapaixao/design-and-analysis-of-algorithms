from collections import defaultdict
import functools
import signal
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
                    if random.random() < 0.1:
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
        print(f"V = {self.V}")
        print(f"E = {self.E}")

    @timer_and_memory(1200, 10240)  # Set your desired timeout and memory limit
    def brute_force_lgp(self):
        max_length = 0
        max_path = None

        def dfs(node, path, length, visited):
            nonlocal max_length, max_path

            if length > max_length:
                max_length = length
                max_path = path[:]

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, path + [neighbor], length + 1, visited)
                    visited.remove(neighbor)

        for start_node in self.graph:
            visited = set([start_node])
            dfs(start_node, [start_node], 1, visited)


        print("Longest path Brute-Force Algorithm:", max_path)
        print("Length:", max_length)

        return max_length

    @timer_and_memory(1200, 10240)  # Set your desired timeout and memory limit
    def greedy_lgp(self):
        """Greedy algorithm for finding the longest path in a graph"""
        max_length = 0
        max_path = None

        def dfs(node, path, length, visited):
            """Depth-first search for finding the longest path in a graph"""
            nonlocal max_length, max_path

            if length > max_length:
                max_length = length
                max_path = path[:]

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, path + [neighbor], length + 1, visited)
                    visited.remove(neighbor)

        for start_node in self.graph:
            visited = set([start_node])
            dfs(start_node, [start_node], 1, visited)

        print("Longest path Greedy Algorithm:", max_path)
        print("Length:", max_length)

        return max_length