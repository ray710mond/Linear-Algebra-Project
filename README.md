# Linear-Algebra-Project

Linear Algebra in “Moneyball”

By Raymond Provost


Goal: Evaluate the value of an MLB player with respect to their current salary

Step 1: Separate Players into 2 categories: Pitchers and Position Players

Step 2: Decide stats to consider for evaluation (FanGraphs)
Pitchers: Age, K/BB, SIERA, xFIP, FBv, WAR
Min 100 IP (124 Starters) 
Min 50 IP (144 Relievers)
Compare starters and relievers separately
Hitters: Age, HR, BB/K, xwOBA, wRC+, Spd, WAR, DRS, OAA, Framing
Min 300 PAs (about 30 players per position)
Compare each position separately (Outfielders together)
Add Framing and remove OAA for catchers only
Remove all defensive metrics (DRS, OAA, Framing) for DHs
Stats from the 2022 season

Step 3: Export stat tables from Fangraphs to CSVs in Excel
Edit out unnecessary information
Combine Offensive and Defensive Stats

Step 4: Set up multiple linear regression with Numpy, Pandas, and Scikit Learn
Least-squares for line/plane/higher-dimensional object of best fit to data
Extract information from the best fit to determine which stats were more valuable in predicting salaries

Step 5: Use orthogonal projection to predict a salary (dependent output variable) based on all of the independent input variables

Step 6: Find a player value index ( (predicted / actual) * 100 )

Step 7: Rank by position and total leaderboards sorted by value index

Question to all: Given the applications of statistics and linear algebra in predicting MLB salaries, what other useful metrics do you think could be predicted with similar methods?

