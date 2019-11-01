import turtle

def setUp():
  t = turtle.Turtle()
  t.color('purple')
  t.penup()
  return(t)

def getInput():
  x = int(input('Enter x value:'))
  y = int(input('Enter y value:'))
  return(x,y)

def markLocation(t,x,y):
  t.goto(x,y)
  t.stamp()

def main():
  tess = setUp()    #Returns a purple turtle with pen up.
  for i in range(5):
       x,y = getInput()        #Asks user for two numbers.
       markLocation(tess,x,y)  #Move tess to (x,y) and stamp.

if __name__ == "__main__":
     main()
