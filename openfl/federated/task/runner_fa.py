# Copyright 2020-2025 Intel Corporation
# SPDX-License-Identifier: Apache-2.0


"""
Base classes for Federated Analytics.

You may copy this file as the starting point of your own keras model.
"""

from openfl.federated.task.runner import TaskRunner

class FederatedAnalyticsTaskRunner(TaskRunner):
    """The base class for Federated Analytics."""

    def __init__(self, **kwargs):
        """Initializes the KerasTaskRunner instance.

        Args:
            **kwargs: Additional parameters to pass to the function
        """
        super().__init__(**kwargs)

    def query(self, **kwargs):
        pass

    def aggregate_query(self, **kwargs):
        pass

    def save_native(self):
        """Save aggegated query result."""
        pass