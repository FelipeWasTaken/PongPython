import turtle as t

win = t.Screen()                    #Define "win" as the Screen
win.title('Pong :D')                #Add a title to the window
win.bgcolor("Black")                #Define the background color
win.setup(width=800, height=600)    #Define the Screen size
win.tracer(0)                       #Smoothest game

#Score:
score_a = 0
score_b = 0

#Objects:
#Paddle A                           
paddle_a = t.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("Red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = t.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("Blue")              
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = t.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("White")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

#Pen
pen = t.Turtle()
pen.speed(0)
pen.color("Gray")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 20, "normal"))


#Functions:    
#Paddle A              
def paddle_a_up():          #Set Paddle A Up
    y = paddle_a.ycor()     
    y += 20                 
    paddle_a.sety(y)        

def paddle_a_down():        #Set Paddle A Down
    y = paddle_a.ycor()     
    y -= 20                 
    paddle_a.sety(y)        

#Paddle B                   
def paddle_b_up():          #Set Paddle B Up       
    y = paddle_b.ycor()     
    y += 20
    paddle_b.sety(y)        

def paddle_b_down():        #Set Paddle B Down
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


#Keyboard binding:
win.listen()
win.onkeypress(paddle_a_up, "w")    #Paddle A
win.onkeypress(paddle_a_down, "s")  #Paddle A

win.onkeypress(paddle_b_up, "Up")    #Paddle B
win.onkeypress(paddle_b_down, "Down")  #Paddle B

#main game loop:                    #Makes the game work
while True:
    win.update()

    #Move the ball:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking:
    if ball.ycor() > 290:       #Top border
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:      #Bottom border
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:       #Right border  
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

    if ball.xcor() < -390:      #Left border
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))
    
    #Paddle Colide:
    #Paddle B
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1

    #Paddle A
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1