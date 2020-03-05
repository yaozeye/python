# Python Turtle Circle
# Code by Yaoze Ye 
# https://yaozeye.github.io
# 05 March, 2020 
import turtle
for i in range(9):
    turtle.circle((i+1)*20)
    turtle.penup()
    turtle.goto(0,-(i+1)*20)
    turtle.pendown()
turtle.penup()
turtle.goto(0,20)
turtle.done()
