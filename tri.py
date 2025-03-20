# def tri(max):
#     r=[1]
#     n=0
#     while max>n:
#         n+=1
#         yield r
#         r=[1]+[r[i]+r[i+1] for i in range(len(r)-1)]+[1]

# b=int(input("請輸入數字:"))
# for a in tri(b):
#     print(a)
import sys

print(sys.executable)