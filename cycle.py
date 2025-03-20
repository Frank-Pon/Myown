
def cycle (a):
#a=input("請輸入:")
#b="".join(reversed(a))
#b=a[::-1]
    a=str(a)
    return a == a[::-1]


#可以做到翻轉字串,加上判斷可以寫成判斷是否回文  ABBA之類


if __name__ == '__main__':
    print(cycle (1223))