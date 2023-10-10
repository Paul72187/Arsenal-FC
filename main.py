import pandas as pd 

df = pd.read_csv('ArsenalPremierLeagueResults.csv')

df.to_html('results.html',index=False)

df = pd.read_csv('ArsenalPremierLeagueScorers.csv')

df.to_html('matchscorers.html',index=False)

df = pd.read_csv('ArsenalPremierLeagueTopScorers.csv')

df.to_html('topscorers.html',index=False)

df = pd.read_csv('ArsenalPremierLeagueCountryScorers.csv')

df.to_html('countryscorers.html',index=False)

df = pd.read_csv('ArsenalPremierLeagueScorelines.csv')

df.to_html('scorelines.html',index=False)

df = pd.read_csv('ArsenalPremierLeagueStats.csv')

df.to_html('premierleaguestats.html',index=False)

df = pd.read_csv('ArsenalPremierLeagueManagers.csv')

df.to_html('managers.html',index=False)

df = pd.read_csv('ArsenalPremierLeagueOpponents.csv')

df.to_html('opponents.html',index=False)

df = pd.read_csv('ArsenalPremierLeaguePointsDistribution.csv')

df.to_html('pointsdistribution.html',index=False)

df = pd.read_csv('ArsenalPremierLeagueOwnGoals.csv')

df.to_html('owngoals.html',index=False)