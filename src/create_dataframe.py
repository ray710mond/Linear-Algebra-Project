import pandas as pd
import os

class Fangraphs:
    def create_dataframe(file_name):
        directory = r"C:\Users\ray71\OneDrive\Documents\Regis Documents\Senior Year\Linear Algebra\Final Project\Final CSV Files"
        abs_path = os.path.join(directory, file_name)
        print(abs_path)
        if os.path.isfile(abs_path):
            database = pd.read_csv(abs_path)
        return database

    starters = create_dataframe('Starting Pitchers - Fangraphs Leaderboards.csv')
    relievers = create_dataframe('Relief Pitchers - Fangraphs Leaderboards.csv')
    catchers = create_dataframe('Catchers - Fangraphs Leaderboards.csv')
    first_basemen = create_dataframe('First Basemen - Fangraphs Leaderboards.csv')
    second_basemen = create_dataframe('Second Basemen - Fangraphs Leaderboards.csv')
    third_basemen = create_dataframe('Third Basemen - Fangraphs Leaderboards.csv')
    shortstops = create_dataframe('Shortstops - Fangraphs Leaderboards.csv')
    outfielders = create_dataframe('Outfielders - Fangraphs Leaderboards.csv')
    designated_hitters = create_dataframe('Designated Hitters - Fangraphs Leaderboards.csv')
