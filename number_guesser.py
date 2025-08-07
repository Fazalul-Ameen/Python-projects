import random
guesses = 0
top_of_range = input("Enter a number : ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please enter a number greater than 0 next time.")
        quit()
else:
    print("Please enter a number next time.")
    quit()

random_number = random.randrange(0,top_of_range) #range = top_of_range-1 = 10.

while True:
    guesses += 1
    user_guess = input("Make a guess : ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        printf("Enter a number next time.")
        continue
    
    if user_guess == random_number:
        print("You got it!!")
        break
    else:
        if user_guess > random_number : 
            print("You are above the number.")
        else:
            print("You are below the number.")
print("You got it in " + str(guesses) + " guesses.")