#Ball Block game deveoped by Akhil Jose C

import turtle

ballblock = turtle.Screen()
ballblock.setup(width=1000, height=700)
ballblock.tracer(0)
ballblock.title("Ball Block")
ballblock.bgcolor("white")

#Ball
balli = turtle.Turtle()
balli.shape("circle")
balli.color("#858181")
balli.penup()
balli.goto(100, 100)
balli.speed(0)
balli.dx = 1
balli.dy = 1


# header
writer1 = turtle.Turtle()
writer1.speed(0)
writer1.color("#858181")
writer1.penup()
writer1.hideturtle()
writer1.goto(0, 310)
writer1.write("Ball Block made by Akhil Jose C" ,align="center",font=("Courier", 16,"bold"))


#Option
writer = turtle.Turtle()
writer.speed(0)
writer.color("#858181")
writer.penup()
writer.hideturtle()
writer.goto(0, 20)
writer.write(f"Start Game (Press Space)", align="center", font=("Terminal", 16,"bold"))
writer.goto(0, -20)
# Below function didn't worked needed to be corrected
writer.write(f"Quit Game (Press Q)", align="center", font=("Terminal", 16,"bold"))



#Function

def option_a():
    writer1.clear()
    writer.clear()
    balli.setx(0)
    balli.sety(0)
    import Ball_Block.py

def option_b():
    quit()

#Keyboard binding
ballblock.listen()

ballblock.onkeypress(option_a, "space")
ballblock.onkeypress(option_b, "q")

#Highlighter

while True:
    ballblock.update()


    #Move the Ball
    balli.setx(balli.xcor() + balli.dx)
    balli.sety(balli.ycor() + balli.dy)




    #Border Checking (ball)

    if balli.ycor() > 290:
        balli.sety(290)
        balli.dy *= -1

    if balli.ycor() < -290:
        balli.sety(-290)
        balli.dy *= -1

    if balli.xcor() > 390:
        balli.setx(390)
        balli.dx *= -1

    if balli.xcor() < -390:
        balli.setx(-390)
        balli.dx *= -1
