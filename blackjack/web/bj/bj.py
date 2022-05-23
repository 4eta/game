import random

def str_point(card):
    if card[0] == 1:
        return 11
    else:
        return min(10, card[0])

def count_card(cards):
    point = [str_point(it) for it in cards]
    score = sum(point)
    for _ in range(point.count(11)):
        if score > 21:
            score -= 10
    return score

class Deck:
    
    def __init__(self):
        self.cards = []
        for i in range(1,14):
            for suit in ["d", "h", "s", "c"]:
                self.cards.append([i, suit])
        random.shuffle(self.cards)

    def emission(self):
        return self.cards.pop()

class Player():
    
    def __init__(self):
        self.cards = []
    
    def draw(self, card):
        self.cards.append(card)