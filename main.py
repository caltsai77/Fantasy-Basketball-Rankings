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
    season = input('Please enter the season in format YY-YY (Ex: 21-22): ')
    if season not in availableSeasons:
        print(f'Your inputted season of {season} is not available in the database: default season is 2021-22')
        season = '21-22'
    # season = '21-22'

    # Create and initialize season object
    user = Season(season)
    user.initialize(user.ranks, user.season)

    # Menu of Available Options for User
    print(f'\nAvailable Options (Season: 20{season}):\n\n1. Display Top Players Overall')
    print(f'2. Display Season Averages (9 Categories)\n3. Something Else')

    # User input validation for choice
    while True:
        choice = input('\nPlease enter your choice (from 1 to 3): ')
        try:  
            choice = int(choice)  
        except ValueError:
            print(f'{choice} is NOT a valid number. Please input a valid number from 1 to 3')
            continue
        if 1 <= choice <= 3:
            break
        else:
            print(f'{choice} is outside the appropriate range. Number MUST be from 1 to 3')

    # Choice 1: Display top x players 
    if choice == 1:
        # Validate user input
        while True:
            num = input('\n1. Display Top Players Overall\nPlease enter the number of players to be displayed (1 to 188): ')
            try:  
                num = int(num)  
            except ValueError:
                print(f'{num} is NOT a valid number. Please input a valid number from 1 to 188')
                continue
            if 1 <= num <= 188:
                break
            else:
                print(f'{num} is outside the appropriate range. Number MUST be from 1 to 188')
        user.displayTop(user.ranks, num, user.season)

    # Choice 2: Display Season Averages (9 Cats)
    elif choice == 2:
        user.displaySeasonAvgs(user.ranks, user.season)

if __name__ == "__main__":
    main()