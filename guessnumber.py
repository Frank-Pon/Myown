import random
answer = random.randint(1,100)
count = 0

def again(ans):
    """
    猜數字函數
    每次猜的次數都會記錄下來,並且回應猜高或猜低,直到猜中為止
    """
    global count
    count+=1
    if ans > answer:
        print(f"第{count}次猜高了,請繼續")
        return False
    elif ans < answer:
        print(f"第{count}次猜低了,請繼續")
        return False
    else:
        print(f"第{count}次猜中了!")
        return True
        


while True:
    try:
        guess = int(input("請猜一個數字:"))
        if guess >100 or guess<1:
            print("數字介於1-100,請重猜")
        else:
            if again(guess):
                break
    except ValueError:
        print("請輸入1-100的整數!")
