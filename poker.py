
import random
import numpy as np

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for i in ("Hearts","Spades","Diamonds","Clubs"):
            self.cards.append(Card("Ace",i))
            for j in range(2,11):
                self.cards.append(Card(j,i))
            for k in ("Jack","Queen","King"):
                self.cards.append(Card(k,i))

    def show(self):
        for i in self.cards:
            i.show()

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawcard(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.chips = 0
        self.folded = False
        self.played = False
        self.callreq = 0
        self.roundcontribution = 0

    def showchips(self):
        print(self.chips)

    def draw(self, deck, num):
        for i in range(num):
            self.hand.append(deck.drawcard())
        return self

    def showhand(self):
        for card in self.hand:
            card.show()

    def place_bet(self,bet):
        if bet <= self.chips:
            self.chips = self.chips - bet
            table.chips += bet
            self.roundcontribution += bet
        else:
            print("You do not have enough chips")

    def receive_chips(self, amount):
        self.chips += amount

    def play(self):
        update_callreqs()
        table.showhand()
        self.showhand(), self.showchips()
        print("{} to call".format(self.callreq))
        end = False
        if self.folded:
            return end
        else:
            if self.callreq ==0:
                
                if self.played:
                    end = True
                    return end
                else:
                    self.played = True
                    print("Check or raise?")
                    action = input()
                    if action == "check":
                        self.place_bet(self.callreq)
                        return
                    elif action == "raise":
                        print("What do you raise by?")
                        plyraise = int(input())
                        self.place_bet(self.callreq+plyraise)
                        return
                    elif action =="fold":
                        self.folded = True
                        return
                    else:
                        print("invalid")
                    return end
                    
            else:
                self.played = True
                print("Call, raise or fold?")
                action = input()
                if action == "call":
                    self.place_bet(self.callreq)
                    return
                elif action == "raise":
                    print("What do you raise by?")
                    plyraise = int(input())
                    self.place_bet(self.callreq+plyraise)
                    return
                elif action =="fold":
                    self.folded = True
                    return
                else:
                    print("invalid")
                    
def update_callreqs():
    contrib_requirement = np.amax([player1.roundcontribution,player2.roundcontribution,player3.roundcontribution])
    player1.callreq = contrib_requirement - player1.roundcontribution
    player2.callreq = contrib_requirement - player2.roundcontribution
    player3.callreq = contrib_requirement - player3.roundcontribution
    return

def initialize_hand():
    deck = Deck()
    player1.folded = False
    player2.folded = False
    player3.folded = False
    player1.hand = []
    player2.hand = []
    player3.hand = []
    table.chips = 0
    player1.draw(deck,2)
    player2.draw(deck,2)
    player3.draw(deck,2)
    blind = 5
    player3.place_bet(blind)
    return deck

table = Player("Table")
player1 = Player("Player 1")
player2 = Player("Player 2")
player3 = Player("Player 3")

table.chips = 0
player1.chips = 100
player2.chips = 100
player3.chips = 100

def play_round(round):
    deck = []
    if round == 0:
        deck = initialize_hand()
        play_turns()
        round += 1
    elif round == 1:
        table.draw(deck,3)
        play_turns()
        round += 1 
    elif round == 2 or 3:
        table.draw(deck,1)
        play_turns()
        round += 1
    else:
        print("End of hand")
        round = 0

    player1.played = False
    player2.played = False
    player3.played = False
    play_round(round)

def play_turns():
    turn = 0
    end = False
    while not end:
        if turn%3 == 0:
            end = player1.play()
            update_callreqs()
            turn += 1
        elif turn%3 == 1:
            end = player2.play()
            update_callreqs()
            turn += 1
        elif turn%3 == 2:
            end = player3.play()
            update_callreqs()
            turn += 1
        continue


play_round(0)