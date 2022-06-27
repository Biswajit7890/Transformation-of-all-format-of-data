# importing all necessary Libraries

import pandas as pd
import requests
import numpy as np
import os
import io
import logging


# Defining all the logger functions also the log file which will catching all the information and Exception

logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler("data_transform.log", mode="w")
fileHandler.setLevel(logging.INFO)
fileFormat = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fileHandler.setFormatter(fileFormat)
logger.addHandler(fileHandler)


# Defining the function which is checking the shape of all the dataframes and concatenating and making into one main dataframe


def transform(df_csv, df_tsv, df_xml, df_json):
    try:
        assert df_csv.shape[0] == 10
        assert df_tsv.shape[0] == 10
        assert df_json.shape[0] == 10
        assert df_xml.shape[0] == 10
        df_main = pd.concat([df_csv, df_tsv, df_json, df_xml], axis=1, join="inner")
        df_main = df_main.loc[:, ~df_main.columns.duplicated()].copy()
        logger.info(" Test Passed")
    except Exception as e:
        logger.error(e)
    return df_main

