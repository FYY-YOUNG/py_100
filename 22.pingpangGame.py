# 两个乒乓球队进行比赛，各出三人。
# 甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。
# a说他不和x比，c说他不和x,z比，
# 请编程序找出三队赛手的名单。

team_2 = ['x','y','z']
# 核心 避免重复参赛
for a in team_2:
    for b in team_2:
        # 避免重复参赛
        if a != b:
            for c in team_2:
                if a != c and b != c:
                    if a != 'x' and c != 'x' and c != 'z':
                        print('a的对手是%s\nb的对手是%s\nc的对手是%s' % (a, b, c))
