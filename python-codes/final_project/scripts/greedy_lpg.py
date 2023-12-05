from collections import defaultdict


def create_graph():
    return defaultdict(list)


def add_edge(graph, u, v, weight):
    graph[u].append((v, weight))


def topological_sort_util(graph, v, visited, stack):
    visited[v] = True

    for neighbor, _ in graph[v]:
        if not visited[neighbor]:
            topological_sort_util(graph, neighbor, visited, stack)

    stack.append(v)


def topological_sort(graph):
    visited = {v: False for v in graph}
    stack = []

    for v in graph:
        if not visited[v]:
            topological_sort_util(graph, v, visited, stack)

    return stack[::-1]


def longest_path_dag(graph, source):
    top_order = topological_sort(graph)
    dist = {v: float("-inf") for v in graph}
    dist[source] = 0

    for v in top_order:
        for neighbor, weight in graph[v]:
            dist[neighbor] = max(dist[neighbor], dist[v] + weight)

    return dist


# Exemplo de uso
graph = defaultdict(list)
add_edge(graph, "A", "B", 5)
add_edge(graph, "A", "C", 3)
add_edge(graph, "B", "D", 2)
add_edge(graph, "C", "D", 8)
add_edge(graph, "B", "E", 4)
add_edge(graph, "D", "E", 1)

source_vertex = "A"
result = longest_path_dag(graph, source_vertex)
print(f"Distâncias mais longas a partir de {source_vertex}: {result}")
