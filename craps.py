from random import randint,choice


revived_scenarios=[  #復活隨機觸發以下情境
"轉頭踩到鈔票,撿起{amount}元",
"電視上正在播報彩券開獎,拿出手上的彩券居然中獎了,兌獎得到{amount}元",
"離開之前,摸了褲子口袋,居然摸到{amount}元",
"不小心跌倒,倒在地上時發現桌下的{amount}元",
"酒館老闆：你這傢伙真有趣,這{amount}元給你,繼續玩吧"
]

money = 1000 #設定籌碼
while money>0: #如果有籌碼的話
    print(f"目前籌碼：{money}") #讓玩家知道籌碼有多少
    while True: #設定無限迴圈
        try:        
            debt = int(input("請輸入賭注:")) #輸入賭注
            if debt<=0 or debt>money: 
                print(f"賭注必須在1與{money}之間")  #賭注要在0跟籌碼之間
            else:
                break       #如果有在0跟籌碼之間就跳出迴圈
        except ValueError: #如果輸入非數字重填
            print("請輸入有效數字")
    while True:#設定無限迴圈
        try: 
            odds = int(input("請輸入賠率:")) #賠率要在0~5之間
            if 0<odds<=5 : #如果符合條件就跳出迴圈
                break
            else:
                print("賠率必須在1與5之間")
        except ValueError:#如果輸入非數字重填
                print("請輸入有效數字")
    first = randint(1,6)+randint(1,6) #骰出第一次點數
    print(f"骰出{first}點") #讓玩家知道骰出結果
    if first == 7 or first == 11: #如果點數是7或11玩家贏
        money+=(debt * odds)
        print(f"玩家勝,目前籌碼:{money}")
    elif first == 2 or first ==3 or first==12:#如果點數是2或3或12莊家贏
        money-=(debt * odds)
        money = max(0,money)
        print(f"莊家勝,目前籌碼:{money}") #------------以上為第一次骰出結果判定--------------------
    else:
        print(f"進入下一輪,目標點數:{first}")#告訴玩家第二輪要骰到目標點數才贏
        need_go_on = True #設定迴圈條件
        while need_go_on:     
            current = randint(1,6)+randint(1,6) #此次骰出結果
            print(f"骰出{current}點")#告訴玩家骰出點數
            if   current == first: #如果此次與初次結果相同,玩家贏
                money+=(debt * odds)
                print(f"玩家勝,目前籌碼:{money}") 
                need_go_on = False #將迴圈條件關閉,停止遊戲
            elif current == 7:#如果骰到7,莊家贏
                money-=(debt * odds)
                money = max(0,money)
                print(f"莊家勝,目前籌碼:{money}")
                need_go_on = False  #將迴圈條件關閉,停止遊戲
    if money <=0: #-----------以下為復活機制,當籌碼0時觸發-------------
        recover = randint(1,999)#隨機範圍 1000
        if recover <=10: #10/1000 約為1% -- 1%機會復活得到1000籌碼
            money+=1000
            amount = 1000
        elif recover<=50:#(50-10)/1000 約為4% -- 4%機會復活得到500籌碼
            money+=500
            amount = 500
        elif recover <=100:#(100-50)/1000 約為5% -- 5%機會復活得到100籌碼  --總復活機率為10%
            money+=100
            amount =100
        else:
            print("已破產,遊戲結束!") #籌碼歸0且無觸發復活則結束遊戲
            break
        print(f"{choice(revived_scenarios).format(amount=amount)},目前籌碼:{money},請繼續遊戲!")#觸發復活情境得到額外籌碼
        continue

