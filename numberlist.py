a=input("請輸入一串數字:")
b=list(map(int,a.split(' ')))
#print(b)
if b[1]-b[0]==b[2]-b[1]:  #等差級數
    b.append(b[len(b)-1]+(b[1]-b[0]))
    #將運算結果推進b list
    print(b)
elif b[1]/b[0] == b[2]/b[1]:  #等比級數
    b.append(int(b[len(b)-1]*(b[1]/b[0])))
    #將運算結果推進b list
    print(b)
else:
    print("非等比也非等差")