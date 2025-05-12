"""
This module contains some test to check the correct
functionalities of the Babai algorithm.
"""

import pytest
import numpy as np

from babai.babai import BabaiAlgorithm
from babai.exceptions import ClosestVectorHasNotBeenComputed


def test_babai_closest_vector_1():
    """
    Performs a simple execution to check that
    the Babai algorithm is executed without errors.
    """
    base = np.array([[1, 0], [0, 1]]).T
    w = np.array([2.0, 3.0])
    expected_result = np.array([2, 3])
    babai_alg = BabaiAlgorithm(base, w)
    babai_alg.compute_closest_vector()
    assert np.all(babai_alg.v == expected_result)


def test_babai_closest_vector_2():
    """
    Performs a simple execution to check that
    the Babai algorithm is executed without errors.
    """
    base = np.array([[1, 0], [0, 1]]).T
    w = np.array([2.4, 3.8])
    expected_result = np.array([2, 4])
    babai_alg = BabaiAlgorithm(base, w)
    babai_alg.compute_closest_vector()
    assert np.all(babai_alg.v == expected_result)


def test_babai_closest_vector_3():
    """
    Performs a simple execution to check that
    the Babai algorithm is executed without errors.
    """
    base = np.array([[137, 312], [215, -187]]).T
    w = np.array([53172, 81743])
    expected_result = np.array([53159, 81818])
    babai_alg = BabaiAlgorithm(base, w)
    babai_alg.compute_closest_vector()
    assert np.all(babai_alg.v == expected_result)


def test_babai_distance_1():
    """
    Performs a simple execution to check that
    the execution of the method that computes the
    distance fails if the closest vector has not been
    computed first.
    """
    base = np.array([[1, 0], [0, 1]]).T
    w = np.array([2.0, 3.0])
    babai_alg = BabaiAlgorithm(base, w)
    with pytest.raises(ClosestVectorHasNotBeenComputed):
        babai_alg.compute_distance()


def test_babai_distance_2():
    """
    Performs a simple execution to check that
    the execution of the method that computes the
    distance works well with a simple case.
    """
    base = np.array([[1, 0], [0, 1]]).T
    w = np.array([2.0, 3.0])
    babai_alg = BabaiAlgorithm(base, w)
    babai_alg.compute_closest_vector()
    assert babai_alg.compute_distance() == 0


def test_babai_good_base():
    """
    Checks that if the base `B` is orthogonal,
    the value of Delta(b) = 1.
    """
    base = np.array([[1, 0], [0, 1]]).T
    w = np.array([2.0, 3.0])
    babai_alg = BabaiAlgorithm(base, w)
    assert babai_alg.compute_delta_b() == 1


if __name__ == "__main__":
    pytest.main()
