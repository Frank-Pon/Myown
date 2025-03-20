n=int(input("請輸入一個數字當作範圍:"))
a,b,c=0,0,0
for i in range(1,n+1,1):
    if i%3==0:
        a+=1
    elif i%3==1:
        b+=1
    else:
        c+=1
print("3K有",a,"個,3K+1有",b,"個,3K+2有",c,"個")

# 輸出3的倍數,3的倍數+1,3的倍數+2的個數