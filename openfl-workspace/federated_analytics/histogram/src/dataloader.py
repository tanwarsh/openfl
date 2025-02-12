# Copyright (C) 2020-2025 Intel Corporation
# SPDX-License-Identifier: Apache-2.0


from openfl.federated import DataLoader


class IRISInMemory(DataLoader):
    """Data Loader for IRIS Dataset."""

    def __init__(self, data_path, batch_size, **kwargs):
        super().__init__(batch_size, **kwargs)

        # download data

        # create shards

    def _load_raw_datashards(shard_num, collaborator_count):
        pass


    def load_mnist_shard(shard_num, collaborator_count, categorical=True, channels_last=True, **kwargs):
        pass
