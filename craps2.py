import tkinter as tk
from tkinter import messagebox
from random import randint, choice

# 定義 GUI
class GamblingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("擲骰子遊戲")
        self.root.geometry("400x500")

        self.money = 1000
        self.create_widgets()

    def create_widgets(self):
        self.money_label = tk.Label(self.root, text=f"目前籌碼: {self.money}", font=("Arial", 14))
        self.money_label.pack(pady=10)

        self.bet_label = tk.Label(self.root, text="輸入賭注:")
        self.bet_label.pack()
        self.bet_entry = tk.Entry(self.root)
        self.bet_entry.pack()

        self.odds_label = tk.Label(self.root, text="輸入賠率 (1-5):")
        self.odds_label.pack()
        self.odds_entry = tk.Entry(self.root)
        self.odds_entry.pack()

        self.roll_button = tk.Button(self.root, text="擲骰子", command=self.roll_dice)
        self.roll_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack()

    def roll_dice(self):
        try:
            bet = int(self.bet_entry.get())
            odds = int(self.odds_entry.get())
            if bet <= 0 or bet > self.money:
                messagebox.showerror("錯誤", "賭注必須在 1 到 目前籌碼之間")
                return
            if odds < 1 or odds > 5:
                messagebox.showerror("錯誤", "賠率必須在 1 到 5 之間")
                return
        except ValueError:
            messagebox.showerror("錯誤", "請輸入有效數字")
            return

        first = randint(1,6) + randint(1,6)
        result_text = f"🎲 骰出 {first} 點\n"

        if first in [7, 11]:
            self.money += bet * odds
            result_text += f"🎉 玩家勝! 目前籌碼: {self.money}"
        elif first in [2, 3, 12]:
            self.money -= bet * odds
            result_text += f"💀 莊家勝! 目前籌碼: {self.money}"
        else:
            result_text += f"🎲 進入下一輪, 目標點數: {first}\n"
            while True:
                current = randint(1,6) + randint(1,6)
                result_text += f"🎲 骰出 {current} 點\n"
                if current == first:
                    self.money += bet * odds
                    result_text += f"🎉 玩家勝! 目前籌碼: {self.money}"
                    break
                elif current == 7:
                    self.money -= bet * odds
                    result_text += f"💀 莊家勝! 目前籌碼: {self.money}"
                    break

        self.money_label.config(text=f"目前籌碼: {self.money}")
        self.result_label.config(text=result_text)

        if self.money <= 0:
            messagebox.showinfo("遊戲結束", "💀 已破產, 遊戲結束！")
            self.root.quit()

# 啟動 GUI
root = tk.Tk()
app = GamblingGame(root)
root.mainloop()
