import pandas as pd
import numpy as np
from geotree.models import GeoData, GeoName
import math
import os

YEAR_RANGE = range(2001,2021)
AGE_RANGE = range(0,91)
_FILE_PATH = "\geotree\data\datadownload.xlsx"
DELIMITER = '_'

def run():
    """Generates migrations for the geodata and geoname models based on reading the excel file datadownload.xlsx

    Raises:
        ValueError: If there is a failure in reading from the excel file
    """
    print("Loading Data")
    #Clear pre-existing models. Note order is important due to keying.
    GeoData.objects.all().delete()
    GeoName.objects.all().delete()
    
    # Loads into dictionary of dataframes, where each key is a year, 
    path = os.path.join(os.getcwd() + _FILE_PATH)
    df = pd.read_excel(path, sheet_name=None)
    print("Data Loaded")

    years = [str(i) for i in YEAR_RANGE]

    for year in years:
        print(f"Processing year {year}")
        for _, r in df[year].iterrows():
            geo_name,_ = GeoName.objects.get_or_create(name = pascal_case_space(r['geogname']), geogcode = r['geogcode'])

            for age in AGE_RANGE:
                male_count = r[gen_col_name(year, age, True)]
                female_count = r[gen_col_name(year, age, False)]

                if math.isnan(male_count) or math.isnan(female_count):
                    raise ValueError("Failed to read data frame for value Year: {year} Age: {age} \n \
                        The erroring row of the dataframe is {r} ")

                geo_data = GeoData(year = year, age = age, male = male_count, female = female_count, geo_name = geo_name)
                geo_data.save()


def pascal_case_space(text):
    """Capitalizes the first letter of every word in a string. All other letters are given in lowercase. 

    Args:
        text (String): The text to be modified

    Returns:
        String
    """
    arr = text.split(" ")
    for i in range(len(arr)):
        arr[i] = arr[i].capitalize()
    
    return " ".join(arr)


def gen_col_name(year, age,male=True):
    """Creates a column name of the datadownload.xlsx file for the given parameters

    Args:
        year (int): The year
        age (int): Population age
        male (bool, optional): Is the gender male. Defaults to True.

    Returns:
        String: A string representing the column name
    """
    if male:
        text = "m_"
    else:
        text = "f_"
    
    text+=str(year)[-2:]
    text+="_"
    text += str(age)
    return text