"""
<Module 2 Assignment>


Copyright (c) 2021 -- This is the 2021 Fall B version of the Template
Licensed
Written by <Abhinav_Jain_ALY6140> <---- PLEASE, WRITE YOUR NAME HERE

# you can also rely on the docstring documentation from pandas on how to format dosctrings:
# https://pandas.pydata.org/pandas-docs/stable/development/contributing_docstring.html

"""

import pandas as pd
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy import inspect


def add_nums(a, b):
    """
    Add two numbers together
    :param a: first number
    :param b: second number
    :return: the sum of two inputs
    """
    
    return a + b

def readTxt(fileLocation):
    """
    Reads the data from the givien text file
    :param fileLocation: give the path of file
    :return: it returns data structure as dataframe
    """
    data_frame_read=pd.read_table(fileLocation,sep="|")
    return data_frame_read

def readCsv(fileLocation):
    """
    Reads the data from the givien csv file
    :param fileLocation: give the path of file
    :return: it returns data structure as dataframe
    """
    data_frame_csv=pd.read_csv(fileLocation)
    return data_frame_csv

def readExcel(fileLocation,sheetName,header):
    """
    Reads the data from the givien excel file
    :param sheetName: sheetName in excel file
    :param header: row number for column names 
    :return: it returns data structure as dataframe
    """
    data_frame_excel=pd.read_excel(fileLocation,sheet_name=sheetName,engine='openpyxl',header=header)
    return data_frame_excel

def readJSON(fileLocation):
    """
    Reads the data from the givien JSON file
    :param fileLocation: give the path of file
    :return: it returns data structure as dataframe
    """
    data_frame_json=pd.read_json(fileLocation)
    return data_frame_json

def readHTML(fileLocation):
    """
    Reads the data from the givien HTML file
    :param fileLocation: give the path of file
    :return: it returns data structure as dataframe
    """  
    with open(fileLocation, 'r') as f:
        file_contents = f.read()
        html_soup = BeautifulSoup(file_contents, 'lxml')
        return html_soup

def readSQL(fileLocation):
    """
    Reads the data from the givien SQL file
    :param fileLocation: give the path of file
    :return: it returns data structure as dataframe
    """   
    sql_engine = create_engine("sqlite:///"+fileLocation)
    insp = inspect(sql_engine)
    return sql_engine


    
 




if __name__ == '__main__':
    print("************************")  
    
    
