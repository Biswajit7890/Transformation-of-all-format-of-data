# Importing all the neccessary libraries
import pandas
import requests
import string
import logging
import os
from data_req.data_read import data_request
from data_transform.data_transform import transform


def script():
    url = "https://raw.githubusercontent.com/Biswajit7890/varied-sources/master/dataset/"  # This the url of data
<<<<<<< HEAD
    df_csv, df_tsv, df_xml, df_json = data_request(url)  # Function for pulling the data
=======
    df_csv, df_tsv, df_json, df_xml = data_request(url)  # Function for pulling the data
>>>>>>> 6056372c4238033f926100bb469f33c2c0f8d497
    df_main = transform(
        df_csv, df_tsv, df_xml, df_json
    )  # Function for assertion and concatenation
    if not os.path.exists("main_data"):
        os.makedirs("main_data")
    complete_path = os.path.join(os.path.abspath(os.curdir) + "/main_data")
    df_main.to_csv(complete_path + "/df_main.csv", index=False)


if __name__ == "__main__":
    script()

