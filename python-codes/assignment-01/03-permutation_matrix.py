import numpy as np


def is_permutation_matrix(matrix: np.array) -> None:
    """Constraints matrix nxn - n < 100"""
    dim = len(matrix)
    one_col_counts = np.zeros(dim)
    one_row_counts = np.zeros(dim)
    for i in range(dim):
        for j in range(dim):
            if (matrix[i, j] > 1) or (matrix[i, j] < 0):
                break
            elif matrix[i, j] == 1:
                one_row_counts[i] += 1
                one_col_counts[j] += 1
            else:
                continue
    if (one_col_counts == one_row_counts).all():
        print("Is permutation matrix")
    else:
        print("Is not permutation matrix")


if __name__ == "__main__":
    matrix = np.array([[0, 3, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    is_permutation_matrix(matrix=matrix)
