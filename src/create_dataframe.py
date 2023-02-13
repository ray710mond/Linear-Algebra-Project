import numpy as np
import pandas as pd
import sklearn as sk
import os



class Fangraphs:
    def create_database(file_name):
        directory = r"C:\Users\ray71\OneDrive\Documents\Regis Documents\Senior Year\Linear Algebra\Final Project\Final CSV Files"
        path = os.path.join(directory, file_name)
        if os.path.isfile(path):
            database = pd.read_csv(path, names=path[0])
        
