# Python Greatest Common Divisor
# Code by Yaoze Ye
# https://yaozeye.github.io
# 09 April 2020
# under the MIT License https://github.com/yaozeye/python/raw/master/LICENSE
num1 = int(input('The first number: '))
num2 = int(input('The second number: '))
num3 = min(num1, num2)
for i in range(1, num3 + 1):
    if num1 % i == 0 and num2 % i == 0:
        greatest_common_divisor = i
print('The maximum common divisor of %d and %d is %d.' % (num1, num2, greatest_common_divisor))
least_common_multiple = (num1 * num2) / greatest_common_divisor
print('The minimum common multiple of %d and %d is %d.' % (num1, num2, least_common_multiple))
