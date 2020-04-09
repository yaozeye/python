# Python Weight Increment
# Code by Yaoze Ye 
# https://yaozeye.github.io
# 08 April 2020 
# under the MIT License https://github.com/yaozeye/python/raw/master/LICENSE 
weight = input()  # weight at present
weight = eval(weight)
print("I am now {:.2f} kg at present".format(weight))
for i in range(1, 11, 1):
    weight = weight + 0.5
    if i == 1:
        print("{} year later weight on earth: {:.2f} kg".format(i, weight))
        print("{} year later weight on moon: {:.2f} kg".format(i, 0.165*weight))        
    else:
        print("{} years later weight on earth: {:.2f} kg".format(i, weight))
        print("{} years later weight on moon: {:.2f} kg".format(i, 0.165*weight))
