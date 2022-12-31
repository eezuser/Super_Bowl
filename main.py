

#creating a scatter plot of all of the teams that have won superbowls in the past 50 years

playing_years = range(1966,2021)
nfl_teams = ["Cardinals", "Falcons", "Ravens", "Bills", "Panthers", "Bears", "Bengals", "Browns", "Cowboys", "Broncos", "Lions" ,"Packers",
             "Texans", "Colts", "Jaguars," "Chiefs", "Chargers", "Rams", "Dolphins", "Vikings", "Patriots", "Saints", "Giants", "Jets", "Raiders",
             "Eagles", "Steelers", "49ers", "Seahawks", "Buccaneers", "Titans", "Commanders"]

#function to iterate through playing_years, which will be used as the x-axis for the scatter plot
def super_bowl_years():
 for i in playing_years:
  i += 1
  print(i)

super_bowl_years()