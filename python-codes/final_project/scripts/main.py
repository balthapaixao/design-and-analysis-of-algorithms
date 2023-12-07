from utils import graph_utils
from glob import glob

# import numpy as np

instances = glob("../data/*.mtx")

times_bf = []
times_dp = []


def run():
    MAX_NODES = 4

    for n in range(4, MAX_NODES + 1):
        graph = graph_utils.Graph()
        graph.create_random_graph(n)
        print(f"Instance with {graph.V} nodes and {graph.E} edges")
        graph.print_graph()

        graph.brute_force_lgp()
        graph.dynamic_programming_lgp()

    print(times_bf)
    print(times_dp)


if __name__ == "__main__":
    run()
