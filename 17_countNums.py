# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
# 判断字母：isalpha()；
# 判断空格isspace()；
# 判断数字 isdigit()；
# 一个 for 循环就可以搞定

import string
s = input('请输入一个字符串:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print ('英文字母 = %d,空格 = %d,数字 = %d,其它字符 = %d' % (letters,space,digit,others))