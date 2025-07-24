import numpy as np


def cross_correlate(x: np.ndarray, y: np.ndarray) -> int:
    """
    Use the cross-correlation algorithm to determine if x and y share a monosynaptic connection.
    Details of the algorithm are at:
        - Perkel, 1967, Neuronal Spike Trains and Stochastic Point Processes: II. Simultaneous Spike Trains, https://doi.org/10.1016/S0006-3495(67)86597-4
        - Moore, 1970, Statistical Signs of Synaptic Interaction in Neurons, https://doi.org/10.1016/S0006-3495(70)86341-X
        - Kobayashi, 2025, Inference of monosynaptic connections from parallel spike trains: A review, https://doi.org/10.1016/j.neures.2024.07.006
    Inputs are binary binned spike trains. Moore et al. used 10ms bins, but other bin sizes can be used. If bin sizes are too large or small, a false positive or negative is more likely respectively.
    
    :param x: vector representing the spike train of neuron x
    :param y: vector representing the spike train of neuron y

    :return: a category as follows
        - -2: y inhibits x
        - -1: y excites x
        -  0: no relationship
        -  1: x excites y
        -  2: x inhibits y
    """
    # validate inputs
    assert isinstance(x, np.ndarray) and isinstance(y, np.ndarray), "x and y must both be of type np.ndarray"
    assert len(x.shape) == 1 and len(y.shape) == 1, "x and y must both be 1-dimensional vectors"
    assert len(x) == len(y), "x and y must have the same length"

    # calculate dot products that would fill a cross-correlogram
    products = dict()
    for i in range(1, len(x)+1):
        products[i] = float(np.dot(x[-i:], y[:i]))
        products[-i] = float(np.dot(y[-i:], x[:i]))

    # ### TODO...
        
    


    return 1

if __name__ == "__main__":
    cross_correlate(np.array([0, 2, 4, 6]), y = np.array([1, 3, 5, 7]))
