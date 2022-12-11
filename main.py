# Author: Caleb Tsai
import pandas as pd
season = '21-22' + '.csv'

# Parse .csv file into dataframe, drop unneeded columns
ranks = pd.read_csv(season)
ranks = ranks.drop(columns=['Round', 'Inj'])

# Round every appropriate statistic to appropriate decimal points
# Average Stats: m/g, p/g, 3/g, r/g, a/g, s/g, b/g, fg%, fga/g, ft%, fta/g, to/g
ranks['m/g'] = ranks['m/g'].round(decimals=1)
ranks['p/g'] = ranks['p/g'].round(decimals=1)
ranks['3/g'] = ranks['3/g'].round(decimals=1)
ranks['r/g'] = ranks['r/g'].round(decimals=1)
ranks['a/g'] = ranks['a/g'].round(decimals=1)
ranks['s/g'] = ranks['s/g'].round(decimals=1)
ranks['b/g'] = ranks['b/g'].round(decimals=1)
ranks['fg%'] = ranks['fg%'].round(decimals=3)
ranks['fga/g'] = ranks['fga/g'].round(decimals=1)
ranks['ft%'] = ranks['ft%'].round(decimals=3)
ranks['fta/g'] = ranks['fta/g'].round(decimals=1)
ranks['to/g'] = ranks['to/g'].round(decimals=1)
# Value Stats: Value, pV, 3V, rV, aV, sV, bV, fg%V, ft%V, toV
ranks['pV'] = ranks['pV'].round(decimals=2)
ranks['3V'] = ranks['3V'].round(decimals=2)
ranks['rV'] = ranks['rV'].round(decimals=2)
ranks['aV'] = ranks['aV'].round(decimals=2)
ranks['sV'] = ranks['sV'].round(decimals=2)
ranks['bV'] = ranks['bV'].round(decimals=2)
ranks['fg%V'] = ranks['fg%V'].round(decimals=2)
ranks['ft%V'] = ranks['ft%V'].round(decimals=2)
ranks['toV'] = ranks['toV'].round(decimals=2)

# Print out top 5 ranked players
top5rows = ranks.head()
print(top5rows)

# Calculate Category Averages across p, 3, r, a , s, b, fg%, ft%, t
averages = {key: 0.0 for key in ['p', '3', 'r', 'a', 's', 'b', 'fg%', 'ft%', 't']}
print(averages)

# Identify row where cat's value is closest to 0.0, assign avg of cat to corresponding stat
