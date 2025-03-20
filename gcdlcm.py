def gcd(x,y):
    (x,y) = (y,x) if x>y else (x,y)

    for i in range(x,0,-1):
        if x%i==0 and y%i==0:
            return i
        
def lcm(x,y):
    a=x*y//gcd(x,y)
    return a


if __name__ == '__main__':
    print(gcd(17,19))
    print(lcm(17,19))