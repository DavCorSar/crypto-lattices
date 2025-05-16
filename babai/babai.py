"""
In this module we will implement the functions
necessary to execute the Babai algorithm.
"""

import numpy as np

from babai.exceptions import ClosestVectorHasNotBeenComputed


class BabaiAlgorithm:
    """
    This class implements the Babai algorithm.
    It also allows to compute the distance between
    the two vectors and decide if it's a good basis.
    """

    def __init__(self, basis: np.ndarray, w: np.array):
        assert basis.shape[0] == w.shape[0]
        self.basis = basis
        self.w = w
        self.v: np.ndarray | None = None

    def compute_closest_vector(self) -> None:
        """
        Implementation of the babai algorithm. This function
        uses the basis `B` and the arbitrary vector `w`. Each
        column of `B` must represent a vector of the basis.
        It stores the vector `v` close to `w`.
        """
        t = np.linalg.solve(self.basis, self.w)
        a = np.round(t)
        v = self.basis @ a
        self.v = v

    def compute_distance(self) -> float:
        """
        If the closest vector `v` has been computed, this
        function returns the Euclidean distance between the vector
        `v` and the vector `w`.
        """
        if self.v is None:
            raise ClosestVectorHasNotBeenComputed
        return np.linalg.norm(self.w - self.v)

    def compute_delta_b(self) -> float:
        """
        Computes the value of Delta(B) that is used
        to check if B is a good basis.
        """
        basis_prod = 1
        for b in self.basis.T:
            basis_prod *= np.linalg.norm(b)
        denom = np.sqrt(np.linalg.det(self.basis.T @ self.basis))
        delta_b = basis_prod / denom
        return delta_b

    def is_a_good_basis(self, epsilon: float = 0.01) -> bool:
        """
        Returns `True` if the basis `B` can be
        considered a good basis. Returns `False` otherwise.
        """
        delta_b = self.compute_delta_b()
        return bool(delta_b - 1 < epsilon)
