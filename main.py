import turtle
import math
t = turtle.Turtle()
def roof():
  width = int(input("Roof Width: "))
  height = int(input("Roof Height: "))
  color = input("Roof Color: ")
  legsquare = ((width / 2) ** 2) + (height ** 2)
  leg = legsquare ** .5
  sin = math.sin(height/leg)
  asin = math.asin(sin)
  anglea = math.degrees(asin)
  angleb = (90 - anglea) * 2
  t.fillcolor(color)
  t.begin_fill()
  t.forward(width)
  t.left(180-anglea)
  t.forward(leg)
  t.right(180+angleb)
  t.forward(leg)
  t.left(180-anglea)
  t.end_fill()
roof()