year = int(input("請輸入西元年份:"))

if year % 1000 ==0:
    print("閏年")
elif year % 400 == 0:
    print("閏年")
elif year % 100 == 0:
    print("平年")
elif year % 4 == 0 and year % 100 != 0:
    print("閏年")
elif year % 4 != 0:
    print("平年")