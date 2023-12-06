from utils import graph_utils
from glob import glob
import numpy as np

instances = glob("../data/*.mtx")

times_bf = []
times_dp = []


def run():
    MAX_NODES = 20

    for n in range(5, MAX_NODES):
        graph = graph_utils.Graph()
        graph.create_random_graph(n)
        print(f"Instance with {graph.V} nodes and {graph.E} edges")
        graph.print_graph()

        try:
            graph.brute_force_lgp()
            times_bf.append(graph.brute_force_lgp.elapsed)
        except:
            times_bf.append(np.nan)
            print("Error")

        try:
            graph.dynamic_programming_lgp()
            times_dp.append(graph.dynamic_programming_lgp.elapsed)
        except:
            times_dp.append(np.nan)
            print("Error")

    print(times_bf)
    print(times_dp)


if __name__ == "__main__":
    run()
