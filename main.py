import turtle
import math
t = turtle.Turtle()
def roof():
  width = int(input("Roof Width: "))
  height = int(input("Roof Height: "))
  leg = width / 2
  hyp = math.sqrt(leg ** 2 + height ** 2)
  print(leg, height, hyp)
  a = height ** 2 + hyp ** 2 - leg ** 2
  b = 2 * height * hyp
  angle1 = math.degrees(math.acos(a/b))
  c = leg ** 2 + hyp ** 2 - height ** 2
  d = 2 * leg * hyp
  angle2 = 90-angle1
  angle2 *= 2
  t.forward(width)
  t.right(180)
  t.right(angle1)
  t.forward(hyp)
  t.right(180)
  t.right(angle2)
  t.forward(hyp)
  t.right(180)
  t.right(angle1)
  print(angle1, angle2)
roof()