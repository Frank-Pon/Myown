import os
import time


def main():
    content = '歡迎你…………'
    while True:
        # 清理螢幕上的輸出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.1)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()