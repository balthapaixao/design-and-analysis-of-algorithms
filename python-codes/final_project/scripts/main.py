from utils import graph_utils
from glob import glob
import numpy as np

instances = glob("../data/*.mtx")

times_bf = []
times_bf_lgp = []
times_bf_lgp_pruning = []

instances = ['../data/teste_50.mtx']

for n in range(5, 16):
    graph= graph_utils.Graph()
    graph.create_random_graph(n)
    print(f"Instance with {graph.V} nodes and {graph.E} edges")
    graph.print_graph()
    print()
    graph.brute_force_lgp()
    print()
    graph.brute_force_lgp()
    print()
    graph.brute_force_lgp()
