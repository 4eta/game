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
        return f"dealer: {self.cards}"
    
    def point_open(self):
        return f"dealer: {count_card(self.cards)}"
    
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
    
    def point_open(self):
        return f"dealer: {str_point(self.cards[0])}"
    
    def hit(self):
        self.cards.append(deck.draw_card())

for i in range(3):
    p = Player()
    print(p.cards)
    print(p.card_open())

