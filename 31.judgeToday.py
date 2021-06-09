# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母

print('提示: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday')

letter = input("猜星期几，请输入对应英文:")

if (letter == 's' or letter == 'S'):
    print('不确定是 Saturday 还是 Sunday')
    letter = input("'请继续输入下一个字母:'")
    if ( letter == 'a' or letter == 'A'):
        print('Saturday')
    elif letter == 'u':
        print('Sunday')
    else:
        print('输入不对 无法匹配')

elif (letter == 'f' or letter == 'F'):
    print('Friday')

elif (letter == 'm' or letter == 'M'):
    print('Monday')

elif (letter == 't' or letter == 'T'):
    print('不确定是 Tuesday 还是 Thursday')
    letter = input("'请继续输入下一个字母:'")

    if (letter == 'u' or letter == 'U'):
        print('Tuesday')
    elif (letter == 'h' or letter == 'H'):
        print('Thursday')
    else:
        print('输入不对 无法匹配')

elif (letter == 'w' or letter == 'W'):
    print('Wednesday')
else:
    print('输入不对 无法匹配')
