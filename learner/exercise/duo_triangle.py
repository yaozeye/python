# Python Turtle Double Triangle
# Code by Yaoze Ye 
# https://yaozeye.github.io
# 05 March, 2020 
# under the MIT License https://github.com/yaozeye/python/raw/master/LICENSE 
import turtle
# Large one
turtle.fd(100)
turtle.seth(120)
turtle.fd(100)
turtle.seth(240)
turtle.fd(100)
turtle.seth(0)
# Small one
turtle.penup()
turtle.goto(50,0)
turtle.pendown()
turtle.seth(60)
turtle.fd(50)
turtle.seth(180)
turtle.fd(50)
turtle.seth(300)
turtle.fd(50)
# Re-position
turtle.penup()
turtle.seth(120)
turtle.fd(50)
turtle.seth(0)
turtle.done()
