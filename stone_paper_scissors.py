import random

user_win = 0
computer_win = 0

print("Welcome to stone paper scissors!!")
play = input("Shall we start the game? (yes/no) : ").lower()
if play != "yes":
    quit()

options = ["stone", "paper", "scissors"]

while True:
    user_input = input("Stone/Paper/Scissors or Q to quit : ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    computer_input = options[random_number]
    print("Computer picked", computer_input)

    if computer_input == "stone" and user_input == "paper":
        print("You won!")
        user_win += 1

    elif computer_input == "paper" and user_input == "scissors":
        print("You won!")
        user_win += 1

    elif computer_input == "scissors" and user_input == "stone":
        print("You won!")
        user_win += 1

    elif user_input == computer_input:
        print("Draw!!")

    else:
        print("Computer won!")
        computer_win += 1

print("Your score : " + str(user_win))
print("Computer's score : " + str(computer_win))
if computer_win < user_win:
    print("You win the game.")
else:
    print("Computer win the game.")
print("Good Bye!!")
