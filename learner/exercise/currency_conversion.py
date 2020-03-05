# Python Currency Conversion
# Be advised, this sample is based on the currency ratio 1:6.7 (CNY:USD)
val = input("请输入带货币表示符号的金钱数目(例如: 128Y, 13D)：")
if val[-1] in ['y','Y']:
    d = float(val[0:-1])/6.7
    print("兑换后的金钱为：%.2fD"%d)
elif val[-1] in ['d','D']:
    y = 6.7 * float(val[0:-1])
    print("兑换后的金钱为：%.2fY"%y)
else:
    print("输入有误")
