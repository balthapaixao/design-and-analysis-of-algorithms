"""4  –  Quando  trabalhamos  com  grafos  admitimos  que  algumas  operações  básicas  já  estejam 
implementadas.  Então  nossa  primeira  tarefa  é  implementar  as  seguintes  operações  básicas 
tanto para uma representação por matriz de adjacências quanto para lista de adjacências: 
a) Definição do Grafo 
b) Adição de Arestas 
c) Determinação de vizinhos de um dado vértice 
d) Teste de vizinhança entre par de vértices 
e) Remoção de arestas """


class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def add_edge(self, node1: int, node2: int):
        if node1 not in self.graph:
            self.graph[node1] = set()
        if node2 not in self.graph:
            self.graph[node2] = set()

        self.graph[node1].add(node2)
        self.graph[node2].add(node1)

    def get_neighbors(self, node: int):
        return self.graph[node]

    def is_neighbor(self, node1: int, node2: int):
        return node2 in self.graph[node1]

    def remove_edge(self, node1: int, node2: int):
        self.graph[node1].remove(node2)
        self.graph[node2].remove(node1)

    def graph_definition(self, nodes: list, edges: list):
        self.nodes = nodes
        self.edges = edges


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

    G = Graph()
    G.graph_definition(nodes, edges)
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(3, 4)
    G.add_edge(3, 4)
    G.add_edge(4, 5)
    G.add_edge(5, 5)
    print(G.graph)
    print(G.get_neighbors(1))
    print(G.is_neighbor(1, 2))
    G.remove_edge(1, 2)
    print(G.graph)
    print(G.is_neighbor(1, 2))
