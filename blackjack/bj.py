import random
import time

suits = ["d", "h", "s", "c"]

class Deck:
    
    def __init__(self):
        self.cards = []
        for i in range(1,14):
            for suit in suits:
                self.cards.append([i, suit])
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

def str_point(card):
    if card[0] == 1:
        return 11
    else:
        return min(10, card[0])

def count_card(cards):
    point = [str_point(it) for it in cards]
    cnt = point.count(11)
    score = sum(point)
    for i in range(cnt):
        if score > 21:
            score -= 10
    return score

deck = Deck()

class Player():
    
    def __init__(self):
        self.cards = [deck.draw_card(), deck.draw_card()]
    
    def card_open(self):
        return f"player: {self.cards}"
    
    def point_open(self):
        return f"player: {count_card(self.cards)}"
    
    def hit(self):
        self.cards.append(deck.draw_card())

class Dealer():
    def __init__(self):
        self.cards = [deck.draw_card(), deck.draw_card()]
    
    def card_open(self):
        return f"dealer: {self.cards}"
    
    def point_open(self):
        return f"dealer: {count_card(self.cards)}"

    def card_close(self):
        return f"dealer: {self.cards[0]},[?,?]"
    
    def point_close(self):
        return f"dealer: {str_point(self.cards[0])}"
    
    def hit(self):
        self.cards.append(deck.draw_card())


def game():

    player = Player()
    print(player.card_open())
    print(player.point_open())

    dealer  = Dealer()
    print(dealer.card_close())
    print(dealer.point_close())

    select = 0
    while count_card(player.cards) <= 21:
        time.sleep(2)
        if count_card(player.cards) == 21:
            print("Black Jack !!!")
            return 1
        select = input("do you draw a card?\nyes:1, no:0 ")

        if select == "1":
            player.hit()
            print(player.card_open())
            print(player.point_open())
        else:
            break
    else:
        print("BARST !!")
        return 0

    time.sleep(1)

    print(dealer.card_open())
    time.sleep(1)
    print(dealer.point_open())

    while count_card(dealer.cards) < 17:
        time.sleep(1)
        dealer.hit()
        print(dealer.card_open())
        time.sleep(1)
        print(dealer.point_open())
        if count_card(dealer.cards) > 21:
            return 1
    
    time.sleep(1)

    if count_card(dealer.cards) < count_card(player.cards):
        return 1
    elif count_card(dealer.cards) > count_card(player.cards):
        return 0
    else:
        return -1

start = 1
win_lose = [0,0]

deck = Deck()

while len(deck.cards) > 10:
    start = input("do you start game?\nyes:1, no:0 ")
    if start != "1":
        print("quit game")
        break
    print("let's start game")
    result = game()
    if result == 1:
        win_lose[0] += 1
        print("you win !!")
        print("win:", win_lose[0], " lose:", win_lose[1])
    elif result == 0:
        win_lose[1] += 1
        print("you lose !!")
        print("win:", win_lose[0], " lose:", win_lose[1])
    else:
        print("draw !!")
        print("win:", win_lose[0], " lose:", win_lose[1])
print("there is no card")