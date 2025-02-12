# Copyright (C) 2020-2025 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

"""You may copy this file as the starting point of your own model."""


from openfl.federated import FederatedAnalyticsTaskRunner


class IrisHistogram(FederatedAnalyticsTaskRunner):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def query(self, **kwargs):
        pass

    def aggregate_query(self, **kwargs):
        pass

    def save_native(self):
        """Save aggegated query result."""
        pass
        