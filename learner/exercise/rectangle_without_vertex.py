# Python Turtle Rectangle Without Vertex
# Code by Yaoze Ye 
# https://yaozeye.github.io
# 05 March, 2020 
import turtle
for i in (90,180,270,0):
    turtle.penup()
    turtle.fd(80)
    turtle.pendown()
    turtle.fd(160)
    turtle.penup()
    turtle.fd(80)
    turtle.seth(i)
turtle.done
