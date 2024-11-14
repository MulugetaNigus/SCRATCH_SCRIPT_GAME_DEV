import turtle
import time
import random

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

score_user = 0
score_computer = 0

paddle_user = turtle.Turtle()
paddle_user.speed(0)
paddle_user.shape("square")
paddle_user.color("white")
paddle_user.shapesize(stretch_wid=5, stretch_len=1)
paddle_user.penup()
paddle_user.goto(-350, 0)


ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = 5

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("User: 0  Computer: 0", align="center", font=("Courier", 24, "normal"))


def paddle_user_up():
    y = paddle_user.ycor()
    y += 20
    if y > 250:
        y = 250
    paddle_user.sety(y)

def paddle_user_down():
    y = paddle_user.ycor()
    y -= 20
    if y < -250:
        y = -250
    paddle_user.sety(y)

wn.listen()
wn.onkeypress(paddle_user_up, "w")
wn.onkeypress(paddle_user_down, "s")


while True:
    try:
        wn.update()
        time.sleep(0.01)

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_computer += 1
            pen.clear()
            pen.write("User: {}  Computer: {}".format(score_user, score_computer), align="center", font=("Courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_user += 1
            pen.clear()
            pen.write("User: {}  Computer: {}".format(score_user, score_computer), align="center", font=("Courier", 24, "normal"))

        if ball.xcor() > 340 and ball.dx > 0:
            ball.setx(340)
            ball.dx *= -1
            ball.dy = random.uniform(-1, 1)

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_user.ycor() + 40 and ball.ycor() > paddle_user.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1

    except Exception as e:
        print(f"An error occurred: {e}")
        break