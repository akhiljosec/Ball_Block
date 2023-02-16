#Ball Block game deveoped by Akhil Jose C

import turtle

ballblock = turtle.Screen()
ballblock.title("Ball Block")
ballblock.bgcolor("white")
ballblock.setup(width=1000, height=700)
ballblock.tracer(0)


# header
writer = turtle.Turtle()
writer.speed(0)
writer.color("#858181")
writer.penup()
writer.hideturtle()
writer.goto(0, 310)
writer.write("Ball Block made by Akhil Jose C" ,align="center",font=("Terminal", 16,"bold"))


# Keys
writer = turtle.Turtle()
writer.speed(0)
writer.color("#858181")
writer.penup()
writer.hideturtle()

# Keys Gamer 1
writer.goto(-450, 100)
writer.write("W" ,align="center",font=("Terminal", 20,"bold"))
writer.goto(-450, 60)
writer.write("S" ,align="center",font=("Terminal", 20,"bold"))
writer.goto(-450, 20)
writer.write("D" ,align="center",font=("Terminal", 20,"bold"))
writer.goto(-450, -20)
writer.write("A" ,align="center",font=("Terminal", 20,"bold"))

#Key Gamer2
writer.goto(450, 100)
writer.write("↑" ,align="center",font=("Terminal", 20,"bold"))
writer.goto(450, 60)
writer.write("↓" ,align="center",font=("Terminal", 20,"bold"))
writer.goto(450, 20)
writer.write("→" ,align="center",font=("Terminal", 20,"bold"))
writer.goto(450, -20)
writer.write("←" ,align="center",font=("Terminal", 20,"bold"))


#Score
pas, pbs = 0, 0

#Wall1
wall1 = turtle.Turtle()
wall1.color("#d1544f")
wall1.shapesize(stretch_wid=2, stretch_len=.5)
wall1.shape("square")
wall1.penup()
wall1.goto(0, -290)

#Wall2
wall2 = turtle.Turtle()
wall2.color("#d1544f")
wall2.shapesize(stretch_wid=2, stretch_len=.5)
wall2.shape("square")
wall2.penup()
wall2.goto(0, 290)

#Blocker A
blocker_a = turtle.Turtle()
blocker_a.speed(0)
blocker_a.color("#d1544f")
blocker_a.shapesize(stretch_wid=0.5, stretch_len=5)
blocker_a.shape("square")
blocker_a.penup()                #Do not trace path
blocker_a.goto(-200, -285)

#Blocker B
blocker_b = turtle.Turtle()
blocker_b.speed(0)
blocker_b.color("#d1544f")
blocker_b.shapesize(stretch_wid=0.5, stretch_len=5)
blocker_b.shape("square")
blocker_b.penup()
blocker_b.goto(200, -285)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("#858181")
ball.shape("circle")
ball.penup()
ball.goto(100, 100)
ball.dx = 2
ball.dy = 2

#BorderY
for i in range(0,595):
	writer = turtle.Turtle()
	writer.speed(0)
	writer.color("#858181")
	writer.penup()
	writer.hideturtle()
	writer.goto(-400, -315+i)
	writer.write("| \n")

	writer = turtle.Turtle()
	writer.speed(0)
	writer.color("#858181")
	writer.penup()
	writer.hideturtle()
	writer.goto(400, -315+i)
	writer.write("| \n")

#BorderX
for i in range(0,795):
	writer = turtle.Turtle()
	writer.speed(0)
	writer.color("#858181")
	writer.penup()
	writer.hideturtle()
	writer.goto(-400+i, 300)
	writer.write("_")
	writer.goto(-400+i, 295)
	writer.write("_")

	writer = turtle.Turtle()
	writer.speed(0)
	writer.color("#858181")
	writer.penup()
	writer.hideturtle()
	writer.goto(-400+i, -300)
	writer.write("_")
	writer.goto(-400+i, -295)
	writer.write("_")


#Score
writer = turtle.Turtle()
writer.speed(0)
writer.color("#858181")
writer.penup()
writer.hideturtle()
writer.goto(0, -335)
writer.write(f"Gamer 1 : {pas}		 			Gamer 2 : {pbs}", align="center", font=("Terminal", 16, "bold"))

#Function
def blocker_a_up():
    y = blocker_a.ycor()
    y += 25
    blocker_a.sety(y)

def blocker_a_down():
    y = blocker_a.ycor()
    y -= 25
    blocker_a.sety(y)

def blocker_a_right():
    x = blocker_a.xcor()
    x += 25
    blocker_a.setx(x)

def blocker_a_left():
    x = blocker_a.xcor()
    x -= 25
    blocker_a.setx(x)

def blocker_b_up():
    y = blocker_b.ycor()
    y += 25
    blocker_b.sety(y)

def blocker_b_down():
    y = blocker_b.ycor()
    y -= 25
    blocker_b.sety(y)

def blocker_b_right():
    x = blocker_b.xcor()
    x += 25
    blocker_b.setx(x)

def blocker_b_left():
    x = blocker_b.xcor()
    x -= 25
    blocker_b.setx(x)

#Keyboard binding
ballblock.listen()
ballblock.onkeypress(blocker_a_up, "w")
ballblock.onkeypress(blocker_a_down, "s")
ballblock.onkeypress(blocker_a_right, "d")
ballblock.onkeypress(blocker_a_left, "a")

ballblock.onkeypress(blocker_b_up, "Up")
ballblock.onkeypress(blocker_b_down, "Down")
ballblock.onkeypress(blocker_b_right, "Right")
ballblock.onkeypress(blocker_b_left, "Left")

while True:
    ballblock.update()


    #Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)




    #Border Checking (ball)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        

    if ball.ycor() < -290 and ball.xcor() > 0:
        ball.goto(0, 0)
        ball.dy *= -1
        pas +=1
        writer.clear()
        writer.write(f"Gamer 1 : {pas}		 			Gamer 2 : {pbs}", align="center", font=("Terminal", 16, "bold"))

    if ball.ycor() < -290 and ball.xcor() < 0:
        ball.goto(0, 0)
        ball.dy *= -1
        pbs +=1
        writer.clear()
        writer.write(f"Gamer 1 : {pas}		 			Gamer 2 : {pbs}", align="center", font=("Terminal", 16, "bold"))

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    # Border Checking (blockers)
    if blocker_a.ycor() > 285:
        blocker_a.sety(285)

    if blocker_a.ycor() < -285:
        blocker_a.sety(-285)

    if blocker_a.xcor() < -350:
        blocker_a.setx(-350)

    if blocker_a.xcor() > -60:
        blocker_a.setx(-60)

    if blocker_b.ycor() > 285:
        blocker_b.sety(285)

    if blocker_b.ycor() < -285:
        blocker_b.sety(-285)

    if blocker_b.xcor() < 60:
        blocker_b.setx(60)

    if blocker_b.xcor() > 350:
        blocker_b.setx(350)

#Blocker and Ball Collisions

    if (ball.ycor() < blocker_b.ycor() + 10 and ball.ycor() > blocker_b.ycor() - 10) and ball.xcor() < blocker_b.xcor() + 50 and ball.xcor() > blocker_b.xcor() - 50:
        ball.dy *= -1

    if (ball.ycor() < blocker_a.ycor() + 10 and ball.ycor() > blocker_a.ycor() - 10) and ball.xcor() < blocker_a.xcor() + 50 and ball.xcor() > blocker_a.xcor() - 50:
        ball.dy *= -1
