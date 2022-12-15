# Author: Caleb Tsai
import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None
from tabulate import tabulate

# Season class
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

     #-----------------------------------------------------------------------------------------------------------------------------
    # Round every appropriate statistic to appropriate decimal points
    def initialize(self, ranks):
        # Average Stats: m/g, p/g, 3/g, r/g, a/g, s/g, b/g, fg%, fga/g, ft%, fta/g, to/g
        ranks['m/g'] = round(ranks['m/g'], 1)
        ranks['p/g'] = round(ranks['p/g'], 1)
        ranks['3/g'] = round(ranks['3/g'], 1)
        ranks['r/g'] = round(ranks['r/g'], 1)
        ranks['a/g'] = round(ranks['a/g'], 1)
        ranks['s/g'] = round(ranks['s/g'], 1)
        ranks['b/g'] = round(ranks['b/g'], 1)
        ranks['fg%'] = round(ranks['fg%'], 3)
        ranks['fga/g'] = round(ranks['fga/g'], 1)
        ranks['ft%'] = round(ranks['ft%'], 3)
        ranks['fta/g'] = round(ranks['fta/g'], 1)
        ranks['to/g'] = round(ranks['to/g'], 1)

        # Value Stats: Value, pV, 3V, rV, aV, sV, bV, fg%V, ft%V, toV
        ranks['Value'] = round(ranks['Value'], 2)
        ranks['pV'] = round(ranks['pV'], 2)
        ranks['3V'] = round(ranks['3V'], 2)
        ranks['rV'] = round(ranks['rV'], 2)
        ranks['aV'] = round(ranks['aV'], 2)
        ranks['sV'] = round(ranks['sV'], 2)
        ranks['bV'] = round(ranks['bV'], 2)
        ranks['fg%V'] = round(ranks['fg%V'], 2)
        ranks['ft%V'] = round(ranks['ft%V'], 2)
        ranks['toV'] = round(ranks['toV'], 2)

    #-----------------------------------------------------------------------------------------------------------------------------
    # Format every appropriate statistic to appropriate decimal points
    def formatAll(self, ranks, colFormat):
        # Format appropriate columns based on colFormat dictionary -> {column:decimals}
        for col, decimal in colFormat.items():
            if decimal == 2:
                # Add '+' before positive numbers
                if col == 'KeepV':
                    ranks[col] = np.where( (ranks[col] > 0.0), (ranks[col].apply(lambda x: "+{:.2f}".format(x))), (ranks[col].apply(lambda x: "{:.2f}".format(x))))
                else:
                    ranks[col] = ranks[col].apply(lambda x: "{:.2f}".format(x))
            else:
                ranks[col] = ranks[col].apply(lambda x: "{:.3f}".format(x))

    #----------------------------------------------------------------------------------------------------------------------
    # Print out top x ranked players overall
    def displayTopOverall(self, ranks, num, season):
        # Format percentages
        colFormat = {'fg%':3, 'ft%':3, 'Value':2}
        self.formatAll(ranks, colFormat)
        ranks.set_index('Rank', inplace=True)
        top = ranks.head(num).drop(columns=['pV', '3V', 'rV', 'aV', 'sV', 'bV', 'fg%V', 'ft%V', 'toV'])

        # Print dataframe (markdown, plain-text, psql, github, pretty, HTML), export to 'out.csv' file
        print(f'\nTop Players Overall in the 20{season} season')
        print(tabulate(top, headers='keys', tablefmt='pretty'))
        top.to_csv('out.csv', sep=',')

    #----------------------------------------------------------------------------------------------------------------------
    def displayTopKeepCats(self, ranks, numPlayers, season, cats, criteria):
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
        
        # Round 'AdjV' to 2 decimals, assign value in 'KeepV' to be difference between AdjV and League, drop value columns (unneeded now)
        ranks['AdjV'] = round(ranks['AdjV'], 2)
        ranks['KeepV'] = round((ranks['AdjV'] - ranks['LeagueV']), 2)
        ranks = ranks.drop(columns=['pV', '3V', 'rV', 'aV', 'sV', 'bV', 'fg%V', 'ft%V', 'toV'])

        # Sort by adjusted value descending
        if criteria == 'Adjusted Value':
            ranks = ranks.sort_values(by=['AdjV'], ascending=False)
        # Sort by value differential descending
        else:
            ranks = ranks.sort_values(by=['KeepV'], ascending=False)
        
        # Update corresponding rank
        ranks.insert(0, 'AdjRank', range(1, 1+len(ranks)))
        ranks.rename(columns={'Rank':'LeagueRank'}, inplace = True)
        ranks.set_index('AdjRank', inplace=True)

        # Format value columns
        colFormat = {'LeagueV':2, 'KeepV':2, 'AdjV':2, 'fg%':3, 'ft%':3}
        self.formatAll(ranks, colFormat)
        top = ranks.head(numPlayers)
        
        # Print out updated rankings by category and export
        print(tabulate(top, headers='keys', tablefmt='pretty'))
        top.to_csv('out.csv', sep=',', index=False)

    #----------------------------------------------------------------------------------------------------------------------
    # Print out season averages across all 9 categories for current season
    def displaySeasonAvgs(self, ranks, season):
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
# Only run this code if ran directly on 'season.py'
# if __name__ == "__main__":
    # season = '19-20'
    # season = '20-21'
    # season = '21-22'
    # user = Season(season, 'All')
    # ranks = user.ranks
    # numTop = 10
    # cats = [1, 2]
    # criteria = 'Adjusted Value'
    # criteria = 'Value Differential'
    
    # Initialize
    # user.initialize(ranks)

    # Choice 1: Display Top Players Overall
    # user.displayTopOverall(user.ranks, numTop, season)

    # Choice 2: Display Top Players Adjusted by Keeping Categories
    # user.displayTopKeepCats(ranks, numTop, season, cats, criteria)

    # Choice 3: Display season averages across all 9 cats
    # user.displaySeasonAvgs(ranks, season)