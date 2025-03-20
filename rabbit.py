rabbit = [1,1]
def bodi(n):
    for i in range (n-2):
        num = rabbit[-1]+rabbit[-2]
        rabbit.append(num)
    return rabbit

print(bodi(20))