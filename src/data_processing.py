import argparse
import os
import pathlib
import sys
from random import shuffle

import pandas as pd
from sklearn.model_selection import train_test_split

from load_data import read_params

#On sépare nos données d'entrainement et de test
def split_data(df, train_data_path, test_data_path, split_ratio, random_state):
    train, test = train_test_split(
        df, test_size=split_ratio, random_state=random_state, shuffle=True
    )
    train.to_csv(train_data_path, sep=",", index=False, encoding="utf-8")
    test.to_csv(test_data_path, sep=",", index=False, encoding="utf-8")

#On sauvegarde nos données d'entrainement et de test 
def split_and_saved_data(config_path):
    """
    split the train dataset(data/raw) and save it in the data/processed folder
    input: config path
    output: save splitted files in output folder
    """
    config = read_params(config_path)

    raw_data_path = (
        pathlib.Path(__file__).parents[1].resolve()
        / config["raw_data_config"]["raw_data_csv"]
    )

    test_data_path = (
        pathlib.Path(__file__).parents[1].resolve()
        / config["processed_data_config"]["test_data_csv"]
    )

    train_data_path = (
        pathlib.Path(__file__).parents[1].resolve()
        / config["processed_data_config"]["train_data_csv"]
    )

    random_state = config["raw_data_config"]["random_state"]
    split_ratio = config["raw_data_config"]["train_test_split_ratio"]

    raw_df = pd.read_csv(raw_data_path)
    split_data(
        raw_df, train_data_path, test_data_path, split_ratio, random_state
    )


if __name__ == "__main__":
    path_yaml = pathlib.Path(__file__).parents[1].resolve() / "params.yaml"
    sys.argv = [""]
    del sys
    args = argparse.ArgumentParser()
    args.add_argument("--config", default=path_yaml)
    parsed_args = args.parse_args()
    split_and_saved_data(config_path=parsed_args.config)
