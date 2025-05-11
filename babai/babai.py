"""
In this module we will implement the functions
necessary to execute the Babai algorithm.
"""

import numpy as np


def babai_algorithm(base: np.array, w: np.array) -> np.array:
    """
    Implementation of the babai algorithm. This function
    recieves a base `B` and an arbitrary vector `w`. Each
    column of `B` must represent a vector of the basis.
    It returns a vector `v` close to `w`.
    """
    assert base.shape[0] == w.shape[0]
    t = np.linalg.solve(base, w)
    a = np.round(t)
    v = base @ a
    return v
