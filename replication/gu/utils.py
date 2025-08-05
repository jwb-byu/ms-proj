from typing import Callable, Optional

import matplotlib.pyplot as plt
import networkx as nx  # type: ignore
import numpy as np
from matplotlib.axes import Axes


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
            adj[i, j] = compare(arr[i], arr[j])
            adj[j, i] = compare(arr[j], arr[i])
    
    return adj


def show_graph(G: nx.Graph, fig_size: tuple[float, float] = (15, 10), title: Optional[str] = None, layout_fun_: Callable = nx.spring_layout) -> None:
    """
    Plot a graph. Adapted from CS 575 class exercises, homeworks, projects

    :param G: the graph
    :param title: title
    :param layout_fun_: a layout function. options include:
        - nx.spring_layout
        - nx.circular_layout
        - nx.nx_pydot.pydot_layout
        - nx.nx_pydot.graphviz_layout
        - see https://networkx.org/documentation/stable/reference/drawing.html#module-networkx.drawing.layout
    """
    node_positions: dict[int, tuple[float,float]] = layout_fun_(G)
    
    plt.clf()
    plt.figure(figsize=fig_size)
    ax: Axes = plt.gca()
    
    if title:
        ax.set_title(title)
    
    nx.draw(G, 
        node_positions, 
        node_color = ['y' for node in G.nodes], 
        with_labels = True, 
        node_size = 300, 
        alpha=0.8)
    plt.show()
