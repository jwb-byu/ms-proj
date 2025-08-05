from typing import Callable

import numpy as np


def adjacency_matrix_from_pairwise(arr: np.ndarray, compare: Callable) -> np.ndarray:
    """
    Given a clusters-by-time-bin matrix, use a pairwise spike comparison function to create an adjacency matrix representing a partial functional connectome.
    It is assumed that clusters more than 100 rows apart in the matrix are not associated (this assumption may decrease accuracy, but is acceptable for our purposes).
    
    :param arr: a 2D clusters-by-time-bin matrix (rows are clusters)
    :param compare: a function that accepts two spike trains and returns a connectedness score

    :return: an adjacency matrix
    """
    assert isinstance(arr, np.ndarray) and len(arr.shape)==2,  "input array must be a two dimensional np.ndarray"

    adj = np.zeros((arr.shape[0], arr.shape[0]), dtype=np.int8)
    for i, _ in enumerate(arr):
        for j in range(i+1, min(i+100, len(arr))):
            score = compare(arr[i], arr[j])
            adj[i, j] = score
            adj[j, i] = score
    
    return adj
