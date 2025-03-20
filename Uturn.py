def is_palindrome(num):
    """判斷一個數是不是迴文數"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

if __name__ == '__main__':
    print(is_palindrome("SNS"))