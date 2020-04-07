# Python Calculate Characters
# Code by Yaoze Ye 
# https://yaozeye.github.io
# 07 April, 2020 
# under the MIT License https://github.com/yaozeye/python/raw/master/LICENSE 
text = input()
kanji = latin = number = space = others = 0
# kanji 中文字符
# latin 英文字符
# number 数字字符
# space 空格字符
# others 其他字符
for i in text:
    if 40869 >= ord(i) >= 19968:                  # unicode
        kanji += 1
    elif 122 >= ord(str.lower(i)) >= 97:          # lowercase
        latin += 1
    elif 57 >= ord(i) >= 48:
        number += 1
    elif i == ' ':
        space += 1
    else:
        others += 1
print('中文字符个数为{}'.format(kanji), '\n'+'英文字符个数为{}'.format(latin), '\n'+'数字字符个数为{}'.format(number), '\n'+'空格字符个数为{}'.format(space), '\n'+'其他字符个数为{}'.format(others))
