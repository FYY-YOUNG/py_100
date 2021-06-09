# 输出指定格式的日期
# 计算当前日期前后3天的日期


from datetime import date, datetime, timedelta

if __name__ == '__main__':
    # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
    print("当前日期："+date.today().strftime('%d/%m/%Y'))

    day = date.today()
    print(("当前日期：{}").format(day))

    # 当前日期的前3天，后3天的日期是？
    now = datetime.now()
    delta = timedelta(days=3)
    n_days_after = now + delta
    n_days_forward = now - delta

print("向后推迟3天的日期：{}".format((now + delta).strftime('%Y-%m-%d')))
print("向后推迟3天的日期：{}".format((now + delta).strftime('%d/%m/%Y')))

print("向前推3天的日期：{}".format(n_days_forward.strftime('%Y-%m-%d')))
print("向前推3天的日期：{}".format(n_days_forward.strftime('%d/%m/%Y')))