class Graph:
    def __init__(self, nodes: list, edges: list):
        self.nodes = nodes
        self.edges = edges
        self.graph = {}

    def create_graph(self):
        for node in self.nodes:
            self.graph[node] = set()

        for edge in self.edges:
            self.graph[edge[0]].add(edge[1])
            self.graph[edge[1]].add(edge[0])

    def dfs(self, node, visited=None):
        if visited is None:
            visited = set()

        visited.add(node)
        print(node, end=" -> ")

        for vizinho in self.graph[node]:
            if vizinho not in visited:
                self.dfs(vizinho, visited)


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    edges = [
        (1, 1),
        (1, 2),
        (2, 1),
        (2, 3),
        (3, 3),
        (3, 4),
        (4, 3),
        (4, 4),
        (5, 4),
        (5, 5),
    ]
    edges = [(1, 2), (1, 3), (3, 4), (3, 4), (4, 5), (5, 5)]

    G = Graph(nodes, edges)
    G.create_graph()
    print(G.graph)
    print(G.dfs(3))
