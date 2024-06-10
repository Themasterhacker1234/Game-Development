import turtle
import time
import random

delay= .1

food=turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-200,200),random.randint(-200,200))

sc=turtle.Screen()
sc.bgcolor("light blue")

snake=turtle.Turtle()
snake.shape("square")
snake.color("black")
snake.penup()
snake.direction="none"

def move():
  
  if snake.direction=="right":
    x=snake.xcor()
    snake.setx(x+20)
    snake.setheading(180)

  if snake.direction=="left":
    x=snake.xcor()
    snake.setx(x-20)
    snake.setheading(-180)

  if snake.direction=="down":
    y=snake.ycor()
    snake.sety(y-20)
    snake.setheading(-90)

  if snake.direction=="up":
    y=snake.ycor()
    snake.sety(y+20)
    snake.setheading(90)
    
def right():
  snake.direction="right"
  
def left():
  snake.direction="left"
  
def up():
  snake.direction="up"
  
def down():
  snake.direction="down"

sc.listen()
sc.onkey(right,"d")
sc.onkey(left,"a")
sc.onkey(up,"w")
sc.onkey(down,"s")

pen=turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.goto(0,150)

segments=[]
score=0
high_score=0
lose="You Lose"

while True:
  sc.update()
  move()
  time.sleep(delay)
  if snake.distance(food)<20:
    food.goto(random.randint(-200,200),random.randint(-200,200))  
    new=turtle.Turtle()
    new.shape("square")
    new.color("grey")
    new.penup()
    segments.append(new)
    score=score+1

    if score>high_score:
      high_score = score
      
    pen.clear()  
    pen.write("Score:{} High Score:{}".format(score,high_score),align="center",font=("Arial",30,"normal"))
  
  for i in range(len(segments)-1,0,-1):
     x=segments[i-1].xcor()
     y=segments[i-1].ycor()
     segments[i].goto(x,y)

  if len(segments)>0:
      x=snake.xcor()
      y=snake.ycor()
      segments[0].goto(x,y)
      if  len(segments)>1 and snake.distance(segments[-1])<20:
        pen.goto(0,0)
        pen.write("Game Over".format(lose),align="center",font=("Arial",45,"normal",))
        break
  
  if snake.xcor() > 240 or snake.xcor() < -250 or snake.ycor() < -201 or snake.ycor() > 220 :
    pen.goto(0,0)
    pen.write("Game Over".format(lose),align="center",font=("Arial",45,"normal",))
    break
    
sc.mainloop()