HOME_TEAM_WON = 1

# O(n) time | O(k) space, where k is number of teams
def tournamentWinner(competitions, results):
    # Write your code here.
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScore(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam
        
    return currentBestTeam

def updateScore(winningTeam, points, scores):
    if winningTeam not in scores:
        scores[winningTeam] = 0
    scores[winningTeam] += points