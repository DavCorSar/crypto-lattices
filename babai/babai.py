"""
In this module we will implement the functions
necessary to execute the Babai algorithm.
"""

import numpy as np

from babai.exceptions import ClosestVectorHasNotBeenComputed


class BabaiAlgorithm():
    """
    This class implements the Babai algorithm.
    It also allows to compute the distance between
    the two vectors and decide if it's a good basis.
    """
    def __init__(self, base: np.array, w: np.array):
        assert base.shape[0] == w.shape[0]
        self.base = base
        self.w = w
        self.v: np.array | None = None

    def compute_closest_vector(self) -> None:
        """
        Implementation of the babai algorithm. This function
        uses the base `B` and the arbitrary vector `w`. Each
        column of `B` must represent a vector of the basis.
        It stores the vector `v` close to `w`.
        """
        t = np.linalg.solve(self.base, self.w)
        a = np.round(t)
        v = self.base @ a
        self.v = v

    def compute_distance(self) -> float:
        """
        If the closest vector `v` has been computed, this
        function returns the distance between the vector
        `v` and the vector `w`.
        """
        if self.v is None:
            raise ClosestVectorHasNotBeenComputed
        return np.linalg.norm(self.w - self.v)

    def is_a_good_base() -> bool:
        """
        Returns `True` if the base `B` can be
        considered a good base. Returns `False` otherwise.
        """