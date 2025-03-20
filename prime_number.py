a=int(input("請輸入一個數字:"))
a_prime = True
#設定一個判斷用布林變數
factor = []
#設定一個list
for i in range(1,a+1):
    if a%i==0 :
        factor.append(i)
#用for迴圈將輸入數字的因數放進list
if len(factor)>2:
    a_prime = False
else:
    a_prime = True
#透過因數的數量來調節布林變數,如果list只有兩個數字(1與自己)就是質數,否則非質數
if a_prime:
    print(a,"是質數")
    print(a,"的因數有",factor)
else:
    print(a,"不是質數")
    print(a,"的因數有",factor)

#判斷質數並且輸出全部因數