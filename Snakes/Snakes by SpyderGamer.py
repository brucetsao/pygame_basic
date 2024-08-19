import turtle
import time
import random

delay = 0.1

mas = str("Less goo")

# Scores
score = 0
high_score = 0

# Screen Setup
wn = turtle.Screen()
wn.title("Snakes by SpyderGamer")
wn.bgcolor("black")
wn.setup(width=640, height=630)
wn.tracer(0)

# Snake Heado
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake Food
food= turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Le Scorez
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("white")
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write("Score: 0  |  High Score: 0", align = "center", font = ("ds-digital", 16, "normal"))

# Instructions
helpp = turtle.Turtle()
helpp.speed(0)
helpp.shape("square")
helpp.color("white")
helpp.penup()
helpp.hideturtle()
helpp.goto(0,240)
helpp.write("Press the Arrow Keys to Move", align = "center", font = ("ds-digital", 12, "normal"))

# Snake Master!
master = turtle.Turtle()
master.speed(0)
master.shape("square")
master.color("white")
master.penup()
master.hideturtle()
master.goto(0,285)
master.write("", align = "center", font = ("ds-digital", 14, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
        
def go_down():
    if head.direction != "up":
        head.direction = "down"
        
def go_left():
    if head.direction != "right":
        head.direction = "left"
        
def go_right():
    if head.direction != "left":
        head.direction = "right"
        
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
        helpp.clear()
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
        helpp.clear()
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
        helpp.clear()
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
        helpp.clear()

# Keyboard Stuff
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# MainLoop
while True:
    wn.update()

    # If collide with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Segments hide
        for segment in segments:
            segment.goto(1000,1000) #out of range
        # Clear the segments
        segments.clear()

        # Reset Score
        score = 0

        # Reset Delay
        delay = 0.1

        sc.clear()
        sc.write("Score: {}  |  High Score: {}".format(score, high_score), align="center", font=("ds-digital", 16, "normal"))

    # Eat food yum yum
    if head.distance(food) <20:
        # Food go faaaaar
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        # Snake grow and go brr
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten Delay
        delay -= 0.001
        # Increase core
        score += 10

        if score == 0:
            master.clear()
            master.write("{}".format(mas), align="center", font=("ds-digital", 16, "normal"))
        elif score == 10:
            master.clear()
            mas = str("Nice")
            master.write("{}".format(mas), align="center", font=("ds-digital", 16, "normal"))
        elif score == 30:
            master.clear()
            mas = str("Subscribe to SpyderGamer :)")
            master.write("{}".format(mas), align="center", font=("ds-digital", 16, "normal"))
        elif score == 50:
            master.clear()
            mas = str("Cool!")
            master.write("{}".format(mas), align="center", font=("ds-digital", 16, "normal"))
        elif score == 100:
            master.clear()
            mas = str("Baby Pro?")
            master.write("{}".format(mas), align="center", font=("ds-digital", 16, "normal"))
        elif score == 250:
            master.clear()
            mas = str("Pro...")
            master.write("{}".format(mas), align="center", font=("ds-digital", 16, "normal"))
        elif score == 400:
            master.clear()
            mas = str("You make Nokias proud!")
            master.write("{}".format(mas), align="center", font=("ds-digital", 16, "normal"))
        elif score == 500:
            master.clear()
            mas = str("Haxor?")
            master.write("{}".format(mas), align="center", font=("ds-digital", 16, "normal"))
        elif score == 700:
            master.clear()
            mas = str("Who is joe?")
        elif score == 1000:
            master.clear()
            mas = str("SNAKES MASTER!")
            master.write("{}".format(mas), align="center", font=("ds-digital", 16, "normal"))
        elif score == 5000:
            master.clear()
            mas = str("NO WAY!")
            master.write("{}".format(mas), align="center", font=("ds-digital", 16, "normal"))
        elif score == 10000:
            master.clear()
            mas = str("Ok, you beat me...")
            master.write("{}".format(mas), align="center", font=("ds-digital", 16, "normal"))
        elif score == 1000000:
            master.clear()
            mas = str("Still here? Ok, here's my iPad password: 2089")
            master.write("{}".format(mas), align="center", font=("ds-digital", 16, "normal")) 

        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("Score: {}  |  High Score: {}".format(score, high_score), align="center", font=("ds-digital", 16, "normal")) 

    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    # yES
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # If snake go yum yum again
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide Segments
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1

            # Update the score     
            sc.clear()
            sc.write("Score: {}  |  High Score: {}".format(score, high_score), align="center", font=("ds-digital", 16, "normal"))
    time.sleep(delay)
wn.mainloop()   
