"""
This module contains some test to check the correct
functionalities of the Babai algorithm.
"""

import pytest
import numpy as np

from babai import babai


def test_babai_1():
    """
    Performs a simple execution to check that
    the Babai algorithm is executed without errors.
    """
    base = np.array([[1, 0], [0, 1]]).T
    w = np.array([2.0, 3.0])
    expected_result = np.array([2, 3])
    v = babai.babai_algorithm(base=base, w=w)
    assert np.all(v == expected_result)


def test_babai_2():
    """
    Performs a simple execution to check that
    the Babai algorithm is executed without errors.
    """
    base = np.array([[1, 0], [0, 1]]).T
    w = np.array([2.4, 3.8])
    expected_result = np.array([2, 4])
    v = babai.babai_algorithm(base=base, w=w)
    assert np.all(v == expected_result)


def test_babai_3():
    """
    Performs a simple execution to check that
    the Babai algorithm is executed without errors.
    """
    base = np.array([[137, 312], [215, -187]]).T
    w = np.array([53172, 81743])
    expected_result = np.array([53159, 81818])
    v = babai.babai_algorithm(base=base, w=w)
    print(v)
    assert np.all(v == expected_result)

if __name__ == "__main__":
    pytest.main()
