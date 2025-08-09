import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "green", "blue", "cyan", "orange", "brown", "yellow", "pink", "black", "purple"]

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10) : ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Number of racers must be a number... Try Again!!")
            continue
        
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number is not in the range specified (2 - 10). Try Again!!")

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH / (len(colors)+1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH/2 + (i+1) * spacingx, -HEIGHT/2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            x, y = racer.pos()
            if y >= HEIGHT/2 - 10:
                return colors[turtles.index(racer)]

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
print(colors)
winner = race(colors)
print("Winner is ",winner)
time.sleep(5)
