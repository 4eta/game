from django.shortcuts import render
from numpy import place
from . import bj

# Create your views here.

def card_path(cards):
    pass

def game(request):
    if request.method == "GET":
        game_flag = False
        player_turn = True
        deck = bj.Deck()
        player = bj.Player()
        dealer = bj.Player()

        player.cards = [deck.emission(),deck.emission()]
        dealer.cards = [deck.emission(),deck.emission()]

        request.session["deck"] = deck
        request.session["player"] = player
        request.session["deqler"] = dealer
        request.session["player_turn"] = player_turn
        request.session["game_flag"] = game_flag

        d = {
            "message":"let's start",
            "dealer_card":["card_back.png","card_back.png"],
            "player_card":["card_back.png","card_back.png"],
            "dealer_point":0,
            "player_point":0,
        }

        return render(request, "game.html", d)
    
    elif request.methos == "POST":
        deck = request.session("deck")
        player = request.session("player")
        dealer = request.session("dealer")
        player_turn = request.session("player_turn")
        game_flag = request.session("game_flag")

        if "hit" in request.POST:
            player.draw(deck.emission())
        elif "stand" in request.POST:
            player_turn = False
        
        if bj.count_card(player.cards) > 21:
            game_flag = True
        elif bj.count_card(dealer.cards) > 16 and not player_turn:
            game_flag = True

        if not game_flag:
            if player_turn:
                player_point = bj.count_card(player.cards)
                dealer_point = bj.str_point(dealer.cards[0])

                dealer_close = [[""], ["card_back.png"]]
                dealer_close[0] = dealer.cards[0]

                if player_point == 21:
                    player_turn = False
                    
                    request.session["deck"] = deck
                    request.session["player"] = player
                    request.session["deqler"] = dealer
                    request.session["player_turn"] = player_turn
                    request.session["game_flag"] = game_flag

                    d = {
                        "message":"Black Jack !!!",
                        "dealer_card":["card_back.png","card_back.png"],
                        "player_card":["card_back.png","card_back.png"],
                        "dealer_point":0,
                        "player_point":0,
                    }

            else:
                pass
        

