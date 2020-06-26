import turtle
import math
t = turtle.Turtle()
def roof():
  width = int(input("Roof Width: "))
  height = int(input("Roof Height: "))
  color = input("Roof Color: ")
  legsquare = ((width / 2) ** 2) + (height ** 2)
  leg = legsquare ** .5
  print(leg)
  sin = math.sin(height/leg)
  anglea = math.asin(sin)
  print(sin)
  angleb = (90 - anglea) * 2
  print(anglea)
  print(angleb)
  t.fillcolor(color)
  t.begin_fill()
  t.left(anglea)
  t.forward(leg)
  t.left(angleb+90)
  t.forward(leg)
  t.left(anglea+90)
  t.forward(width)
  t.end_fill()
roof()