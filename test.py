# class bank():
#     def __init__(self,name,num):
#         self.name = name
#         self.num = num
#         self.balance = 0
#     def debit(self,amount):
#         if amount <=0:
#             raise ValueError("Amount must be positive!")
#         else:
#             self.balance+=amount
#     def credit(self,amount):
#         if amount <=0:
#             raise ValueError("Amount must be positive!")
#         elif (self.balance-amount)<0:
#             raise RuntimeError("Balance is not enough!")
#         else:
#             self.balance-=amount

# a=bank("Pon",7)
# a.debit(35000)
# a.credit(10000)
# print(a.name,"'s balance :",a.balance)



# s1=72
# s2=85
# r= (85-72)/72*100
# print('小明本次成績相比上次提升了%.2f%%'%r)
# print('小明本次成績相比上次提升了{0:.2f}%'.format(r))
# print(f'小明本次成績相比上次提升了{r:.2f}%')

# L=[
# ['Apple','Google','Microsoft'],
# ['Python','PHP','Ruby','Java'],
# ['Adam','Bart','Bob']
# ]


# print(L[0][0]) #Apple
# print(L[1][2]) #Ruby
# print(L[2][1]) #Bart

# h=int(input('請輸入您的身高:'))/100
# w=int(input('請輸入您的體重:'))
# bmi=w/(h**2)
# if bmi>=32:
#     print(f'您的BMI:{bmi:.1f},身體狀態處於嚴重肥胖,請盡速就醫尋求協助')
# elif 28<=bmi<32:
#     print(f'您的BMI:{bmi:.1f},身體狀況為肥胖,請多注意身體健康')
# elif 25<=bmi<28:
#     print(f'您的BMI:{bmi:.1f},身體狀況為過重,請稍加注意身體健康')
# elif  18.5<= bmi<25:
#     print(f'您的BMI:{bmi:.1f},身體狀況為正常,請繼續保持')
# else:
#     print(f'您的BMI:{bmi:.1f},身體狀況為過輕,請多攝取營養以維持身體機能')

#args=['gcc','hello.c','world.c']
#args =['clean']
# args=['gcc']

# match args:
#     case ['gcc']:
#         print('gcc:missing source file(s).')
#     case ['gcc',file1,*files]:
#         print('gcc compile: '+file1+',',','.join(files))
#     case [clean]:
#         print(clean)
#     case _:
#         print('Invalid command')


# import math
# def xx(a,b,c):
#     x=(-b+math.sqrt(b**2-(4*a*c)))/(2*a)
#     y=(-b-math.sqrt(b**2-(4*a*c)))/(2*a)
#     return (x,y)


# print(xx(1,3,-4))

# def xx(a,b,*arg,g=99,name,age,**kw):
#     print(a,b)
#     print(g)
#     z=0
#     for i in arg:
#         z+=i
#     print(z)
#     print(name+"'s age is",age)
#     print(kw)


# xx(1,4,7,9,name='Josh',age=15,city='LA',gender='M')

# def num(n):
#     return num1(n,1)

# def num1(m,p):
#     if m==1:
#         return p
#     return num1(m-1,m*p)

# print(num(5))


# def move(n,a,b,c):
#     if n == 1:
#         return (f"{a} -> {c}")
#     move(n-1,a,b,c)
#     print('A -> C')
#     move(n-1,a,c,b)
#     print('A -> B')
#     move(n-1,c,a,b)
#     print('C -> B')




# def move(n, a, b, c):
#      if n == 1:
#           print(f'{a} --> {c}')
#      else:
#           move(n-1,a,c,b)
#           print(f'{a} --> {c}')
#           move(n-1,b,a,c)

# move(3,'A','B','C')


# def count():                # 建立一個 count 函式
#     a = []                    # 函式內有區域變數 a 是串列
#     def avg(val):             # 建立內置函式 avg ( 閉包 )
#         a.append(val)           # 將參數數值加入變數 a
#         #print(sum(a)/len(a))                # 印出 a
#         return sum(a)/len(a)    # 回傳 a 串列所有數值的平均
#     return avg                # 回傳 avg

# test = count()
# test(10)      # 將 10 存入 a
# test(11)      # 將 11 存入 a
# print(test(12))      

from functools import reduce

# def f(x,y):
#     return 10*x+y
# def c(m,n):
#     return m+n
# def m(a):
#     b={'0': 0, '1': '你', '2': 2, '3': '的', '4': 4, '5': '腳', '6': 6, '7': '踏', '8': 8, '9': '車'}
#     return b[a]

# print(reduce(c,map(m,'13579')))

# def normalize(name):
#      n1=name.upper()
#      n2=name.lower()
#      return n1[0]+n2[1:]
# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# from functools import reduce

# def prod(x,y):
#     return x*y
# print('3 * 5 * 7 * 9 =', reduce(prod,[3, 5, 7, 9]))
# if reduce(prod,[3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# def odd():
#     n=1 
#     while True:
#         n=n+2
#         yield n

# def delete(n):
#     return lambda x : x % n > 0

# def prime():
#     yield 2
#     it = odd()
#     while True:
#         n=next(it)
#         yield n 
#         it = filter(delete(n),it)

# for n in prime():
#      if n <100:
#         print(n)
#      else:
#         break
    
# def turn(n):
#     if str(n)[::-1] == str(n):
#         return n


# output=filter(turn,range(1,1000))
# print('1~1000',list(output))
# if list(filter(turn,range(1,200))) ==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def name(t):
#      return t[0]
# def num(t):
#      return t[1]
# L2 = sorted(L,key=num)
# print(L2)

# def createCounter():
#      a=0
#      def counter():
#         nonlocal a
#         a+=1
#         return a
#      return counter

# # 测试:
# counterB = createCounter()
# print ([counterB(), counterB(), counterB(), counterB()])
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')

# import keyboard
# def createCounter():
#      a=0
#      def counter():
#         nonlocal a
#         a+=1
#         return a
#      return counter
# CB = createCounter()
# def key(event):
#      if event.name == 'a':
#         print(CB())
#      elif event.name == 'esc':
#           print('結束')
#      else:
#         print('B')

# keyboard.on_press(key)

# keyboard.wait('esc')



# L = list(filter(lambda x:x%2>0, range(1, 100)))
     
# print(L)

# class Student(object):
#      def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender
#      def get_gender(self):
#          return self.__gender
#      def set_gender(self,gender):
#          self.__gender = gender
        


# # 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')

# str1 = 'abcde'
# str2 = 'ABCDE'
# str3 = str1 + str2
# str4 = ''

# for i in str3:
#     if i != 'c' and i != 'C':
#         #print(i)
#         str4 += i

# print(str4)

# q2ans = []
# q2ans.append('a')
# q2ans.append('b')
# print(q2ans)

# q3ans = {'K0':'V0'}
# q3ans['K1'] = 'V1'
# q3ans['K2'] = 'V2'
# print(q3ans)

# list1 = [["a","b"],["c","d"]]
# print(list1[0][1])

# n=0
# for i in range(1025):
#     n+=i
# print(n)    

# s = "hello"
# # 預期輸出: "olleh"
# def  upside_down(n): 
#     return n[::-1]
# print(upside_down(s))

# list2 = [1, 2, 3, 4, 5]
# # 預期輸出: 15
# n=0
# for i in list2:
#     n+=i
# print(n)

# list3 = [10, 15, 20, 25, 30, 35, 40]
# even_nums = []
# # 預期輸出: [10, 20, 30, 40]
# for i in list3:
#     if i % 2 ==0:
#         even_nums.append(i)
# print(even_nums)

# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# # 預期輸出: {"a": 1, "b": 2, "c": 3, "d": 4}
# dict1.update(dict2)
# merged_dict = dict1
# print(merged_dict)


s1 = "racecar"  # True
s2 = "python"   # False
s3 = 121
s4='.0.'
#print(s4)
def turn(n):
    if str(n) == str(n)[::-1]:
        print('TRUE')
    else:
        print('FALSE')
turn(s3)