import turtle
import time
import random
import game

delay = 0.1
snake_tail = []

# Score
score = 0
high_score = 0
# Functions
class Direction:
    def __init__(self):
        pass
    def go_up(self):
        if game.head.direction != "down":
            game.head.direction = "up"

    def go_dowindow(self):
        if game.head.direction != "up":
            game.head.direction = "down"

    def go_left(self):
        if game.head.direction != "right":
            game.head.direction = "left"

    def go_right(self):
        if game.head.direction != "left":
            game.head.direction = "right"

class Move:
    def __init__(self):
        pass
    def move(self):
        if game.head.direction == "up":
            y = game.head.ycor()
            game.head.sety(y + 20)

        if game.head.direction == "down":
            y = game.head.ycor()
            game.head.sety(y - 20)

        if game.head.direction == "left":
            x = game.head.xcor()
            game.head.setx(x - 20)

        if game.head.direction == "right":
            x = game.head.xcor()
            game.head.setx(x + 20)

# Keyboard bindings
game.window.listen()
dir = Direction()
game.window.onkeypress(dir.go_up, "Up")
game.window.onkeypress(dir.go_dowindow, "Down")
game.window.onkeypress(dir.go_left, "Left")
game.window.onkeypress(dir.go_right, "Right")

# Main game loop
while True:
    game.window.update()

    # Check for a collision with the border
    if game.head.xcor()>290 or game.head.xcor()<-290 or game.head.ycor()>290 or game.head.ycor()<-290:
        time.sleep(1)
        game.head.goto(0,0)
        game.head.direction = "stop"

        # Hide the snake_tail
        for segment in snake_tail:
            segment.goto(1000, 1000)
        
        # Clear the snake_tail list
        snake_tail.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        game.pen.clear()
        game.pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # Check for a collision with the food
    if game.head.distance(game.food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        game.food.goto(x,y)

        # Add a segment
        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.shape("circle")
        new_tail.color("black")
        new_tail.penup()
        snake_tail.append(new_tail)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        game.pen.clear()
        game.pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Move the end snake_tail first in reverse order
    for index in range(len(snake_tail)-1, 0, -1):
        x = snake_tail[index-1].xcor()
        y = snake_tail[index-1].ycor()
        snake_tail[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(snake_tail) > 0:
        x = game.head.xcor()
        y = game.head.ycor()
        snake_tail[0].goto(x,y)

    Movement =  Move()
    Movement.move()    

    # Check for head collision with the body snake_tail
    for segment in snake_tail:
        if segment.distance(game.head) < 20:
            time.sleep(1)
            game.head.goto(0,0)
            game.head.direction = "stop"
        
            # Hide the snake_tail
            for segment in snake_tail:
                segment.goto(1000, 1000)
        
            # Clear the snake_tail list
            snake_tail.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            game.pen.clear()
            game.pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

print("Game Over!")
game.window.mainloop()