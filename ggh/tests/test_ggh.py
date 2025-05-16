"""
This module contains some test to check the correct
functionalities of the Babai algorithm.
"""

import pytest
import numpy as np

from ggh.ggh import GGHAlgorithm


def test_ggh_execution_1():
    """
    Performs a simple execution to check that
    the private and public key of the GGH algorithm
    are generated without errors.
    """
    basis = np.array([[1, 0], [0, 1]]).T
    _ = GGHAlgorithm(basis, values_range=10)


def test_ggh_cipher_decipher_1():
    """
    Performs a simple execution to check that
    the cipher and decipher methods work well.
    """
    message = [42, 11]
    basis = np.array([[1, 0], [0, 1]]).T
    for _ in range(100):
        ggh_algo = GGHAlgorithm(basis, values_range=10)
        cipher_message = ggh_algo.cipher_message(message)
        recovered_message = ggh_algo.decipher_message(cipher_message)
        assert recovered_message == message


def test_ggh_cipher_decipher_2():
    """
    Performs a simple execution to check that
    the cipher and decipher methods work well.
    """
    message = [4123135, 231351, 78321686]
    basis = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]).T
    ggh_algo = GGHAlgorithm(basis, values_range=10)
    cipher_message = ggh_algo.cipher_message(message)
    recovered_message = ggh_algo.decipher_message(cipher_message)
    assert recovered_message == message


def test_ggh_cipher_decipher_3():
    """
    Performs a simple execution to check that
    the cipher and decipher methods work well.
    """
    message = [2754254, 254698, 963, 4562123]
    basis = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]).T
    ggh_algo = GGHAlgorithm(basis, values_range=10)
    cipher_message = ggh_algo.cipher_message(message)
    recovered_message = ggh_algo.decipher_message(cipher_message)
    assert recovered_message == message


def test_ggh_cipher_decipher_4():
    """
    Performs a simple execution to check that
    the cipher and decipher methods work well.
    """
    message = [123456789, 546213879]
    basis = np.array([[127, 546], [462, 213]]).T
    for _ in range(100):
        ggh_algo = GGHAlgorithm(basis, values_range=10)
        cipher_message = ggh_algo.cipher_message(message)
        recovered_message = ggh_algo.decipher_message(cipher_message)
        assert recovered_message == message


def test_ggh_cipher_decipher_5():
    """
    Performs a specific operation of cipher and decipher.
    """
    message = [3, -4, 1, 3]
    basis = np.array([[2, -2, -1, -1], [-3, 1, 3, -4], [1, 0, 2, 3], [-4, 4, 1, -2]]).T
    public_key = np.array([[1, 0, 0, 44], [0, 1, 0, 18], [0, 0, 1, 4], [0, 0, 0, 49]]).T
    ggh_algo = GGHAlgorithm(basis, public_key=public_key, values_range=10)
    ggh_algo.public_key = public_key
    r = np.array([-1, 1, 1, -1])
    cipher_message = ggh_algo.cipher_message(message, r=r)
    recovered_message = ggh_algo.decipher_message(cipher_message)
    assert recovered_message == message


def test_private_key_is_ortogonal_basis():
    """
    After generating the public and private keys,
    we will check that the basis B is a good basis.
    """

    basis = np.array([[1, 0], [0, 1]]).T
    ggh_algo = GGHAlgorithm(basis, values_range=10)
    delta_b = GGHAlgorithm.compute_delta_basis(ggh_algo.private_key)
    assert delta_b == 1


def test_private_key_is_good_basis():
    """
    After generating the public and private keys,
    we will check that the basis B is a good basis.
    """
    epsilon = 0.1

    basis = np.array([[2, 0], [0, 2]]).T
    ggh_algo = GGHAlgorithm(basis, values_range=10)
    delta_b = GGHAlgorithm.compute_delta_basis(ggh_algo.private_key)
    assert 0 < delta_b - 1 < epsilon


if __name__ == "__main__":
    pytest.main()
