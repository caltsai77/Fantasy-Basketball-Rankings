# Author: Caleb Tsai
# Main file that creates Season objects for a given user
from season import Season

def main():
    # Initialize season as well as default season
    currYear = '22-23'
    availableSeasons = ['03-04', '04-05', '05-06', '06-07', '07-08', '08-09', '09-10', '10-11', '11-12', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18', '18-19', '19-20', '20-21', '21-22']
    season = input('\nPlease input the season in {YY-YY}. Available seasons range from 03-04 to 21-22\nSeason: ')
    # Validate inputted season
    if season not in availableSeasons:
        print(f'ERROR: Your inputted season of {season} is not available: season set to 2021-22')
        season = '21-22'
    
    #----------------------------------------------------------------------------------------------------------------------
    # If season is not the current calendar season, ask user for elite player (Top 188) data or all player data
    if season != currYear:
        start = True
        # Loop until user inputs either "e" (elite) or "a" (all)
        while True:
            if start:
                letter = input(f'\nThere are 2 available data types to use:\nEnter "e" to use data of ELITE (Top 188) players.\nEnter "a" to use data of ALL players.\nChoice: ')
                start = False
            else:
                letter = input(f'Choice: ')
            if letter == 'e' or letter == 'a':
                break
            else:
                print(f'\nInvalid input! Please input either "e" (ELITE) or "a" (ALL)')
    
    # Set dataType to either 'elite' or 'all'
    dataType = 'Elite'
    if not (letter == 'e'):
        dataType = 'All'

    # Continue loop until user chooses to leave program
    while True:
        # Create and initialize season object
        user = Season(season, dataType)
        user.initialize(user.ranks)

        # Menu of Available Options for User
        print(f'\nAvailable Options (Season: 20{season}, Player Data: {dataType})\n\n1. Display Top Players (All Categories)')
        print(f'2. Display Top Players (Select Categories to Keep)')
        print(f'3. Display Season Averages (9 Categories)')
        print(f'4. End program')

        #----------------------------------------------------------------------------------------------------------------------
        # User input validation for choice
        while True:
            choice = input('\nPlease enter one choice (from 1 to 4): ')
            try:  
                choice = int(choice)  
            except ValueError:
                print(f'{choice} is NOT a valid number. Please input one valid number from 1 to 4')
                continue
            if 1 <= choice <= 4:
                break
            else:
                print(f'{choice} is outside the appropriate range. Number MUST be from 1 to 4')

        #----------------------------------------------------------------------------------------------------------------------
        # Choice 1: Display top x players 
        if choice == 1:
            # Validate user input (number of players to be displayed)
            while True:
                num = input(f'\n1. Display Top Players (All Categories)\nPlease enter the number of players to be displayed (1 to {len(user.ranks)}): ')
                try:  
                    num = int(num)  
                except ValueError:
                    print(f'{num} is NOT a valid number. Please input a valid number from 1 to {len(user.ranks)}')
                    continue
                if 1 <= num <= len(user.ranks.index):
                    break
                else:
                    print(f'{num} is outside the appropriate range. Number MUST be from 1 to {len(user.ranks)}')
            user.displayTopOverall(user.ranks, num, user.season)

        #----------------------------------------------------------------------------------------------------------------------
        # Choice 2: Display top x players by certain filtered categories
        elif choice == 2:
            # Validate user input (number of players to be displayed) before asking for number of categories
            while True:
                num = input(f'\n2. Display Top Players (Select Categories to Keep)\nPlease enter the number of players to be displayed (1 to {len(user.ranks)}): ')
                try:  
                    num = int(num)  
                except ValueError:
                    print(f'{num} is NOT a valid number. Please input a valid number from 1 to {len(user.ranks)}')
                    continue
                if 1 <= num <= len(user.ranks.index):
                    break
                else:
                    print(f'{num} is outside the appropriate range. Number MUST be from 1 to {len(user.ranks)}')
            
            #----------------------------------------------------------------------------------------------------------------------
            # Obtain number of desired categories
            while True:
                numCats = input(f'\nPlease input the total number of categories to KEEP (1 to 8): ')
                try:
                    numCats = int(numCats)
                except ValueError:
                    print(f'{numCats} is NOT a valid number. Please input a valid number from 1 to 8 (categories to KEEP)')
                    continue
                if 1 <= numCats <= 8:
                    break
                else:
                    print(f'{numCats} is outside the appropriate range. Number MUST be from 1 to 8 (categories to KEEP)')

            #----------------------------------------------------------------------------------------------------------------------------------------------------------------------
            # Obtain each individual category to keep
            code = {1:'Points', 2:'3-Pointers Made', 3:'Rebounds', 4:'Assists', 5:'Steals', 6:'Blocks', 7:'Field Goal Percentage', 8:'Free Throw Percentage', 9:'Turnovers'}
            codeStr = f'1: {code[1]}\n2: {code[2]}\n3: {code[3]}\n4: {code[4]}\n5: {code[5]}\n6: {code[6]}\n7: {code[7]}\n8: {code[8]}\n9: {code[9]}'
            userCats = []
            for i in range(numCats):
                while True:
                    # Initial prompt
                    if i == 0:
                        currCat = input(f'\nMap (Input: Category)\n{codeStr}\n\nPlease input category to keep ({len(userCats)}/{numCats} chosen): ')
                    # Prompt that includes categories already chosen
                    else:
                        chosen = ''
                        if len(userCats) == 1:
                            chosen += (f'{userCats[0]} ({code[userCats[0]]})')
                        else:
                            chosen += (f'{userCats[0]} ({code[userCats[0]]})')
                            for cat in userCats[1:]:
                                chosen += (f', {cat} ({code[cat]})')
                        currCat = input(f'\nMap (Input: Category)\n{codeStr}\n\nCategories Chosen: {chosen}\nPlease input category to keep ({len(userCats)}/{numCats} chosen): ')
                    try:
                        currCat = int(currCat)
                    except ValueError:
                        print(f'{codeStr}\n\n{currCat} is NOT a valid number. Please input a valid number from 1 to 9 (categories to KEEP)')
                        continue
                    if 1 <= currCat <= 9:
                        if currCat in userCats:
                            print(f'{codeStr}\n\n{code[currCat]} ({currCat}) has been selected. Choose another category!')
                        else:
                            break
                    else:
                        print(f'{codeStr}\n\n{currCat} is outside the appropriate range. Number MUST be from 1 to 9 (categories to KEEP)')
                userCats.append(currCat)
            #----------------------------------------------------------------------------------------------------------------------------------------------------------------------
            # Print chosen categories to user
            chosen = ''
            if len(userCats) == 1:
                print(f'\nCategory Chosen (1): {code[userCats[0]]}')
            else:
                chosen += (f'{code[userCats[0]]}')
                for cat in userCats[1:]:
                    chosen += (f', {code[cat]}')
                print(f'\nCategories Chosen ({len(userCats)}): {chosen}')
            
            # Determine sorting criteria (adjusted value or value differential)
            

            # Call function
            user.displayTopKeepCats(user.ranks, num, user.season, userCats)
        #----------------------------------------------------------------------------------------------------------------------
        # Choice 3: Display Season Averages (9 Cats)
        elif choice == 3:
            user.displaySeasonAvgs(user.ranks, user.season)
        
        #----------------------------------------------------------------------------------------------------------------------
        # Choice 4: End Program
        else:
            print(f'\nGoodbye, have a great day!')
            quit()
        
        #----------------------------------------------------------------------------------------------------------------------
        # Ask user if they would like to return to menu
        start = True
        while True:
            if start:
                option = input(f'\nAwesome! To select another option in the menu, input "y". To leave the program, input "n".\nChoice: ')
                start = False
            else:
                option = input(f'Choice: ')
            if option == 'y' or option == 'n':
                break
            else:
                print(f'\nInvalid input! Please input either "y" (YES) or "n" (NO)')
        # User wants to leave program
        if option == 'n':
            print(f'\nGoodbye, have a great day!')
            quit()
        # Ask user if they want to change the season
        start = True
        while True:
            if start:
                keepSeason = input(f'\nWould you like to change the current 20{season} season? ("y": yes, "n": no) \nChoice: ')
                start = False
            else:
                keepSeason = input(f'Choice: ')
            if keepSeason == 'y' or keepSeason == 'n':
                break
            else:
                print(f'\nInvalid input! Please input either "y" (YES) or "n" (NO)')
        # User wants to change the season
        if keepSeason == 'y':
            newSeason = input('\nPlease enter the new season in the format: YY-YY (Ex: 21-22): ')
            if newSeason not in availableSeasons:
                print(f'Your inputted season of {season} is not available in the database: the season will remain the same: 20{season}')
            else:
                season = newSeason

# Main, called if ran directly on 'main.py'
if __name__ == "__main__":
    main()