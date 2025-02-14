# Copyright (C) 2020-2025 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

"""You may copy this file as the starting point of your own model."""


from openfl.federated import FederatedAnalyticsTaskRunner
import numpy as np
from openfl.utilities import TensorKey

class IrisHistogram(FederatedAnalyticsTaskRunner):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def query(self, col_name, round_num, columns, **kwargs):
        print("query called")
        for key, value in kwargs.items():
            print(f"{key}: {value}")
        data = self.data_loader.get_data()
        query_tensorkey_dict = {}
        tags = ("trained",)
        for column in columns:
            print(f"Computing histogram for column: {column}")
            hist = self.compute_hist(data, column)
            query_tensorkey_dict[TensorKey(column, col_name, round_num, False, tags)] = hist
        return query_tensorkey_dict
    
    def compute_hist(self, df, col_name):
        _, vals = np.histogram(df[col_name])  
        _, vals = np.histogram(df[col_name])
        return vals

    def aggregate_query(self, **kwargs):
        print("aggregate_query called")
        for key, value in kwargs.items():
            print(f"{key}: {value}")

    def save_native(self):
        """Save aggegated query result."""
        pass
        