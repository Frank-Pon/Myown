
x = int(input('x = '))
y = int(input('y = '))
# 如果x大於y就交換x和y的值
if x > y:
    # 透過下面的操作將y的值賦給x, 將x的值賦給y
    x, y = y, x
# 從兩個數中較小的數開始做遞減的迴圈
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公約數是%d' % (x, y, factor))
        print('%d和%d的最小公倍數是%d' % (x, y, x * y // factor))
        break
