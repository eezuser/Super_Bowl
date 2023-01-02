from matplotlib import pyplot as plt



#using the range and list functions to store years since the superbowl started

playing_years = list(range(1967,2023))
nfl_teams = ["Packers", "Packers", "Jets", "Chiefs", "Colts", "Cowboys", "Dolphins", "Dolphins", "Steelers", "Steelers", "Raiders", "Cowboys",
             "Steelers", "Steelers", "Raiders", "49ers", "Commanders", "Raiders" , "49ers", "Bears", "Giants", "Commanders", "49ers", "49ers", "Giants", "Commanders", "Cowboys", "Cowboys", "49ers",
             "Cowboys", 'Packers', "Broncos", "Broncos", "Rams", "Ravens", "Patriots", "Buccaneers", "Patriots", "Patriots", "Steelers", "Colts", "Giants", "Steelers",
             "Saints", "Packers", "Giants", "Ravens", "Seahawks", "Patriots", "Broncos", "Patriots", "Eagles", "Patriots", "Chiefs", "Buccaneers", "Rams"]


# scatter plot corresponding the playing_years to the nfl_teams list indices
plt.scatter(playing_years, nfl_teams)
plt.show()



