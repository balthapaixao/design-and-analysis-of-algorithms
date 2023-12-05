from utils import graph_utils
from glob import glob
import numpy as np

graph = graph_utils.Graph()
graph.read_from_file("../data/494_bus.mtx")

# graph.print_graph()

instances = glob("../data/*.mtx")

times_bf = []
times_bf_lgp = []
times_bf_lgp_pruning = []

for instance in instances:
    graph = graph_utils.Graph()
    graph.read_from_file(instance)
    print(f"File: {instance}")
    print()
    graph.brute_force()
    print()
    graph.brute_force_lgp()
    print()
    graph.brute_force_lgp_with_pruning()
