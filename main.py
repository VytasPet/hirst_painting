import colorgram
import random
from turtle import Turtle, Screen

t = Turtle()
colors_list = [(209, 165, 125), (140, 48, 106), (164, 169, 38), (244, 80, 56), (3, 143, 55), (233, 109, 162), (215, 234, 232), (241, 65, 140)]

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)

def panting():
    t.penup()
    t.setposition(-100, -100)
    t.pendown()
    pos = 0
    while pos < 210:
        long = 0
        t.setposition(-100, -100 + pos)
        while long < 210:
            t.pendown()
            t.dot(20, rgb_to_hex(random.choice(colors_list)))
            t.penup()
            t.forward(40)
            long += 40
        pos += 40

panting()


colors = colorgram.extract('hir.jpg', 10)

cols =[]

for c in colors:
    r = c.rgb.r
    g = c.rgb.g
    b = c.rgb.b
    new_col = (r, g, b)
    cols.append(new_col)

screen = Screen()
screen.exitonclick()
