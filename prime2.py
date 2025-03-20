import math

def prime_a(n):
    if n<2: #排除0、1
        return False
    if n==2: #唯一偶數質數
        return True
    if n %2 ==0: #排除2以外的偶數
        return False
    for i in range(3,int(math.sqrt(n))+1,2): #判斷奇數是否為質數
        if n%i ==0: #平方根有因數就不是質數
            return False
    return True
    


def prime_b(m):
    prime = [i for i in range(1,m+1) if prime_a(i)]
    print(prime)
    print("共",len(prime),"個質數")


if __name__ == '__main__':
    prime_b(100)