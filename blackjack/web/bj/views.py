from django.shortcuts import render
from numpy import place
from . import bj

# Create your views here.

def card_path(cards):
    path = []
    for card in cards:
        suit = card[1]
        num = str(card[0]).zfill(2)
        name = f"card_{suit}_{num}.png"
        path.append(name)
    return path

def game(request):
    if request.method == "GET" or "restart" in request.POST:
        game_flag = False
        player_turn = True
        deck = bj.Deck()
        player = bj.Player()
        dealer = bj.Player()

        player.cards = [deck.emission(),deck.emission()]
        dealer.cards = [deck.emission(),deck.emission()]

        request.session["deck"] = deck
        request.session["player_turn"] = player_turn
        request.session["game_flag"] = game_flag
        request.session["player"] = player
        request.session["dealer"] = dealer

        d = {
            "message":"とりあえず作ったブラックジャック",
            "dealer_card":["card_ura_00.png","card_ura_00.png"],
            "player_card":["card_ura_00.png","card_ura_00.png"],
            "dealer_point":0,
            "player_point":0,
        }

        return render(request, "game.html", d)
    
    elif request.method == "POST":
        deck = request.session["deck"]
        player_turn = request.session["player_turn"]
        game_flag = request.session["game_flag"]
        player = request.session["player"]
        dealer = request.session["dealer"]
        
        #プレイヤーターンの処理
        if "hit" in request.POST:
            player.draw(deck.emission())
        elif "stand" in request.POST:
            player_turn = False
        
        #ゲームが終わるかの処理
        if bj.count_card(player.cards) > 21:
            game_flag = True
        elif bj.count_card(dealer.cards) > 16 and not player_turn:
            game_flag = True

        #ゲームが終わらない場合
        if not game_flag:
            #プレイヤーターンの場合
            if player_turn:
                player_point = bj.count_card(player.cards)
                dealer_point = bj.str_point(dealer.cards[0])

                dealer_close = [[""], [0,"ura"]]
                dealer_close[0] = dealer.cards[0]

                #合計が21の場合はすぐに終わらせる(コーナーケース)
                if player_point == 21:
                    player_turn = False
                    game_flag = True
                    request.session["deck"] = deck
                    request.session["player"] = player
                    request.session["dealer"] = dealer
                    request.session["player_turn"] = player_turn
                    request.session["game_flag"] = game_flag

                    d = {
                        "message":"Black Jack !!!",
                        "dealer_card":card_path(dealer_close),
                        "player_card":card_path(player.cards),
                        "dealer_point":dealer_point,
                        "player_point":player_point,
                        "turn":player_turn,
                        "flag":game_flag,
                    }

                    return render(request, "game.html", d)
                
                #プレイヤーがカードを引くかそのままか選ぶ
                else:
                    request.session["deck"] = deck
                    request.session["player"] = player
                    request.session["dealer"] = dealer
                    request.session["player_turn"] = player_turn
                    request.session["game_flag"] = game_flag

                    d = {
                        "message":"Do you draw more card ?",
                        "dealer_card":card_path(dealer_close),
                        "player_card":card_path(player.cards),
                        "dealer_point":dealer_point,
                        "player_point":player_point,
                        "turn":player_turn,
                        "flag":game_flag,
                    }

                    return render(request, "game.html", d)

            
            #ディーラーターンの場合
            else:
                player_point = bj.count_card(player.cards)
                dealer_point = bj.count_card(dealer.cards)
                
                dealer.draw(deck.emission())

                request.session["deck"] = deck
                request.session["player"] = player
                request.session["dealer"] = dealer
                request.session["player_turn"] = player_turn
                request.session["game_flag"] = game_flag

                d = {
                    "message":"Dealer draw a card.",
                    "dealer_card":card_path(dealer.cards),
                    "player_card":card_path(player.cards),
                    "dealer_point":dealer_point,
                    "player_point":player_point,
                    "turn":player_turn,
                    "flag":game_flag,
                }

                return render(request, "game.html", d)

        #ゲームが終わった場合
        else:
            player_point = bj.count_card(player.cards)
            dealer_point = bj.count_card(dealer.cards)

            player_turn = False

            if player_point > 21:
                msg = "You lose !"
            elif dealer_point > 21:
                msg = "You win !!"
            elif player_point == dealer_point:
                msg = "draw !"
            elif player_point < dealer_point:
                msg = "You lose !"
            else:
                msg = "You win !!"

            d = {
                "message":msg,
                "dealer_card":card_path(dealer.cards),
                "player_card":card_path(player.cards), 
                "dealer_point":dealer_point,
                "player_point":player_point, 
                "turn":player_turn,
                "flag":game_flag,
            }

            return render(request, "game.html", d)


        

