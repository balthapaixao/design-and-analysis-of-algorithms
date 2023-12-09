from utils import graph_utils
from glob import glob
import numpy as np
import logging

instances = glob("../data/*.mtx")
logfile = "../logs/log_2.txt"
logging.basicConfig(filename=logfile, level=logging.DEBUG)
times_bf = []
times_greedy = []


def run():
    MIN_NODES = 10
    MAX_NODES = 10

    for n in range(MIN_NODES, MAX_NODES + 1):
        graph = graph_utils.Graph()
        graph.create_random_graph(n)
        print(f"Instance with {graph.V} nodes and {graph.E} edges")
        logging.info(f"Instance with {graph.V} nodes and {graph.E} edges")
        logging.info(graph.print_graph())
        max_length_bf, time_elapsed_bf = graph.brute_force_longest_path()
        times_bf.append(time_elapsed_bf)

        max_length_greedy, time_elapsed_greedy = graph.greedy_lgp()
        times_greedy.append(time_elapsed_greedy)
        logging.info(
            f"Brute Force Algorithm: {max_length_bf} in {time_elapsed_bf} seconds"
        )
        logging.info(
            f"Greedy Algorithm:      {max_length_greedy} in {time_elapsed_greedy} seconds"
        )
        logging.info("----------------------------------------------------------")
    logging.info(f"Average time for Brute Force Algorithm:  {np.mean(times_bf)}")
    logging.info(f"Average time for Greedy Algorithm:       {np.mean(times_greedy)}")

    print(f"Average time for Brute Force Algorithm:  {np.mean(times_bf)}")
    print(f"Average time for Greedy Algorithm:       {np.mean(times_greedy)}")

    assert max_length_bf == max_length_greedy


if __name__ == "__main__":
    run()
