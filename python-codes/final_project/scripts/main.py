from utils import graph_utils
from glob import glob
import numpy as np
import logging

instances = glob("../data/*.mtx")

times_bf = []
times_greedy = []
diff = []

MIN_NODES = 2
MAX_NODES = 25

logfile = f"../logs/log_{MIN_NODES}_{MAX_NODES}.txt"
logging.basicConfig(filename=logfile, level=logging.DEBUG)

def run():

    for n in range(MIN_NODES, MAX_NODES + 1):
        graph = graph_utils.Graph()
        graph.create_random_graph(n)

        logging.info(f"Instance with {graph.V} nodes and {graph.E} edges")
        logging.info(graph.print_graph())

        max_path_bf, time_elapsed_bf = graph.brute_force_longest_path()
        max_path_greedy, time_elapsed_greedy = graph.greedy_lgp()
        if max_path_bf is None:
            max_path_bf = []
        if max_path_greedy is None:
            max_path_greedy = []

        times_bf.append(time_elapsed_bf)
        times_greedy.append(time_elapsed_greedy)
        diff.append(len(max_path_bf) - len(max_path_greedy))

        logging.info(
            f"Brute Force Algorithm: {max_path_bf} in {time_elapsed_bf} seconds"
        )
        logging.info(
            f"Greedy Algorithm:      {max_path_greedy} in {time_elapsed_greedy} seconds"
        )
        print(
            f"Difference in path length: {len(max_path_bf) - len(max_path_greedy)} nodes")
        logging.info("----------------------------------------------------------")


    logging.info(f"Average time for Brute Force Algorithm:  {np.mean(times_bf)}")
    logging.info(f"Average time for Greedy Algorithm:       {np.mean(times_greedy)}")


    print(f"Average time for Brute Force Algorithm:  {np.mean(times_bf)}")
    print(f"Average time for Greedy Algorithm:       {np.mean(times_greedy)}")


if __name__ == "__main__":
    run()
