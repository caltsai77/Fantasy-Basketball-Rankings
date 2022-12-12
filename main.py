# Author: Caleb Tsai
from season import Season
def main():
    # Ask user if they want to start
    # name = input('Enter name: ')
    # isYes = input(f'Hi {name}! To begin, please input "Y"')
    
    # if isYes == "Y":
    #     print(f'Awesome! We can get started')
    # else:
    #     print(f'Goodbye, have a great day!')
    #     quit()

    # Initialize season as well as default season
    availableSeasons = ['19-20', '20-21', '21-22']
    season = input('Please enter the season in the format: YY-YY (Ex: 21-22): ')
    if season not in availableSeasons:
        print(f'Your inputted season of {season} is not available in the database: default season is 2021-22')
        season = '21-22'
    # season = '21-22'

    # Create and initialize season object
    user = Season(season)
    user.initialize(user.ranks)

    #----------------------------------------------------------------------------------------------------------------------
    # Menu of Available Options for User
    print(f'\nAvailable Options (Season: 20{season}):\n\n1. Display Top Players (Overall)')
    print(f'2. Display Top Players (Given User-Selected Categories to Keep)')
    print(f'3. Display Season Averages (9 Categories)')

    #----------------------------------------------------------------------------------------------------------------------
    # User input validation for choice
    while True:
        choice = input('\nPlease enter one choice (from 1 to 3): ')
        try:  
            choice = int(choice)  
        except ValueError:
            print(f'{choice} is NOT a valid number. Please input one valid number from 1 to 3')
            continue
        if 1 <= choice <= 3:
            break
        else:
            print(f'{choice} is outside the appropriate range. Number MUST be from 1 to 3')

    #----------------------------------------------------------------------------------------------------------------------
    # Choice 1: Display top x players 
    if choice == 1:
        # Validate user input (number of players to be displayed)
        while True:
            num = input(f'\n1. Display Top Players (Overall)\nPlease enter the number of players to be displayed (1 to 188): ')
            try:  
                num = int(num)  
            except ValueError:
                print(f'{num} is NOT a valid number. Please input a valid number from 1 to 188')
                continue
            if 1 <= num <= 188:
                break
            else:
                print(f'{num} is outside the appropriate range. Number MUST be from 1 to 188')
        user.displayTopOverall(user.ranks, num, user.season)

    #----------------------------------------------------------------------------------------------------------------------
    # Choice 2: Display top x players by certain filtered categories
    elif choice == 2:
        # Obtain number of desired categories
        print(f'\n2. Display Top Players (Keep User-Selected Categories)')
        while True:
            numCats = input(f'Please input the total number of categories to KEEP (1 to 9): ')
            try:
                numCats = int(numCats)
            except ValueError:
                print(f'{numCats} is NOT a valid number. Please input a valid number from 1 to 9 (categories to KEEP)')
                continue
            if 1 <= numCats <= 9:
                break
            else:
                print(f'{numCats} is outside the appropriate range. Number MUST be from 1 to 9 (categories to KEEP)')
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
            print(f'\nCategory Chosen: {code[userCats[0]]}')
        else:
            chosen += (f'{code[userCats[0]]}')
            for cat in userCats[1:]:
                chosen += (f', {code[cat]}')
            print(f'\nCategories Chosen: {chosen}')

        #----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # Validate user input (number of players to be displayed) before calling function
        while True:
            num = input(f'\n3. Display Top Players (Keep User-Selected Categories)\nPlease enter the number of players to be displayed (1 to 188): ')
            try:  
                num = int(num)  
            except ValueError:
                print(f'{num} is NOT a valid number. Please input a valid number from 1 to 188')
                continue
            if 1 <= num <= 188:
                break
            else:
                print(f'{num} is outside the appropriate range. Number MUST be from 1 to 188')
        user.displayTopKeepCats(user.ranks, num, user.season, userCats, code)
    #----------------------------------------------------------------------------------------------------------------------
    # Choice 3: Display Season Averages (9 Cats)
    else:
        user.displaySeasonAvgs(user.ranks, user.season)

# Main, called if ran directly on 'main.py'
if __name__ == "__main__":
    main()