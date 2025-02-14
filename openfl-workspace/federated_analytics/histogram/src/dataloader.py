# Copyright (C) 2020-2025 Intel Corporation
# SPDX-License-Identifier: Apache-2.0


from openfl.federated import DataLoader
from sklearn.datasets import load_iris
import pandas as pd


class IRISInMemory(DataLoader):
    """Data Loader for IRIS Dataset."""

    def __init__(self, batch_size, data_path, **kwargs):
        print('IRISInMemory.__init__')
        print(batch_size)
        print(data_path)
        for key, value in kwargs.items():
            print(f"{key}: {value}")
        super().__init__(**kwargs)

        # download data
        self._download_raw_data()
        self._load_raw_datashards()
        # create shards
        self.data_shard = self.load_mnist_shard(
            shard_num=int(data_path), **kwargs
        )
        print("Data shard loaded")
        print(self.data_shard)

    def _download_raw_data(self):
        iris = load_iris(as_frame=True)
        data = iris['data']
        data.to_csv('./data/client.csv', index=False)

    def _load_raw_datashards(self):
        return pd.read_csv('./data/client.csv')


    def load_mnist_shard(self, shard_num, collaborator_count, **kwargs):
        print('IRISInMemory.load_mnist_shard')
        print(shard_num)
        print(collaborator_count)
        return self._load_raw_datashards().iloc[shard_num::collaborator_count]
        
    def get_data(self, **kwargs):
        print('IRISInMemory.get_data')
        for key, value in kwargs.items():
            print(f"{key}: {value}")
        return self.data_shard


    def get_feature_shape(self):
        """Returns the shape of an example feature array.

        Raises:
            NotImplementedError: This method must be implemented by a child
                class.
        """
        print('IRISInMemory.get_feature_shape')

    def get_train_loader(self, **kwargs):
        """Returns the data loader for the training data.

        Args:
            kwargs: Additional arguments to pass to the function.

        Raises:
            NotImplementedError: This method must be implemented by a child
                class.
        """
        print('IRISInMemory.get_train_loader')

    def get_valid_loader(self):
        """Returns the data loader for the validation data.

        Raises:
            NotImplementedError: This method must be implemented by a child
                class.
        """
        print('IRISInMemory.get_valid_loader')

    def get_infer_loader(self):
        """Returns the data loader for inferencing data.

        Raises:
            NotImplementedError: This method must be implemented by a child
                class.
        """
        print('IRISInMemory.get_infer_loader')

    def get_train_data_size(self):
        """Returns the total number of training samples.

        Raises:
            NotImplementedError: This method must be implemented by a child
                class.
        """
        print('IRISInMemory.get_train_data_size')

    def get_valid_data_size(self):
        """Returns the total number of validation samples.

        Raises:
            NotImplementedError: This method must be implemented by a child
                class.
        """
        print('IRISInMemory.get_valid_data_size')

    def get_query_data_size(self):
        print('IRISInMemory.get_query_data_size')
        return len(self.data_shard)