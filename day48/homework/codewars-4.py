def rowWeights(weights):
    team1_weight = 0
    team2_weight = 0
    
    for i in range(len(weights)):
        if i % 2 == 0:
            team1_weight += weights[i]
        else:
            team2_weight += weights[i]
    
    return (team1_weight, team2_weight)
