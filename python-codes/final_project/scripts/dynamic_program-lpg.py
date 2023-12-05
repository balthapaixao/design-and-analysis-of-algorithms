# https://www.altcademy.com/blog/discover-the-longest-path-in-a-directed-acyclic-graph-solved/#solution-to-the-problem
from collections import defaultdict


# Perform a topological sort of the graph
def topological_sort(graph):
    visited = set()
    sorted_nodes = []

    def visit(node):
        if node not in visited:
            visited.add(node)
            for successor in graph[node]:
                visit(successor)
            sorted_nodes.append(node)

    for node in graph:
        visit(node)

    return sorted_nodes[::-1]


# Find the longest path in a directed acyclic graph
def longest_path(graph, weights):
    sorted_nodes = topological_sort(graph)
    dist = defaultdict(lambda: float("-inf"))
    dist[sorted_nodes[0]] = 0

    for node in sorted_nodes:
        for successor in graph[node]:
            dist[successor] = max(
                dist[successor], dist[node] + weights[(node, successor)]
            )

    return max(dist.values())


# Example graph
graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["E"], "D": [], "E": []}

weights = {("A", "B"): 2, ("A", "C"): 4, ("B", "D"): 3, ("B", "E"): 1, ("C", "E"): 4}

print(longest_path(graph, weights))  # Output: 8
