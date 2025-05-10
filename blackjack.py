import random
import json
global d_sum
global p1_sum
global p2_sum
global p3_sum
global p4_sum
global d_cards
global d1_cards
global p1_cards
global p2_cards
global p3_cards
global p4_cards
global p1_sprit
global p2_sprit
global p3_sprit
global p4_sprit
global p1_spcar
global p2_spcar
global p3_spcar
global p4_spcar
global p1_sum
global p2_sum
global p3_sum
global p4_sum
global p1_bet
global p2_bet
global p3_bet
global p4_bet
global p1_sta
global p2_sta
global p3_sta
global p4_sta
global p1_money
global p2_money
global p3_money
global p4_money
global Ace

num_list = list(range(52))
suits = ["♤", "♧", "♡", "♢"]
numbers = ["A","2,","3","4","5","6","7","8","9","10","J","Q","K"]
trump_deck = [f"{suit}{number}" for suit in suits for number in numbers]
d_sum = (0)
p1_sum = (0)
p2_sum = (0)
p3_sum = (0)
p4_sum = (0)
p1_bet = ["0"]
p2_bet = ["0"]
p3_bet = ["0"]
p4_bet = ["0"]
p1_sprit = (0)
p2_sprit = (0)
p3_sprit = (0)
p4_sprit = (0)
d_cards = []
d1_cards = []
p1_cards = []
p2_cards = []
p3_cards = []
p4_cards = []
p1_spcar = []
p2_spcar = []
p3_spcar = []
p4_spcar = []
p1_name = "1p"
p2_name = "2p"
p3_name = "3p"
p4_name = "4p"
Ace = "♧A", "♤A", "♡A", "♢A"





def BJcon(shuffle, deck, cards, total, p_name, p_bet, p_cards):
    num = shuffle.pop(0)
    cards.append(deck[num])
    num = (num+1)%13
    #print(num)
    print(cards)
    if num == 11:
        num = 10
    elif num == 12:
        num = 10
    elif num == 0:
        num = 10
    elif num == 1:
        num = 11
    if p_name == "ディーラー":
        score = num + total
        return score, 0
    elif p_bet[0] == "split":
        score = num + total
        return score, 0, p_bet
    if len(p_cards) == 2 and num == total:
        while True:
            ans = input(f"{p_name}\n今の手札は{cards}です\nスプリット:s\n:なにもしない:n")
            if ans == "s":
                score = total
                p1_spcar = cards.pop(0)
                p_bet = ["split", p_bet[0], p_bet[0]]
                return score, score, p_bet
            elif ans == "n":
                break
            else:
                print("ちょっと何言ってるかわからない")

    if len(p_cards) == 2 and num + total == 21 and any(Aces in d1_cards for Aces in Ace):
        score = num + total
        while True:
            ans = input(f"{p_name}\nディーラーのアップカードは{d1_cards}です\n今の手札は{cards}です\nイーブンマネー:e\n:なにもしない:n")
            if ans == "e":
                print("イーブンマネーしました")
                p_bet = ["evenmoney", p_bet[0]]
                return score, 0, p_bet
            elif ans == "n":
                break
            else:
                print("ちょっと何言ってるかわからない")

    if len(p_cards) == 2 and any(Aces in d1_cards for Aces in Ace):
        score = num + total
        while True:
            ans = input(f"{p_name}\nディーラーのアップカードは{d1_cards}です\n今の手札は{cards}です\nインシュアランス:i\n:なにもしない:n")
            if ans == "i":
                while True:
                    betable = int((p_bet[0] / 2))
                    bet = int(input(f"{p_name}\n何ベットを保険に当てますか？(上限は{betable}$までです)"))
                    if betable >= bet:
                        betable = p_bet[0] - betable
                        p_bet = ["insurance", betable, betable]
                        print("上乗せしました")
                        return score, 0, p_bet
                    else:
                        print("ちょっと何言ってるかわからない")
            elif ans == "n":
                break

            else:
                print("ちょっと何言ってるかわからない")
    if len(p_cards) == 2:
        score = num + total
        status = True
        while status:
            ans = input(f"{p_name}\nディーラーのアップカードは{d1_cards}です\n今の手札は{cards}です\nダブリングダウン:d\nサレンダー:s\n:なにもしない:n")
            if ans == "d":
                while True:
                    bet = int(input(f"{p_name}\n何ベット上乗せしますか？(上限は{p_bet}$までです)"))
                    if p_bet[0] >= bet:
                        p_bet = ["double", p_bet[0] + bet, bet]
                        print("上乗せしました")
                        return score, 0, p_bet
                    else:
                        print("ちょっと何言ってるかわからない")
            elif ans == "s":
                while True:
                    ans = input("本当にサレンダーしますか？\nはい:y\nいいえ:n")
                    if ans == "n":
                        break
                    elif ans == "y":
                        bet = int(p_bet[0] / 2)
                        p_bet = ["surrender", bet, bet]
                        return score, 0, p_bet
                    else:
                        print("ちょっと何言ってるかわからない")
            elif ans == "n":
                    score = num + total
                    p_bet = ["not", p_bet[0]]

                    return score, 0, p_bet
            else:
                print("ちょっと何言ってるかわからない")
    score = num + total
    return score, 0, p_bet


def Acechange(d_cards):
    if "♧A" in d_cards:
        index = d_cards.index("♧A")
        d_cards[index] = "♤A "
    elif "♤A" in d_cards:
        index = d_cards.index("♤A")
        d_cards[index] = "♤A "
    elif "♡A" in d_cards:
        index = d_cards.index("♡A")
        d_cards[index] = "♡A "
    elif "♢A" in d_cards:
        index = d_cards.index("♢A")
        d_cards[index] = "♢A "
    return d_cards

def hit(p_name, num_shuffle, trump_deck, cards, total, p_bet):
    while True:
        if len(cards) == 2 and int(total) == 21 and p_bet[0] != "split":
            input(f"{p_name}\n現在の手札:{cards}です\n何か入力してください")
            return total, cards, 0
        elif p_bet[0] == "surrender":
            return total, cards, 0
        ans = input(f"{p_name}\n現在の手札:{cards}です\nスタンド:s\n　ヒット:h")
        if ans == "h":
            total, sprit, p_bet = BJcon(num_shuffle, trump_deck, cards, total, p_name, p_bet, [])
            print(total)
            if any(Aces in cards for Aces in Ace) and int(total) > 21:
                total = int(total) - 10
                Acechange(d_cards)
                print("ACEを1とカウントします")
            if int(total) > 21:
                total = (0)
                print(p_name,"はバーストしました")
                return total, cards, 0
            if p_bet[0] == "double":
                return total, cards, 0
        elif ans == "s":
            return total, cards, 0
        else:
            print("ちょっと何言ってるかわからない")


def result_all(p_name, p_sum, p_bet, p_cards, p_money):
    print(f"{p_name}の手札は{p_cards}")
    if p_bet[0] == "split":
        if len(d_cards) == 2 and d_sum == 21 and any(Aces in d_cards for Aces in Ace):
            print(p_name,"負け！")
            result = p_bet[1] * 0
            print(f"払い戻しは{result}＄です")
        elif d_sum == p_sum:
            print(p_name,"引き分け！")
            result = p_bet[1] * 1
            print(f"払い戻しは{result}＄です")
        elif d_sum < p_sum:
            print(p_name,"勝ち！")
            result = p_bet[1] * 2
            print(f"払い戻しは{result}＄です")
        else:
            print(p_name,"負け！")
            result = p_bet[1] * 0
            print(f"払い戻しは{result}＄です")
    elif p_bet[0] == "evenmoney":
        print("BlackJack！！")
        result = p_bet[1] * 2
        print(f"払い戻しは{result}＄です")
    elif p_bet[0] == "insurance":
        if len(d_cards) == 2 and d_sum == 21 and any(Aces in d_cards for Aces in Ace):
            print(p_name,"負け！")
            result = p_bet[1] * 0 + p_bet[2] * 3
            print(f"払い戻しは{result}＄です")
        elif d_sum == p_sum:
            print(p_name,"引き分け！")
            result = p_bet[1] * 1
            print(f"払い戻しは{result}＄です")
        elif d_sum < p_sum:
            print(p_name,"勝ち！")
            result = p_bet[1] * 2
            print(f"払い戻しは{result}＄です")
        else:
            print(p_name,"負け！")
            result = p_bet[1] * 0 + p_bet[2] * 3
            print(f"払い戻しは{result}＄です")
    elif p_bet[0] == "double":
        p_money = p_money - p_bet[2]
        if len(d_cards) == 2 and p_sum == 21 and any(Aces in d_cards for Aces in Ace):
            print(p_name,"負け！")
            result = p_bet[1] * 0
            print(f"払い戻しは{result}＄です")
        elif d_sum == p_sum:
            print(p_name,"引き分け！")
            result = p_bet[1] * 1
            print(f"払い戻しは{result}＄です")
        elif d_sum < p_sum:
            print(p_name,"勝ち！")
            result = p_bet[1] * 2
            print(f"払い戻しは{result}＄です")
        else:
            print(p_name,"負け！")
            result = p_bet[1] * 0
            print(f"払い戻しは{result}＄です")
    elif p_bet[0] == "surrender":
        result = p_bet[1]
        print("サレンダーしました")
        print(f"払い戻しは{result}＄です")
    else:
        if len(d_cards) == 2 and d_sum == 21 and any(Aces in d_cards for Aces in Ace) and p_sum == 21 and any(Aces in p_cards for Aces in Ace):
            print(p_name,"引き分け！")
            result = p_bet[1] * 1
            print(f"払い戻しは{result}＄です")
        elif len(p_cards) == 2 and p_sum == 21 and any(Aces in p_cards for Aces in Ace):
            print(p_name,"BlackJack")
            result = p_bet[1] * 2.5
            print(f"払い戻しは{int(result)}＄です")
        elif d_sum == p_sum:
            print(p_name,"引き分け！")
            result = p_bet[1] * 1
            print(f"払い戻しは{result}＄です")
        elif d_sum < p_sum:
            print(p_name,"勝ち！")
            result = p_bet[1] * 2
            print(f"払い戻しは{result}＄です")
        else:
            print(p_name,"負け！")
            result = p_bet[1] * 0
            print(f"払い戻しは{result}＄です")
    p_money = p_money + int(result)
    print(p_money)
    return p_money



#p1_name = input("プレイヤー1の名前を入力してください:")
#p2_name = input("プレイヤー2の名前を入力してください:")
#p3_name = input("プレイヤー3の名前を入力してください:")
#p4_name = input("プレイヤー4の名前を入力してください:")

with open("money.json", "r") as f:
    datalist = json.load(f)

print(datalist)
if p1_name in datalist:
    p1_money = datalist[p1_name]
else:
    p1_money = 10000

if p2_name in datalist:
    p2_money = datalist[p2_name]
else:
    p2_money = 10000

if p3_name in datalist:
    p3_money = datalist[p3_name]
else:
    p3_money = 10000

if p4_name in datalist:
    p4_money = datalist[p4_name]
else:
    p4_money = 10000

print("あなたの現在の掛け金は",p1_money,"＄です")
print("あなたの現在の掛け金は",p2_money,"＄です")
print("あなたの現在の掛け金は",p3_money,"＄です")
print("あなたの現在の掛け金は",p4_money,"＄です")


#p1_bet = int(input(f"{p1_name}\n掛け金を数字で入力してください:"))
#p2_bet = int(input(f"{p2_name}\n掛け金を数字で入力してください:"))
#p3_bet = int(input(f"{p3_name}\n掛け金を数字で入力してください:"))
#p4_bet = int(input(f"{p4_name}\n掛け金を数字で入力してください:"))

p1_bet = [10]
p2_bet = [10]
p3_bet = [10]
p4_bet = [10]

p1_money = p1_money - p1_bet[0]
p2_money = p2_money - p2_bet[0]
p3_money = p3_money - p3_bet[0]
p4_money = p4_money - p4_bet[0]


num_shuffle = num_list
random.shuffle(num_shuffle)
#print(num_shuffle)
print(p1_bet)
#-------------------------------1回目-------------------------------------
p1_sum, p1_sprit, p1_bet = BJcon(num_shuffle, trump_deck, p1_cards, p1_sum, p1_name, p1_bet, p1_cards)
print(p1_sum)
print(p1_bet)
p2_sum, p2_sprit, p2_bet = BJcon(num_shuffle, trump_deck, p2_cards, p2_sum, p2_name, p2_bet, p2_cards)
print(p2_sum)
print(p2_bet)
p3_sum, p3_sprit, p3_bet = BJcon(num_shuffle, trump_deck, p3_cards, p3_sum, p3_name, p3_bet, p3_cards)
print(p3_sum)
print(p3_bet)
p4_sum, p4_sprit, p4_bet = BJcon(num_shuffle, trump_deck, p4_cards, p4_sum, p4_name, p4_bet, p4_cards)
print(p4_sum)
print(p4_bet)
d_sum, d_sprit2 = BJcon(num_shuffle, trump_deck, d_cards, d_sum, "ディーラー", 0,[])
print(d_sum)
d1_cards = d_cards
#-------------------------------2回目------------------------------------
p1_sum, p1_sprit, p1_bet = BJcon(num_shuffle, trump_deck, p1_cards, p1_sum, p1_name, p1_bet, p1_cards)
print(p1_sum)
print(p1_bet)
p2_sum, p2_sprit, p2_bet = BJcon(num_shuffle, trump_deck, p2_cards, p2_sum, p2_name, p2_bet, p2_cards)
print(p2_sum)
print(p2_bet)
p3_sum, p3_sprit, p3_bet = BJcon(num_shuffle, trump_deck, p3_cards, p3_sum, p3_name, p3_bet, p3_cards)
print(p3_sum)
print(p3_bet)
p4_sum, p4_sprit, p4_bet = BJcon(num_shuffle, trump_deck, p4_cards, p4_sum, p4_name, p4_bet, p4_cards)
print(p4_sum)
print(p4_bet)
d_sum, d_sprit2 = BJcon(num_shuffle, trump_deck, d_cards, d_sum, "ディーラー", 0,[])
print(d_sum)
#------------------------------引くぅ？------------------------------------
print(p1_name, num_shuffle, trump_deck, p1_cards, p1_sum, p1_bet)
p1_sum, p1_cards, p1_sprit = hit(p1_name, num_shuffle, trump_deck, p1_cards, p1_sum, p1_bet)
if p1_sprit != 0:
    print("スプリットしました")
    p1_sprit, p1_spcar = hit(p1_name, num_shuffle, trump_deck, p1_cards, p1_sprit, p1_bet)

p2_sum, p2_cards, p2_sprit = hit(p2_name, num_shuffle, trump_deck, p2_cards, p2_sum, p2_bet)
if p2_sprit != 0:
    print("スプリットしました")
    p2_sprit, p2_spcar = hit(p2_name, num_shuffle, trump_deck, p2_cards, p2_sprit, p2_bet)

p3_sum, p3_cards, p3_sprit = hit(p3_name, num_shuffle, trump_deck, p3_cards, p3_sum, p3_bet)
if p3_sprit != 0:
    print("スプリットしました")
    p3_sprit, p3_spcar = hit(p3_name, num_shuffle, trump_deck, p3_cards, p3_sprit, p3_bet)

p4_sum, p4_cards, p4_sprit = hit(p4_name, num_shuffle, trump_deck, p4_cards, p4_sum, p4_bet)
if p4_sprit != 0:
    print("スプリットしました")
    p4_sprit, p4_spcar = hit(p4_name, num_shuffle, trump_deck, p4_cards, p4_sprit, p4_bet)



if int(d_sum) < 17:
    while True:
        d_sum, blank_cards = BJcon(num_shuffle, trump_deck, d_cards, d_sum, "ディーラー", 0,[])
        if int(d_sum) > 17:
            if int(d_sum) <= 21:
                break
            if any(Aces in d_cards for Aces in Ace) and int(d_sum) > 21:
                d_sum = d_sum - 10
                Acechange(d_cards)
            if int(d_sum) > 21:
                d_sum = (0)
                print("ディーラーはバーストしました")
                break

#-----------------------------勝負！！！------------------------------------

print("ディーラーのカードは、")
print(d_cards)
print(p1_money,p2_money,p3_money,p4_money)
p1_money = result_all(p1_name, p1_sum, p1_bet, p1_cards, p1_money)
p2_money = result_all(p2_name, p2_sum, p2_bet, p2_cards, p2_money)
p3_money = result_all(p3_name, p3_sum, p3_bet, p3_cards, p3_money)
p4_money = result_all(p4_name, p4_sum, p4_bet, p4_cards, p4_money)

#---------------------------保存-------------------------------------------
datalist = {p1_name: p1_money,p2_name: p2_money,p3_name: p3_money,p4_name:p4_money}
with open("money.json", "w") as f:
    json.dump(datalist, f)