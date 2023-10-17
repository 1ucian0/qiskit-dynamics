# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2023.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Global alias instances.
"""

from typing import Union

from arraylias import numpy_alias, scipy_alias

from qiskit_dynamics.array import Array

# global NumPy and SciPy aliases
DYNAMICS_NUMPY_ALIAS = numpy_alias()
DYNAMICS_SCIPY_ALIAS = scipy_alias()

DYNAMICS_NUMPY_ALIAS.register_type(Array, "numpy")
DYNAMICS_SCIPY_ALIAS.register_type(Array, "numpy")


DYNAMICS_NUMPY = DYNAMICS_NUMPY_ALIAS()
DYNAMICS_SCIPY = DYNAMICS_SCIPY_ALIAS()


ArrayLike = Union[DYNAMICS_NUMPY_ALIAS.registered_types()]