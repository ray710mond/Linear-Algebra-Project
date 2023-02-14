import numpy as np
from sklearn.linear_model import LinearRegression
from create_dataframe import *

#input variables
starters_X = Fangraphs.starters.drop(columns = ['Name', 'Team', 'Pos', 'Actual Salary'])
relievers_X = Fangraphs.relievers.drop(columns = ['Name', 'Team', 'Pos', 'Actual Salary'])
catchers_X = Fangraphs.catchers.drop(columns = ['Name', 'Team', 'Pos', 'Actual Salary'])
first_basemen_X = Fangraphs.first_basemen.drop(columns = ['Name', 'Team', 'Pos', 'Actual Salary'])
second_basemen_X = Fangraphs.second_basemen.drop(columns = ['Name', 'Team', 'Pos', 'Actual Salary'])
third_basemen_X = Fangraphs.third_basemen.drop(columns = ['Name', 'Team', 'Pos', 'Actual Salary'])
shortstops_X = Fangraphs.shortstops.drop(columns = ['Name', 'Team', 'Pos', 'Actual Salary'])
outfielders_X = Fangraphs.outfielders.drop(columns = ['Name', 'Team', 'Pos', 'Actual Salary'])
designated_hitters_X = Fangraphs.designated_hitters.drop(columns = ['Name', 'Team', 'Pos', 'Actual Salary'])

#output variable
starters_Y = Fangraphs.starters['Actual Salary']
relievers_Y = Fangraphs.relievers['Actual Salary']
catchers_Y = Fangraphs.catchers['Actual Salary']
first_basemen_Y = Fangraphs.first_basemen['Actual Salary']
second_basemen_Y = Fangraphs.second_basemen['Actual Salary']
third_basemen_Y = Fangraphs.third_basemen['Actual Salary']
shortstops_Y = Fangraphs.shortstops['Actual Salary']
outfielders_Y = Fangraphs.outfielders['Actual Salary']
designated_hitters_Y = Fangraphs.designated_hitters['Actual Salary']

#linear regressions
starters_lr = LinearRegression()
relievers_lr = LinearRegression()
catchers_lr = LinearRegression()
first_basemen_lr = LinearRegression()
second_basemen_lr = LinearRegression()
third_basemen_lr = LinearRegression()
shortstops_lr = LinearRegression()
outfielders_lr = LinearRegression()
designated_hitters_lr = LinearRegression()

#least-squares fitting
starters_lr.fit(starters_X, starters_Y)
relievers_lr.fit(relievers_X, relievers_Y)
catchers_lr.fit(catchers_X, catchers_Y)
first_basemen_lr.fit(first_basemen_X, first_basemen_Y)
second_basemen_lr.fit(second_basemen_X, second_basemen_Y)
third_basemen_lr.fit(third_basemen_X, third_basemen_Y)
shortstops_lr.fit(shortstops_X, shortstops_Y)
outfielders_lr.fit(outfielders_X, outfielders_Y)
designated_hitters_lr.fit(designated_hitters_X, designated_hitters_Y)

#orthogonal projection predictions
starters_pred = starters_lr.predict(starters_X)
relievers_pred = relievers_lr.predict(relievers_X)
catchers_pred = catchers_lr.predict(catchers_X)
first_basemen_pred = first_basemen_lr.predict(first_basemen_X)
second_basemen_pred = second_basemen_lr.predict(second_basemen_X)
third_basemen_pred = third_basemen_lr.predict(third_basemen_X)
shortstops_pred = shortstops_lr.predict(shortstops_X)
outfielders_pred = outfielders_lr.predict(outfielders_X)
designated_hitters_pred = designated_hitters_lr.fit_predict(designated_hitters_X)

#adding predictions to dataframes
starters_output = Fangraphs.starters.drop(columns = ['K/BB', 'SIERA', 'xFIP', 'FBv', 'WAR'])
starters_output["Predicted Salary"] = starters_pred.tolist()
relievers_output = Fangraphs.relievers.drop(columns = ['K/BB', 'SIERA', 'xFIP', 'FBv', 'WAR'])
relievers_output["Predicted Salary"] = relievers_pred.tolist()
catchers_output = Fangraphs.catchers.drop(columns = ['HR', 'BB/K', 'xwOBA', 'wRC+', 'Spd', 'WAR', 'DRS', 'FRM'])
catchers_output["Predicted Salary"] = catchers_pred.tolist()
first_basemen_output = Fangraphs.first_basemen.drop(columns = ['HR', 'BB/K', 'xwOBA', 'wRC+', 'Spd', 'WAR', 'DRS', 'OAA'])
first_basemen_output["Predicted Salary"] = first_basemen_pred.tolist()
second_basemen_output = Fangraphs.second_basemen.drop(columns = ['HR', 'BB/K', 'xwOBA', 'wRC+', 'Spd', 'WAR', 'DRS', 'OAA'])
second_basemen_output["Predicted Salary"] = second_basemen_pred.tolist()
third_basemen_output = Fangraphs.third_basemen.drop(columns = ['HR', 'BB/K', 'xwOBA', 'wRC+', 'Spd', 'WAR', 'DRS', 'OAA'])
third_basemen_output["Predicted Salary"] = third_basemen_pred.tolist()
shortstops_output = Fangraphs.shortstops.drop(columns = ['HR', 'BB/K', 'xwOBA', 'wRC+', 'Spd', 'WAR', 'DRS', 'OAA'])
shortstops_output["Predicted Salary"]  = shortstops_pred.tolist()
outfielders_output = Fangraphs.outfielders.drop(columns = ['HR', 'BB/K', 'xwOBA', 'wRC+', 'Spd', 'WAR', 'DRS', 'OAA'])
outfielders_output["Predicted Salary"] = outfielders_pred.tolist()
designated_hitters_output = Fangraphs.designated_hitters.drop(columns = ['HR', 'BB/K', 'xwOBA', 'wRC+', 'Spd', 'WAR'])
designated_hitters_output["Predicted Salary"] = designated_hitters_pred.tolist()

#convert to int datatype
starters_output["Predicted Salary"] = starters_output["Predicted Salary"].astype(int)
relievers_output["Predicted Salary"] = relievers_output["Predicted Salary"].astype(int)
catchers_output["Predicted Salary"] = catchers_output["Predicted Salary"].astype(int)
first_basemen_output["Predicted Salary"] = first_basemen_output["Predicted Salary"].astype(int)
second_basemen_output["Predicted Salary"] = second_basemen_output["Predicted Salary"].astype(int)
third_basemen_output["Predicted Salary"] = third_basemen_output["Predicted Salary"].astype(int)
shortstops_output["Predicted Salary"] = shortstops_output["Predicted Salary"].astype(int)
outfielders_output["Predicted Salary"] = outfielders_output["Predicted Salary"].astype(int)
designated_hitters_output["Predicted Salary"] = designated_hitters_output["Predicted Salary"].astype(int)

#Value Indeces
starters_output["Value Index"] = ((starters_output["Predicted Salary"]/starters_output["Actual Salary"]) * 100)
relievers_output["Value Index"] = ((relievers_output["Predicted Salary"]/relievers_output["Actual Salary"]) * 100)
catchers_output["Value Index"] = ((catchers_output["Predicted Salary"]/catchers_output["Actual Salary"]) * 100)
first_basemen_output["Value Index"] = ((first_basemen_output["Predicted Salary"]/first_basemen_output["Actual Salary"]) * 100)
second_basemen_output["Value Index"] = ((second_basemen_output["Predicted Salary"]/second_basemen_output["Actual Salary"]) * 100)
third_basemen_output["Value Index"] = ((third_basemen_output["Predicted Salary"]/third_basemen_output["Actual Salary"]) * 100)
shortstops_output["Value Index"] = ((shortstops_output["Predicted Salary"]/shortstops_output["Actual Salary"]) * 100)
outfielders_output["Value Index"] = ((outfielders_output["Predicted Salary"]/outfielders_output["Actual Salary"]) * 100)
designated_hitters_output["Value Index"] = ((designated_hitters_output["Predicted Salary"]/designated_hitters_output["Actual Salary"]) * 100)

#combine and sort
all_players = pd.DataFrame(np.vstack((starters_output.to_numpy(), relievers_output.to_numpy(), catchers_output.to_numpy(), first_basemen_output.to_numpy(), second_basemen_output.to_numpy(), third_basemen_output.to_numpy(), shortstops_output.to_numpy(), outfielders_output.to_numpy(), designated_hitters_output.to_numpy())))
all_players.set_axis(['Name','Team','Pos','Age','Actual Salary','Predicted Salary','Value Index'], axis = 1, copy=False)
all_players.sort_values(by = ['Value Index'], ascending = False, inplace = True, kind = 'mergesort', axis = 0)
print(all_players)
all_players.to_csv('all_players.csv')