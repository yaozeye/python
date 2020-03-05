# Python Turtle Circle
# Code by Yaoze Ye 
# https://yaozeye.github.io
# 05 March, 2020 
# under the MIT License https://github.com/yaozeye/python/raw/master/LICENSE 
import turtle
for i in range(9):
    turtle.circle((i+1)*15)
    turtle.penup()
    turtle.goto(0,-(i+1)*15)
    turtle.pendown()
turtle.penup()
turtle.goto(0,15)
turtle.done()
