# Author: Caleb Tsai
import pandas as pd
pd.options.mode.chained_assignment = None
from tabulate import tabulate
# if __name__ == "__main__":
class Season:
    season = ''
    ranks = pd.DataFrame()
    # Constructor: season either default or user inputted into dataframe
    def __init__(self, season, dataType):
        # Path is either elite or all player data
        if dataType == 'Elite':
            path = './Data_Elite/CSV/'
        else:
            path = './Data_All/CSV/'
        self.season += season
        self.ranks = pd.read_csv(path+self.season+'.csv', index_col=False).drop(columns=['Round', 'Inj'])

    def initialize(self, ranks):
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
        ranks['Value'] = ranks['Value'].round(decimals=2)
        ranks['pV'] = ranks['pV'].round(decimals=2)
        ranks['3V'] = ranks['3V'].round(decimals=2)
        ranks['rV'] = ranks['rV'].round(decimals=2)
        ranks['aV'] = ranks['aV'].round(decimals=2)
        ranks['sV'] = ranks['sV'].round(decimals=2)
        ranks['bV'] = ranks['bV'].round(decimals=2)
        ranks['fg%V'] = ranks['fg%V'].round(decimals=2)
        ranks['ft%V'] = ranks['ft%V'].round(decimals=2)
        ranks['toV'] = ranks['toV'].round(decimals=2)
    #----------------------------------------------------------------------------------------------------------------------
    # Print out top x ranked players overall
    def displayTopOverall(self, ranks, num, season):
        ranks.set_index('Rank', inplace=True)
        top = ranks.head(num).drop(columns=['pV', '3V', 'rV', 'aV', 'sV', 'bV', 'fg%V', 'ft%V', 'toV'])

        # Print dataframe (markdown, plain-text, psql, github, pretty, HTML), export to 'out.csv' file
        print(f'\nTop Players Overall in the 20{season} season')
        print(tabulate(top, headers='keys', tablefmt='pretty'))
        top.to_csv('out.csv', sep=',')

    #----------------------------------------------------------------------------------------------------------------------
    def displayTopKeepCats(self, ranks, numPlayers, season, cats):
        codeName = {1:'Points', 2:'3-Pointers Made', 3:'Rebounds', 4:'Assists', 5:'Steals', 6:'Blocks', 7:'Field Goal Percentage', 8:'Free Throw Percentage', 9:'Turnovers'}
        # Heading of output
        chosen = ''
        if len(cats) == 1:
            print(f'\nTop Players Based On {len(cats)} Category ({codeName[cats[0]]}) in the 20{season} season:')
        else:
            chosen += (f'{codeName[cats[0]]}')
            for cat in cats[1:]:
                chosen += (f', {codeName[cat]}')
            print(f'\nTop Players Based On {len(cats)} Categories ({chosen}) in the 20{season} season:')
        
        # Dictionary to map to values categories in ranks df
        codeLabel = {1:'pV', 2:'3V', 3:'rV', 4:'aV', 5:'sV', 6:'bV', 7:'fg%V', 8:'ft%V', 9:'toV'}

        # Rename column name from 'Value' to 'LeagueV'
        ranks.rename(columns={'Value':'LeagueV'}, inplace = True)

        # Add empty adjValue column after 'Rank' column, empty valueDiff column after 'LeagueV' column
        ranks.insert(1, 'AdjV', 0.0)
        ranks.insert(3, 'KeepV', 0.0)

        # Assign value in 'AdjV' to sum of _V categories desired divided by the # of categories
        numCats = len(cats)
        if numCats == 1:
            ranks['AdjV'] = round(ranks[codeLabel[cats[0]]], 2)
        elif numCats == 2:
            ranks['AdjV'] = round(((ranks[codeLabel[cats[0]]] + ranks[codeLabel[cats[1]]]) / len(cats)), 2)
        elif numCats == 3:
            ranks['AdjV'] = round(((ranks[codeLabel[cats[0]]] + ranks[codeLabel[cats[1]]] + ranks[codeLabel[cats[2]]]) / len(cats)), 2)
        elif numCats == 4:
            ranks['AdjV'] = round(((ranks[codeLabel[cats[0]]] + ranks[codeLabel[cats[1]]] + ranks[codeLabel[cats[2]]] + ranks[codeLabel[cats[3]]]) / len(cats)), 2)
        elif numCats == 5:
            ranks['AdjV'] = round(((ranks[codeLabel[cats[0]]] + ranks[codeLabel[cats[1]]] + ranks[codeLabel[cats[2]]] + ranks[codeLabel[cats[3]]] + ranks[codeLabel[cats[4]]]) / len(cats)), 2)
        elif numCats == 6:
            ranks['AdjV'] = round(((ranks[codeLabel[cats[0]]] + ranks[codeLabel[cats[1]]] + ranks[codeLabel[cats[2]]] + ranks[codeLabel[cats[3]]] + ranks[codeLabel[cats[4]]] + ranks[codeLabel[cats[5]]]) / len(cats)), 2)
        elif numCats == 7:
            ranks['AdjV'] = round(((ranks[codeLabel[cats[0]]] + ranks[codeLabel[cats[1]]] + ranks[codeLabel[cats[2]]] + ranks[codeLabel[cats[3]]] + ranks[codeLabel[cats[4]]] + ranks[codeLabel[cats[5]]] + ranks[codeLabel[cats[6]]]) / len(cats)), 2)
        elif numCats == 8:
            ranks['AdjV'] = round(((ranks[codeLabel[cats[0]]] + ranks[codeLabel[cats[1]]] + ranks[codeLabel[cats[2]]] + ranks[codeLabel[cats[3]]] + ranks[codeLabel[cats[4]]] + ranks[codeLabel[cats[5]]] + ranks[codeLabel[cats[6]]] + ranks[codeLabel[cats[7]]]) / len(cats)), 2)
        else:
            ranks['AdjV'] = ranks['LeagueV']
        # Drop value columns bc they're unneeded now
        ranks = ranks.drop(columns=['pV', '3V', 'rV', 'aV', 'sV', 'bV', 'fg%V', 'ft%V', 'toV'])
        # Assign value in 'KeepV' to be difference between AdjV and LeagueV
        ranks.loc[:, 'KeepV'] = round((ranks.loc[:, 'AdjV'] - ranks.loc[:, 'LeagueV']), 2)

        # Sort by adjusted value descending, update corresponding rank
        ranks = ranks.sort_values(by=['AdjV'], ascending=False)
        ranks.insert(0, 'AdjRank', range(1, 1+len(ranks)))
        ranks.rename(columns={'Rank':'LeagueRank'}, inplace = True)
        ranks.set_index('AdjRank', inplace=True)
        top = ranks.head(numPlayers)
        
        # Print out updated rankings by category and export
        print(tabulate(top, headers='keys', tablefmt='pretty'))
        top.to_csv('out.csv', sep=',', index=False)

    #----------------------------------------------------------------------------------------------------------------------
    # Print out season averages across all 9 categories for current season
    def displaySeasonAvgs(self, ranks, season):
        # Calculate Category Averages across p, 3, r, a , s, b, fg%, ft%, t
        # averages -> [category: [avg, player]]
        averages = {key: [] for key in ['Points', '3-Pointers Made', 'Rebounds', 'Assists', 'Steals', 'Blocks', 'Field Goal Percentage', 'Free Throw Percentage', 'Turnovers']}

        # Identify row where cat's value is closest to 0.0, assign avg of cat to corresponding stat
        # Points
        pointsAvgPlayer = ranks.iloc[(ranks['pV']-0.0).abs().argsort()[:1]]
        pointsAvgName = pointsAvgPlayer['Name'].tolist()
        pointsAvg = pointsAvgPlayer['p/g'].tolist()
        averages['Points'].append(pointsAvg[0])
        averages['Points'].append(pointsAvgName[0])
        # 3s Made
        threesAvgPlayer = ranks.iloc[(ranks['3V']-0.0).abs().argsort()[:1]]
        threesAvgName = threesAvgPlayer['Name'].tolist()
        threesAvg = threesAvgPlayer['3/g'].tolist()
        averages['3-Pointers Made'].append(threesAvg[0])
        averages['3-Pointers Made'].append(threesAvgName[0])
        # Rebounds
        reboundsAvgPlayer = ranks.iloc[(ranks['rV']-0.0).abs().argsort()[:1]]
        reboundsAvgName = reboundsAvgPlayer['Name'].tolist()
        reboundsAvg = reboundsAvgPlayer['r/g'].tolist()
        averages['Rebounds'].append(reboundsAvg[0])
        averages['Rebounds'].append(reboundsAvgName[0])
        # Assists
        assistsAvgPlayer = ranks.iloc[(ranks['aV']-0.0).abs().argsort()[:1]]
        assistsAvgName = assistsAvgPlayer['Name'].tolist()
        assistsAvg = assistsAvgPlayer['a/g'].tolist()
        averages['Assists'].append(assistsAvg[0])
        averages['Assists'].append(assistsAvgName[0])
        # Steals
        stealsAvgPlayer = ranks.iloc[(ranks['sV']-0.0).abs().argsort()[:1]]
        stealsAvgName = stealsAvgPlayer['Name'].tolist()
        stealsAvg = stealsAvgPlayer['s/g'].tolist()
        averages['Steals'].append(stealsAvg[0])
        averages['Steals'].append(stealsAvgName[0])
        # Blocks
        blocksAvgPlayer = ranks.iloc[(ranks['bV']-0.0).abs().argsort()[:1]]
        blocksAvgName = blocksAvgPlayer['Name'].tolist()
        blocksAvg = blocksAvgPlayer['b/g'].tolist()
        averages['Blocks'].append(blocksAvg[0])
        averages['Blocks'].append(blocksAvgName[0])
        # Field Goal Percentage
        fieldGoalAvgPlayer = ranks.iloc[(ranks['fg%V']-0.0).abs().argsort()[:1]]
        fieldGoalAvgName = fieldGoalAvgPlayer['Name'].tolist()
        fieldGoalAvg = fieldGoalAvgPlayer['fg%'].tolist()
        averages['Field Goal Percentage'].append(fieldGoalAvg[0])
        averages['Field Goal Percentage'].append(fieldGoalAvgName[0])
        # Free Throw Percentage
        freeThrowAvgPlayer = ranks.iloc[(ranks['ft%V']-0.0).abs().argsort()[:1]]
        freeThrowAvgName = freeThrowAvgPlayer['Name'].tolist()
        freeThrowAvg = freeThrowAvgPlayer['ft%'].tolist()
        averages['Free Throw Percentage'].append(freeThrowAvg[0])
        averages['Free Throw Percentage'].append(freeThrowAvgName[0])
        # Turnovers
        turnoversAvgPlayer = ranks.iloc[(ranks['toV']-0.0).abs().argsort()[:1]]
        turnoversAvgName = turnoversAvgPlayer['Name'].tolist()
        turnoversAvg = turnoversAvgPlayer['to/g'].tolist()
        averages['Turnovers'].append(turnoversAvg[0])
        averages['Turnovers'].append(turnoversAvgName[0])

        # Add average stat, player who represents that chat into dataFrame
        print(f'\nLeague Averages (Categories) for the 20{season} season:')
        averagesDF = pd.DataFrame()
        for stat in averages.keys():
            averagesDF[stat] = [averages[stat][0], averages[stat][1]]
        averagesDF.set_index([['Stat', 'Player']], inplace=True)
        
        # Print and export
        print(tabulate(averagesDF, headers='keys', tablefmt='pretty'))
        averagesDF.to_csv('out.csv', sep=',')
        
        #----------------------------------------------------------------------------------------------------------------------

        # Export data frame into CSV file, print nicely
        # print(tabulate(__, headers='keys', tablefmt='pretty'))
        # top.to_csv('out.csv', sep=',')

# Only run this code if ran directly on 'season.py'
if __name__ == "__main__":
    # season = '19-20'
    # season = '20-21'
    season = '21-22'
    user = Season(season)
    ranks = user.ranks
    numTop = 10
    cats = [1, 2]
    
    # Initialize
    user.initialize(ranks)

    # Choice 1: Display Top Players Overall
    # user.displayTopOverall(user.ranks, numTop, season)

    # Choice 2: Display Top Players Adjusted by Keeping Categories
    user.displayTopKeepCats(ranks, numTop, season, cats)

    # Choice 3: Display season averages across all 9 cats
    # user.displaySeasonAvgs(ranks, season)

# Below code is ran if not running directly on file (imported to another file)
# else:
#     print('Not the original file')