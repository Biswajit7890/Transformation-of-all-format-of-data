# Importing all the neccessary libraries
import pandas
import requests
import string
import logging
import os
from data_req.data_read import data_request
from data_transform.data_transform import transform


def script():
    url = "https://raw.githubusercontent.com/Biswajit7890/Data-Storage/main/cars"  # This the url of data
    df_csv, df_tsv, df_json, df_xml = data_request(url)  # Function for pulling the data
    df_main = transform(
        df_csv, df_tsv, df_json, df_xml
    )  # Function for assertion and concatenation
    if not os.path.exists("main_data"):
        os.makedirs("main_data")
    complete_path = os.path.join(os.path.abspath(os.curdir) + "/main_data")
    df_main.to_csv(complete_path + "/df_main.csv", index=False)

if __name__ == "__main__":
    script()

