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

    def initialize_tensorkeys_for_functions(self):
        print("initialize_tensorkeys_for_functions called")
        return {}
    
    def train_batches(self, num_batches=None, use_tqdm=False):
        print("train_batches called")

    def get_query_data_size(self):
        return self.data_loader.get_query_data_size()

    def get_valid_data_size(self):
        """Get the number of examples.

        It will be used for weighted averaging in aggregation.

        Returns:
            int: The number of validation examples.
        """
        return self.data_loader.get_valid_data_size()
    
    def validate(self):
        """Run validation.

        Returns:
            dict: {<metric>: <value>}.
        """
        raise NotImplementedError

    def get_required_tensorkeys_for_function(self, func_name, **kwargs):
        """When running a task, a map of named tensorkeys must be provided to
        the function as dependencies.

        Args:
            func_name (str): The function name.
            **kwargs: Additional parameters to pass to the function.

        Returns:
            list: List of required TensorKey. (TensorKey(tensor_name, origin,
                round_number))
        """
        print("get_required_tensorkeys_for_function called")
        return []

    def get_tensor_dict(self, with_opt_vars):
        """Get the weights.

        Args:
            with_opt_vars (bool): Specify if we also want to get the variables
                of the optimizer.

        Returns:
            dict: The weight dictionary {<tensor_name>: <value>}.
        """
        print("get_tensor_dict called")
        return {}

    def set_tensor_dict(self, tensor_dict, with_opt_vars):
        """Set the model weights with a tensor dictionary:
        {<tensor_name>: <value>}.

        Args:
            tensor_dict (dict): The model weights dictionary.
            with_opt_vars (bool): Specify if we also want to set the variables
                of the optimizer.

        Returns:
            None
        """
        print("set_tensor_dict")

    def reset_opt_vars(self):
        """Reinitialize the optimizer variables.

        Returns:
            None
        """
        print("reset_opt_vars called")

    def initialize_globals(self):
        """Initialize all global variables.

        Returns:
            None
        """
        print("initialize_globals called")

    def load_native(self, filepath, **kwargs):
        """Load model state from a filepath in ML-framework "native" format,
        e.g. PyTorch pickled models.

        May load from multiple files. Other filepaths may be derived from the
        passed filepath, or they may be in the kwargs.

        Args:
            filepath (str): Path to frame-work specific file to load.
                For frameworks that use multiple files, this string must be
                    used to derive the other filepaths.
            **kwargs: Additional parameters to pass to the function. For
                future-proofing.

        Returns:
            None
        """
        print("load_native called")

    def save_native(self, filepath, **kwargs):
        """Save model state in ML-framework "native" format, e.g. PyTorch
        pickled models.

        May save one file or multiple files, depending on the framework.

        Args:
            filepath (str): If framework stores a single file, this should be
                a single file path. Frameworks that store multiple files may
                need to derive the other paths from this path.
            **kwargs: Additional parameters to pass to the function. For
                future-proofing.

        Returns:
            None
        """
        print("save_native called")