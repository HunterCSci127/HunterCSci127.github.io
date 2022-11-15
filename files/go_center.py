#Random search
import turtle
import random

def drawSquare():
    tess = turtle.Turtle()
    tess.penup()
    tess.goto(-25, -25)
    tess.color("red")
    tess.pendown()
    n = 4
    for i in range(n):
        tess.forward(50)
        tess.left(360/n)

def move(): #move tess
    tess = turtle.Turtle()
    tess.color('steelBlue')
    tess.shape('turtle')
    tess.penup()
    #Start off screen:
    tess.goto(-250,-250)
    #Remember:  abs(x) < 25 means absolute value: -25 < x < 25
    while abs(tess.xcor()) > 25 or abs(tess.ycor()) > 25:
      x = random.randrange(-200,200)
      y = random.randrange(-200,200)
      tess.goto(x,y)
      tess.stamp()
      print(tess.xcor(), tess.ycor())
    print('Found the center!')
    
    turtle.done()

def main():
    drawSquare()
    move()

if __name__ == '__main__':
   main()
