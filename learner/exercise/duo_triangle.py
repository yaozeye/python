# Code by Yaoze Ye 
# https://yaozeye.github.io
# 05 March, 2020 
import turtle
# Large one
turtle.fd(300)
turtle.seth(120)
turtle.fd(300)
turtle.seth(240)
turtle.fd(300)
turtle.seth(0)
# Small one
turtle.penup()
turtle.goto(150,0)
turtle.pendown()
turtle.seth(60)
turtle.fd(150)
turtle.seth(180)
turtle.fd(150)
turtle.seth(300)
turtle.fd(150)
# Re-position
turtle.penup()
turtle.seth(120)
turtle.fd(150)
turtle.seth(0)
turtle.done()
