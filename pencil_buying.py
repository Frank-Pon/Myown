
while True:
    n=int(input("請輸入班級人數:"))
    if 1<=n<=200:
        cash=str(((n//12)*50)+((n%12)*5))
        print("總共"+cash+"元")
        break
    else:
        print("請輸入正確人數!")

#買鉛筆,一支5元,一打50元,輸入班級人數算出要花多少錢買鉛筆