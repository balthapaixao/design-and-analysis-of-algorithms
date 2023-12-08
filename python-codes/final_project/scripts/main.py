from utils import graph_utils
from glob import glob
import numpy as np

instances = glob("../data/*.mtx")

times_bf = []
times_dp = []


def run():
    MIN_NODES = 4
    MAX_NODES = 6

    for n in range(MIN_NODES, MAX_NODES + 1):
        graph = graph_utils.Graph()
        graph.create_random_graph(n)
        print(f"Instance with {graph.V} nodes and {graph.E} edges")
        graph.print_graph()

        time_elapsed = graph.brute_force_lgp()
        times_bf.append(time_elapsed[1])

        time_elapsed = graph.dynamic_programming_lgp()
        times_dp.append(time_elapsed[1])

    print(times_bf)
    print(times_dp)

    print(f"Average time for Brute Force: {np.mean(times_bf)}")
    print(f"Average time for Dynamic Programming: {np.mean(times_dp)}")


if __name__ == "__main__":
    run()
