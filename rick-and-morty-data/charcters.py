#!/usr/bin/python3  
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    
    data_file = "rickandmortychars.csv"

    sheet1 = pd.read_excel(data_file, sheet_name=0, index_col=0)

    sheet2 = pd.read_excell(data_file, sheet_name=1, index_col=0)
    # DF has 5 rows and 24 columns (indexed by title)
    rickle = pr.concat([sheet1,sheet2])
    print(sheet1.head())


