import turtle
import os



win = turtle.Screen()
win.title("Game")
win.bgcolor("black")
win.setup(width =800,height=600 )
win.tracer(0)

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5,stretch_len = 1)
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350,0)






#paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5,stretch_len = 1)
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350,0)



#Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape('circle')
Ball.color('white')
Ball.penup()
Ball.goto(0, 0)
Ball.dx = .3
Ball.dy = -.3

#pen

pen= turtle.Turtle()
pen.speed(0)
pen.color('White')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0  Player B: 0", align="center", font=("Courier", 20,"normal"))

#Score

score_a = 0
score_b = 0


#Function


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)




#keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")    
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")




#Main Game Loop
while True:
    win.update()

    #move the ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    #border checking
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1
        os.system("aplay bounce.wav&")
        

    
    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1
        os.system("aplay bounce.wav&")

    if Ball.xcor() > 390:
        Ball.goto(0,0)
        Ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A:{}  Player B: {}".format(score_a,score_b), align="center",
                  font=("Courier", 20, "normal"))
        os.system("aplay bounce.wav&")


        


    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A:{}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 20, "normal"))
        os.system("aplay bounce.wav&")

    #paddle and ball collisions

    if (Ball.xcor() > 340 and Ball.xcor() < 350) and (Ball.ycor() < paddle_b.ycor() + 40 and Ball.ycor() > paddle_b.ycor() -40):
        Ball.setx(340)
        Ball.dx *= -1
        os.system("aplay bounce.wav&")


    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (Ball.ycor() < paddle_a.ycor() + 40 and Ball.ycor() > paddle_a.ycor() - 40):
        Ball.setx(-340)
        Ball.dx *= -1
        os.system("aplay bounce.wav&")

        



