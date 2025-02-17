# Copyright 2020-2024 Intel Corporation
# SPDX-License-Identifier: Apache-2.0


"""Median module."""

import numpy as np

from openfl.interface.aggregation_functions.core import AggregationFunction


class Median(AggregationFunction):
    """Median aggregation."""

    def call(self, local_tensors, *_) -> np.ndarray:
        print("Median called")
        tensors = np.array([x.tensor for x in local_tensors])
        return np.median(tensors, axis=0)
