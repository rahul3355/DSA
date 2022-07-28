def createStandings(competitions, results):
    # Write your code here.
    standings = {}

    for matchPtr in range(len(results)):
        teams = competitions[matchPtr]
        homeTeam = teams[0]
        awayTeam = teams[1]

        if homeTeam not in standings:
            standings[homeTeam] = 0
        if awayTeam not in standings:
            standings[awayTeam] = 0

    return standings



def updateStandings(competitions, results, standings):
    
    for matchPtr in range(len(results)):
        homeTeam = competitions[matchPtr][0]
        awayTeam = competitions[matchPtr][1]

        if results[matchPtr] == 1:
            valueHome = standings[homeTeam]
            valueHome += 3
            standings[homeTeam] = valueHome
        else:
            valueAway = standings[awayTeam]
            valueAway += 3
            standings[awayTeam] = valueAway

    print(standings)
    return standings

def getWinnerTeamName(standings, maxScore):
    keys = [k for k,v in standings.items() if v == maxScore]
    winner = str(keys[0])
    return winner




def tournamentWinner(competitions, results):
    standings = createStandings(competitions, results)
    standings = updateStandings(competitions, results, standings)
    scores = standings.values()
    maxScore = max(scores)
    winner = getWinnerTeamName(standings, maxScore)
    return winner