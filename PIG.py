import random;

def roll():
    min_value = 1
    max_value = 6
    value = random.randint(min_value, max_value)
    return value

players = input("Enter the number of players (2 - 4 players) : ")
if players.isdigit():
    players = int(players)
    if 2 <= players <= 4:
        print("You have selected ", players ,"players")
    else:
        print("Invalid! Please enter the number of players from 2 to 4 next time..")
        quit()

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("Player", player_idx+1, "'s turn has just started.")
        print("Current score : ", player_scores[player_idx],"\n")
        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll ? (Y) : ").lower()
            if should_roll != "y":
                break
            
            value = roll()
            if value == 1:
                print("You rolled 1; Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:",value)
            
            print("Your current score is:", current_score)
            if current_score >=50:
                break
    
    player_scores[player_idx] = current_score
    print("Your total score is :",player_scores[player_idx])
    print("----------------------------------------------------------------------------------------------")

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player-",winning_idx+1,"Won the game!!")