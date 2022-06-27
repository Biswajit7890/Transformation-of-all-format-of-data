# importing all necessary Libraries

import pandas as pd
import requests
import numpy as np
import os
import io
import logging

# Defining all the logger functions also the log file which will catching all the information and Exception

logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler("data_request.log", mode="w")
fileHandler.setLevel(logging.INFO)
fileFormat = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fileHandler.setFormatter(fileFormat)
logger.addHandler(fileHandler)


# Pulling all the data format from the github


def data_request(infile):
    try:
        csv_path = infile + "df_personal_details.csv"
        json_path = infile + "df_termdeposit_details.json"
        tsv_path = infile + "df_loan_details.tsv"
        xml_path = infile + "df_contactdur_details.xml"
        df_csv = pd.read_csv(csv_path, sep=",")
        df_tsv = pd.read_csv(tsv_path, sep="\t")
        df_xml = pd.read_xml(xml_path)
        df_xml = df_xml.drop(labels=["index"], axis=1)
        df_json = pd.read_json(json_path, orient="split")
        logger.info(" All files have been extracted from the Storage Server")
    except Exception as e:
        logger.error(e)
    return (df_csv, df_tsv, df_xml, df_json)

