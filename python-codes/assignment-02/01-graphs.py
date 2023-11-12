import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def create_G() -> nx.Graph:
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

    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    return G


def find_non_adjacents(G: nx.Graph):
    non_adjacents = []
    for node in G.nodes:
        for other_node in G.nodes:
            if node != other_node and not G.has_edge(node, other_node):
                non_adjacents.append((node, other_node))
    return non_adjacents


def find_loops(G: nx.Graph):
    loops = []
    for node in G.nodes:
        if G.has_edge(node, node):
            loops.append(node)
    return loops


def degree_of_node(G: nx.Graph, node: int):
    return G.degree[node]


def find_isomorhism(G: nx.Graph):
    ...


def show_adjaency_matrix(G: nx.Graph) -> pd.DataFrame:
    nodes = list(G.nodes)
    nodes.sort()
    matrix = np.zeros((len(nodes), len(nodes)))
    for node in nodes:
        for other_node in nodes:
            if G.has_edge(node, other_node):
                matrix[node - 1][other_node - 1] = 1

    df = pd.DataFrame(matrix, index=nodes, columns=nodes)
    df = df.astype(int)

    return df


def plot_G(G: nx.Graph):
    sns.set()
    nx.draw(
        G,
        with_labels=True,
        font_weight="bold",
    )
    plt.savefig("./imgs/G.png")
    # plt.show()


def main():
    print("Question 1 - a)")
    G = create_G()
    plot_G(G)
    print()
    print("Question 1 - b)")
    non_adjacents = find_non_adjacents(G)
    print(f"Non adjacents nodes: {non_adjacents}")
    print(f"Loop: {find_loops(G)}")
    print(f"Degree of node 3: {degree_of_node(G, 3)}")
    print()
    print("Question 1 - c)")
    print(find_isomorhism(G))
    print()
    print("Question 1 - d)")
    df = show_adjaency_matrix(G)
    print(df)


if __name__ == "__main__":
    main()
