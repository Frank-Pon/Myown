perfect_num = []
def single(n):
    a=0
    a= sum(i for i in range(1,n) if n%i==0)
    if a == n:
        perfect_num.append(n)


def perfect(m):
    for i in range(1,m+1):
        single(i)


        
if __name__ == '__main__':
    perfect(10000)
    print(perfect_num)

#----------------------------------------------------

elem = []
perfect_num = []
def single(n):
    elem.clear()
    a=0
    for i in range(1,n):
        if n%i == 0:
            elem.append(i)
    for j in elem:
        a+=j
    if a == n:
        perfect_num.append(n)


def perfect(m):
    for i in range(1,m+1):
        single(i)


        
if __name__ == '__main__':
    perfect(10000)
    print(perfect_num)