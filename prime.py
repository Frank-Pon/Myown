prime_elem = []
prime = []
def prime_a(n):
    prime_elem.clear() # 常出錯,要記得清空list
    for i in range(1,n+1):
        if n%i == 0:
            prime_elem.append(i)
    if len(prime_elem)==2:
        prime.append(n)


def prime_b(m):
    for i in range(1,m+1):
        prime_a(i)
    print(prime)
    print("共",len(prime),"個質數")


if __name__ == '__main__':
    prime_b(100)