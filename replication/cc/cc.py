import numpy as np


def find_outlier_limits(x: list[float]) -> tuple[float, float]:
    """
    given a list of floats, find the upper and lower limits that could be considered as outliers
    an outlier is defined as a value outside 3 standard deviations and 1.5xIQR outside the IQR

    :param x: the distribution

    :return: lower and upper limits respectively
    """
    percentiles = np.percentile(x, np.array([25, 75]))
    iqr = percentiles[1]-percentiles[0]
    mean = float(np.mean(x))
    sd = float(np.std(x))
    upper_limit = max([percentiles[1]+1.5*iqr, mean+(3*sd)])
    lower_limit = min([percentiles[0]-1.5*iqr, mean-(3*sd)])
    return lower_limit, upper_limit


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
        - 1: relationship
        - 0: no relationship
    
    NOTE: many methods exist to identify a statistically-significant peak/dip (Kobayashi, 2025). For simplicity, here we use simple univariate statistics as in `find_outlier_limits`.
    """
    assert isinstance(x, np.ndarray) and isinstance(y, np.ndarray), "x and y must both be of type np.ndarray"
    assert len(x.shape) == 1 and len(y.shape) == 1, "x and y must both be 1-dimensional vectors"
    assert len(x) == len(y), "x and y must have the same length"

    products: list = [float(np.dot(x[-i:], y[:i])) for i in range(1, len(x)+1)]
    lower_limit, upper_limit = find_outlier_limits(products)
    outliers = np.sum([1 for x in products if x > upper_limit or x < lower_limit])
    
    if outliers > 0:
        return 1
    return 0
