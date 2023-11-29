# Brute force algorithm for longest path in graphs

from itertools import permutations
import sys


def longest_path(graph, start, end):
    # Find all possible paths
    paths = [
        [start] + list(perm) + [end] for perm in permutations(graph - {start, end})
    ]
    # print(paths)
    # Find the longest path
    return max(paths, key=len)


def main():
    # Read the graph from the file
    graph = set()
    with open(sys.argv[1]) as f:
        for line in f:
            graph.add(tuple(line.strip().split(" ")))
    # print(graph)

    # Find the longest path
    path = longest_path(graph, "1", "n")
    # print(path)

    # Print the longest path
    print(" -> ".join(path))


if __name__ == "__main__":
    main()
