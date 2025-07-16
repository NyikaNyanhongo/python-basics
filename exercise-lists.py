#play with for loops

#create a list 
premier_league_teams =["Liverpool", "Arsenal","Manchester City", "Chelsea","Newcastle United"]
print("Top 5 English Premier_league_teams:", premier_league_teams)

#append 2 teams to the list 
premier_league_teams.append("Aston Villa")
premier_league_teams.append("Nottingham Forest")
print("Top 7 Premier league teams:", premier_league_teams)


#using indexes and slicing 
print("Favorite Football Team:",premier_league_teams[3])


#use a for loop to iterate throught the list 

print("Top 7 English Premier League Football Teams:")
for team in premier_league_teams:
    print("-", team)


print("Worst team ever:", premier_league_teams.pop(0))

