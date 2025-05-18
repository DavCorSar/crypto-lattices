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
    basis = np.array([[1, 0], [0, 1]]).T
    w = np.array([2.0, 3.0])
    expected_result = np.array([2, 3])
    babai_alg = BabaiAlgorithm(basis, w)
    babai_alg.compute_closest_vector()
    assert np.all(babai_alg.v == expected_result)


def test_babai_closest_vector_2():
    """
    Performs a simple execution to check that
    the Babai algorithm is executed without errors.
    """
    basis = np.array([[1, 0], [0, 1]]).T
    w = np.array([2.4, 3.8])
    expected_result = np.array([2, 4])
    babai_alg = BabaiAlgorithm(basis, w)
    babai_alg.compute_closest_vector()
    assert np.all(babai_alg.v == expected_result)


def test_babai_closest_vector_3():
    """
    Performs a simple execution to check that
    the Babai algorithm is executed without errors.
    """
    basis = np.array([[137, 312], [215, -187]]).T
    w = np.array([53172, 81743])
    expected_result = np.array([53159, 81818])
    babai_alg = BabaiAlgorithm(basis, w)
    babai_alg.compute_closest_vector()
    assert np.all(babai_alg.v == expected_result)


def test_babai_distance_1():
    """
    Performs a simple execution to check that
    the execution of the method that computes the
    distance fails if the closest vector has not been
    computed first.
    """
    basis = np.array([[1, 0], [0, 1]]).T
    w = np.array([2.0, 3.0])
    babai_alg = BabaiAlgorithm(basis, w)
    with pytest.raises(ClosestVectorHasNotBeenComputed):
        babai_alg.compute_distance()


def test_babai_distance_2():
    """
    Performs a simple execution to check that
    the execution of the method that computes the
    distance works well with a simple case.
    """
    basis = np.array([[1, 0], [0, 1]]).T
    w = np.array([2.0, 3.0])
    babai_alg = BabaiAlgorithm(basis, w)
    babai_alg.compute_closest_vector()
    assert babai_alg.compute_distance() == 0


def test_babai_good_basis():
    """
    Checks that if the basis `B` is orthogonal,
    the value of Delta(b) = 1.
    """
    basis = np.array([[1, 0], [0, 1]]).T
    w = np.array([2.0, 3.0])
    babai_alg = BabaiAlgorithm(basis, w)
    assert babai_alg.compute_delta_b() == 1


def test_babai_with_complex_basis():
    """
    Performs an execution using a complex basis.
    """
    basis_bad = np.array([[1, 0, -213], [0, 1, 1213], [0, 0, 234]]).T
    basis_good = np.array([[57, 1, 0], [4135, 0, 1213], [0, 54612, 234]]).T
    w = np.array([2315, 0, 35])

    good_alg = BabaiAlgorithm(basis_good, w)
    good_alg.compute_closest_vector()
    good_alg.compute_distance()
    delta_b_good = good_alg.compute_delta_b()

    bad_alg = BabaiAlgorithm(basis_bad, w)
    bad_alg.compute_closest_vector()
    bad_alg.compute_distance()
    delta_b_bad = bad_alg.compute_delta_b()

    assert delta_b_bad > 100
    assert delta_b_good < 5


if __name__ == "__main__":
    pytest.main()
