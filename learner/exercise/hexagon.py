# Python Turtle Hexagon
# Code by Yaoze Ye 
# https://yaozeye.github.io
# 05 March, 2020 
import turtle
# First Triangle
turtle.seth(30)
turtle.fd(300)
turtle.seth(150)
turtle.fd(300)
turtle.seth(270)
turtle.fd(300)
# Re-position
turtle.penup()
turtle.seth(30)
turtle.fd(100)
turtle.seth(-30)
turtle.pendown()
# Second Triangle
turtle.fd(100)
turtle.seth(90)
turtle.fd(300)
turtle.seth(210)
turtle.fd(300)
turtle.seth(330)
turtle.fd(200)
# Re-position
turtle.penup()
turtle.goto(0,300)
turtle.done
