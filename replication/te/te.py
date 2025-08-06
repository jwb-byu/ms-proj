import numpy as np


def transfer_entropy(x: np.ndarray, y: np.ndarray, look_back: int = 1) -> float:
    """
    Calculate the transfer entropy from x to y, considering look_back timepoints before each timepoint
    Details of the algorithm are at:
        - Kobayashi, 2025, Inference of monosynaptic connections from parallel spike trains: A review, https://doi.org/10.1016/j.neures.2024.07.006
    Inputs are binary binned spike trains. If bin sizes are too large or small, a false positive or negative is more likely respectively.
    
    :param x: vector representing the spike train of neuron x
    :param y: vector representing the spike train of neuron y
    :param look_back: number of timepoints to consider prior to each timepoint

    :return: the transfer entropy from x to y
    """
    assert isinstance(x, np.ndarray) and isinstance(y, np.ndarray), "x and y must both be of type np.ndarray"
    assert len(x.shape) == 1 and len(y.shape) == 1, "x and y must both be 1-dimensional vectors"
    assert len(x) == len(y), "x and y must have the same length"

    count_yxy_combined: dict[str, np.float64] = {} # keys are lists of ints as [y_t, y_t-1, y_t-2, x_t-1, x_t-2, ...]
    count_y_given_xy: dict[str, dict[int, np.float64]] = {} # first key is a list of ints as [y_t-1, y_t-2, x_t-1, x_t-2, ...], second key is y_t
    count_y_given_y: dict[str, dict[int, np.float64]] = {} # first key is a list of ints as [y_t-1, y_t-2, ...], second key is y_t
    total_count: np.float64 = np.float64(0)
    te: np.float64 = np.float64(0)

    # count the occurrences
    arr = np.stack((x, y))
    for i in range(look_back, arr.shape[1]):
        total_count += 1
        y_t: int = int(arr[1, i])
        y_history = arr[1, i-look_back:i]
        x_history = arr[0, i-look_back:i]
        
        count_yxy_combined_key: str = "".join(np.concat(([y_t], y_history, x_history)).astype(str).tolist())
        if count_yxy_combined_key not in count_yxy_combined.keys():
            count_yxy_combined[count_yxy_combined_key] = np.float64(0)
        count_yxy_combined[count_yxy_combined_key] += 1
        
        count_y_given_xy_key: str = "".join(np.concat((y_history, x_history)).astype(str).tolist())
        if count_y_given_xy_key not in count_y_given_xy.keys():
            count_y_given_xy[count_y_given_xy_key] = {}
        if y_t not in count_y_given_xy[count_y_given_xy_key].keys():
            count_y_given_xy[count_y_given_xy_key][y_t] = np.float64(0)
        count_y_given_xy[count_y_given_xy_key][y_t] += 1
        
        count_y_given_y_key: str = "".join(y_history.astype(str).tolist())
        if count_y_given_y_key not in count_y_given_y.keys():
            count_y_given_y[count_y_given_y_key] = {}
        if y_t not in count_y_given_y[count_y_given_y_key].keys():
            count_y_given_y[count_y_given_y_key][y_t] = np.float64(0)
        count_y_given_y[count_y_given_y_key][y_t] += 1
    
    # calculate te
    for k in count_yxy_combined.keys():
        k_list = [int(character) for character in k]
        y_t = int(k_list[0])
        history = np.array(k_list[1:])
        y_history = history[:look_back]
        x_history = history[look_back:]

        count_yxy_combined_key = k
        p_yxy_combined: np.float64 = count_yxy_combined[count_yxy_combined_key]/total_count

        count_y_given_xy_key = "".join(np.concat((y_history, x_history)).astype(str).tolist())
        p_y_given_xy: np.float64 = count_y_given_xy[count_y_given_xy_key][y_t]/total_count

        count_y_given_y_key = "".join(y_history.astype(str).tolist())
        p_y_given_y: np.float64 = count_y_given_y[count_y_given_y_key][y_t]/total_count

        te_t: np.float64 = p_yxy_combined * np.log2(p_y_given_xy/p_y_given_y)
        te += te_t
    
    return te
