# Python Weight Increment
# Code by Yaoze Ye 
# https://yaozeye.github.io
# 08 April, 2020 
# under the MIT License https://github.com/yaozeye/python/raw/master/LICENSE 
weight = input()  # weight at present
weight = eval(weight)
n = 0.5/weight
for i in range(1, 11, 1):
    weight = weight*(1+n)
    print("{} years later weight on earth: {:.2f}kg".format(i, weight))
    print("{} years later weight on moon: {:.2f}kg".format(i, 0.165*weight))
