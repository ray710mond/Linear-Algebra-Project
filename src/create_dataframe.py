import pandas as pd
import os

class Fangraphs:
    def create_database(file_name):
        directory = r"C:\Users\ray71\OneDrive\Documents\Regis Documents\Senior Year\Linear Algebra\Final Project\Final CSV Files"
        abs_path = os.path.join(directory, file_name)
        print(abs_path)
        if os.path.isfile(abs_path):
            database = pd.read_csv(abs_path, names=abs_path[0])
        return database

    starters = create_database('Starting Pitchers - Fangraphs Leaderboards.csv')
    relievers = create_database('Relief Pitchers - Fangraphs Leaderboards.csv')
    catchers = create_database('Catchers - Fangraphs Leaderboards.csv')
    first_basemen = create_database('First Basemen - Fangraphs Leaderboards.csv')
    second_basemen = create_database('Second Basemen - Fangraphs Leaderboards.csv')
    third_basemen = create_database('Third Basemen - Fangraphs Leaderboards.csv')
    shortstops = create_database('Shortstops - Fangraphs Leaderboards.csv')
    outfielders = create_database('Outfielders - Fangraphs Leaderboards.csv')
    designated_hitters = create_database('Designated Hitters - Fangraphs Leaderboard')
    

        
