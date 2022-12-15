# Fantasy Basketball Rankings
### Author: Caleb Tsai
### Created: 12/11/2022  
</br>

## Purpose:
- To display and rank Fantasy players for future drafts
- To store player data among 9 unique categories year to year
- To query specific searches (ex: best players i.t.o. points, steals, and assists)
</br>

## Introduction
Fantasy Basketball ([ESPN Fantasy Basketball Site](https://www.espn.com/fantasy/mens-basketball/)) is a ~~reality~~ game played by many users (yours truly) around the world (specifically the U.S.)
Leagues typically consist of 8-14 teams and rosters containing 10 starters, 3 bench players, and 2 Injured Reserve slots. 

### Positions:
- PG (Facilitator, Ex: LaMelo Ball)
- SG (Scorer, Ex: Devin Booker)
- SF (Flexibility / Handles, Ex: Jayson Tatum)
- PF (Height / Strength, Ex: Domantas Sabonis)
- C  (Rim Protector, Ex: Nikola Jokic)  
</br>

## How to Use Program
### Option 1:
1. Download files from GitHub onto local directory
2. Download VS Code
3. Run program via VS Code terminal by inputting: `python3 main.py`
4. Follow prompts that occur in local terminal
### Option 2:
1. Download files from GitHub onto local directory
2. Open local command prompt (Windows) or terminal (Mac)
3. Navigate to folder that contains program (titled: FantasyBasketballRankings)
4. Run program by inputting: `python3 main.py`
</br>

## League and Scoring Formats
League formats typically include weekly Head-to-Head (one opponent) or season-long Rotisserie (entire league) formats.
Head-to-Head formats are either points or category-based, with the latter being my preferred option :)
</br>

### Points Scoring:
- Point = 1
- 3PM = 1
- FGA = -1
- FGM = 2
- FTA = -1
- FTM = 1
- REB = 1
- AST = 2
- STL = 4
- BLK = 4
- TOV = -2
</br>

### 9-Cat Scoring:
- Points
- 3-Pointers Made
- Rebounds
- Assists
- Steals
- Blocks
- Field Goal Percentage
- Free Throw Percentage
- Turnovers

For weekly H2H Points, a team must accumulate more points than their opponent\
For weekly H2H 9-Cat, a team must win more categories than their opponent
</br>

## Strategy
Points Leagues: biased to players with more starts/volume, less affected by deficiencies in certain categories (Ex: player with bad defensive stats)
Category Leagues: greater player pool, for more "serious" players, requires constant roster turnover and streaming to win weekly match-ups.
</br>

## Knowledge Gained:
1. Extensive use of pandas and dataFrame properties
2. Formatting of decimals and positive (+) numbers
3. Display in a "pretty" format via importing tabulate
4. Input Validation including try/except
5. Python Object2.Oriented Programming and Classes
6. Python Data Structures including Lists and Dictionaries
</br>

## Applications:
1. For anyone interested in Fantasy Basketball trends and analysis across multiple seasons
2. For anyone interested in NBA statistics!
3. For anyone who wants to have a good time
4. For you! :)
</br>

## Future Features to Implement
- Input player name: output entire career with averages, value over time (overall and across 9 cats)
- Input category: output GOATS for each cat (highest average category value over player's career)
- Input team: output GOATS overall and for each cat
- Create my own ranking system from raw NBA statistics via [Basketball Reference](https://www.basketball-reference.com/)  
(I love Josh Lloyd don't get me wrong, I just wanna create my own rankings system!)
</br>

## Sources:
- [Basketball Monster Fantasy Basketball Player Rankings](https://basketballmonster.com/playerrankings.aspx)

