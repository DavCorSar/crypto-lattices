# Babai & GGH Algorithms in Python

This repository provides clean, Pythonic implementations of the **Babai Algorithm** and the **Goldreich–Goldwasser–Halevi (GGH) cryptosystem**, two important concepts in lattice-based cryptography.

## Overview

- **Babai Algorithm**: A technique for finding an approximate closest vector in a lattice.
- **GGH Cryptosystem**: A public-key cryptographic scheme based on lattice problems, designed to be resistant to quantum attacks.

These algorithms demonstrate core principles in lattice-based cryptography and serve as educational tools or experimental cryptographic primitives.

---

## Algorithms

### Babai Algorithm

The Babai algorithm approximates the **Closest Vector Problem (CVP)** in a lattice by projecting a target vector onto a lattice basis and rounding the coefficients.

**Key Features:**
- Computes the closest vector approximation.
- Calculates the Euclidean distance from the target.
- Evaluates the quality of a basis.

```python
import numpy as np

from babai.babai import BabaiAlgorithm


basis = np.array([[57, 1, 0], [4135, 0, 1213], [0, 54612, 234]]).T
w = np.array([2315, 0, 35])
babai_alg = BabaiAlgorithm(basis, w)
babai_alg.compute_closest_vector()
distance = babai_alg.compute_distance()
delta_b = babai_alg.compute_delta_b()
```

### GGH Cryptosystem

The GGH scheme is a lattice-based encryption algorithm that uses a private basis for decryption and a public basis for encryption.

**Key Features:**
- Key generation (private and public basis).
- Message encryption.
- Message decryption.
- Basis quality metrics (delta and determinant).

```python
import numpy as np

from ggh.ggh import GGHAlgorithm


message = [3, -4, 1, 3]
basis = np.array([[2, -2, -1, -1], [-3, 1, 3, -4], [1, 0, 2, 3], [-4, 4, 1, -2]]).T
ggh_algo = GGHAlgorithm(basis, values_range=10)
cipher_message = ggh_algo.cipher_message(message)
recovered_message = ggh_algo.decipher_message(cipher_message)
delta_private_key = GGHAlgorithm.compute_delta_basis(ggh_algo.private_key)
delta_public_key = GGHAlgorithm.compute_delta_basis(ggh_algo.public_key)
```
---

## Installation
You can install the dependencies by cloning the repository and using `uv` (https://github.com/astral-sh/uv):

```bash
git clone https://github.com/DavCorSar/crypto-lattices.git
cd crypto-lattices
uv sync
```
