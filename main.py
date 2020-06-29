import turtle
import math
t = turtle.Turtle()
def roof():
  width = int(input("Roof Width: "))
  height = int(input("Roof Height: "))
  color = input("Roof Color: ")
  leg = width / 2
  hyp = ((leg ** 2) + (height ** 2)) ** .5
  a = math.degrees(math.atan(height/leg))
  b = 2*(math.degrees(math.atan(leg/height)))
  c = a
  if a + b/2 != 90:
    print("The degrees don't add up!")
    print(a, b)
    quit()
  t.fillcolor(color)
  t.begin_fill()
  t.forward(width)
  t.left(180)
  t.right(a)
  t.forward(leg)
  t.left(180)
  t.right(b)
  t.forward(leg)
  t.left(180)
  t.right(c)
  t.end_fill()
roof()