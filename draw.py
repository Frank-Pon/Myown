Y=int(input("請輸入年份:"))
M=int(input("請輸入月份:"))
D=int(input("請輸入日期:"))

A=(Y*4+M*2+D)%3

if A==0:
    print("普")
elif A==1:
    print("吉")
else:
    print("大吉")

#輸入日期並占卜