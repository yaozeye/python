# Python Turtle Hexagon
# Code by Yaoze Ye 
# https://yaozeye.github.io
# 05 March, 2020 
# under the MIT License https://github.com/yaozeye/python/raw/master/LICENSE 
import turtle
# First Triangle
turtle.seth(30)
turtle.fd(120)
turtle.seth(150)
turtle.fd(120)
turtle.seth(270)
turtle.fd(120)
# Re-position
turtle.penup()
turtle.seth(30)
turtle.fd(40)
turtle.seth(-30)
turtle.pendown()
# Second Triangle
turtle.fd(40)
turtle.seth(90)
turtle.fd(120)
turtle.seth(210)
turtle.fd(120)
turtle.seth(330)
turtle.fd(80)
# Re-position
turtle.penup()
turtle.goto(0,120)
turtle.done
