# Code by Yaoze Ye 
# https://yaozeye.github.io
# 05 March, 2020 
# under the MIT License https://github.com/yaozeye/python/raw/master/LICENSE 
import turtle
for i in (90,180,270,0):
    turtle.penup()
    turtle.fd(30)
    turtle.pendown()
    turtle.fd(60)
    turtle.penup()
    turtle.fd(30)
    turtle.seth(i)
turtle.done
