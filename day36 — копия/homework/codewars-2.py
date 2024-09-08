def rock_paper_scissors(player1, player2):
    # Define the rules: rock beats scissors, scissors beats paper, paper beats rock
    rules = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    
    # Check if it's a draw
    if player1 == player2:
        return "Draw!"
    
    
    if rules[player1] == player2:
        return "Player 1 wins!"
    
    # Otherwise, player2 wins
    return "Player 2 wins!"

# Examples
print(rock_paper_scissors('rock', 'scissors'))  
print(rock_paper_scissors('paper', 'rock'))     
print(rock_paper_scissors('scissors', 'scissors'))  
print(rock_paper_scissors('rock', 'paper'))     
