There is one folder for each (dataset, noise type) combination, for FB15k-237 and WN18RR with type noise (indicated by a _type suffix) and random noise (no suffix)

The noise types are further elaborated upon in the report.

Each folder has 0-10% noise subfolders, indicating with % noise the models where trained on. The datasets for each combination is found in the data folder.

The datasets are named following the name scheme: [datasetname]-[noiselevel][noise indicator] with "n" as random noise and "nt as type noise indicators. fb15k-237-5n for example is the FB15k-237 dataset with 5\% random noise. They can be found in the respective "data" folders

Each model folder contains the config file used to train that model. Note that due to github file size limits, the best checkpoints are not in this repository. The config files for training are modified versions of the best hyperparameter configurations for the (model,evaluation dataset) combination,
found by Daniel Ruffinelli, Samuel Broscheit und Rainer Gemulla in the 2020 paper "YOU CAN TEACH AN OLD DOG NEW TRICKS! ON TRAINING KNOWLEDGE GRAPH EMBEDDINGS".
