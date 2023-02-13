import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from create_dataframe import *

starters_X = Fangraphs.starters.drop(columns = ['Name', 'Team', 'Pos', 'Actual Salary'])
relievers_X = Fangraphs.relievers.drop(columns = ['Name', 'Team', 'Pos', 'Actual Salary'])
catchers_X = Fangraphs.catchers.drop(columns = ['Name', 'Team', 'Pos', 'Actual Salary'])
first_basemen_X = Fangraphs.first_basemen.drop(columns = ['Name', 'Team', 'Pos', 'Actual Salary'])
second_basemen_X = Fangraphs.second_basemen.drop(columns = ['Name', 'Team', 'Pos', 'Actual Salary'])
third_basemen_X = Fangraphs.third_basemen.drop(columns = ['Name', 'Team', 'Pos', 'Actual Salary'])
shortstops_X = Fangraphs.shortstops.drop(columns = ['Name', 'Team', 'Pos', 'Actual Salary'])
outfielders_X = Fangraphs.outfielders.drop(columns = ['Name', 'Team', 'Pos', 'Actual Salary'])
designated_hitters_X = Fangraphs.designated_hitters.drop(columns = ['Name', 'Team', 'Pos', 'Actual Salary'])

starters_Y = Fangraphs.starters['Actual Salary']
relievers_Y = Fangraphs.relievers['Actual Salary']
catchers_Y = Fangraphs.catchers['Actual Salary']
first_basemen_Y = Fangraphs.first_basemen['Actual Salary']
second_basemen_Y = Fangraphs.second_basemen['Actual Salary']
third_basemen_Y = Fangraphs.third_basemen['Actual Salary']
shortstops_Y = Fangraphs.shortstops['Actual Salary']
outfielders_Y = Fangraphs.outfielders['Actual Salary']
designated_hitters_Y = Fangraphs.designated_hitters['Actual Salary']

starters_lr = LinearRegression()
relievers_lr = LinearRegression()
catchers_lr = LinearRegression()
first_basemen_lr = LinearRegression()
second_basemen_lr = LinearRegression()
third_basemen_lr = LinearRegression()
shortstops_lr = LinearRegression()
outfielders_lr = LinearRegression()
designated_hitters_lr = LinearRegression()

starters_lr.fit(starters_X, starters_Y)
relievers_lr.fit(relievers_X, relievers_Y)
catchers_lr.fit(catchers_X, catchers_Y)
first_basemen_lr.fit(first_basemen_X, first_basemen_Y)
second_basemen_lr.fit(second_basemen_X, second_basemen_Y)
third_basemen_lr.fit(third_basemen_X, third_basemen_Y)
shortstops_lr.fit(shortstops_X, shortstops_Y)
outfielders_lr.fit(outfielders_X, outfielders_Y)
designated_hitters_lr.fit(designated_hitters_X, designated_hitters_Y)