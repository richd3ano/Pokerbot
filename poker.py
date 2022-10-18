import random
from timeit import repeat

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
        else:
            print("You do not have enough chips")

    def receive_chips(self, amount):
        self.chips += amount

    def play(self,callreq):
        table.showhand()
        self.showhand(), self.showchips()

        if callreq == 0:
            print("check or raise?")
        else:
            print("call, raise or fold?")

        action = input()

        if action == "call" or "check":
            self.place_bet(callreq)
            callreq = 0
            return callreq
        elif action == "raise":
            print("What do you raise by?")
            plyraise = int(input())
            self.place_bet(callreq+plyraise)
            callreq = plyraise
            return callreq
        elif action =="fold":
            callreq = callreq*-1
            return callreq

        else:
            print("invalid")
        
deck = Deck()
table = Player("Table")
player1 = Player("Player 1")
player2 = Player("Player 2")
player3 = Player("Player 3")

def begin_flop(num_players):
    table.draw(deck,3)

    turn = 0
    callrequ = 0

    while callrequ > 0 or turn < num_players:
        if turn == 0:
            print("Player 1")
            status = player1.play(callrequ)
            turn += 1
            callrequ = status
            table.showchips()
        elif turn ==1:
            print("Player 2")
            status = player2.play(callrequ)
            turn += 1
            callrequ = status
            table.showchips()
        elif turn ==2:
            print("Player 3")
            status = player3.play(callrequ)
            turn += 1
            callrequ = status
            table.showchips()

    else:
        if turn == 1:
            player2.receive_chips(table.chips)
            print("Player 2 wins")
            print(table.chips)
        elif turn == 0:
            player1.receive_chips(table.chips)
            print("Player 1 wins")
            print(table.chips)

def begin_hand(num_players):
    deck.shuffle()

    turn = 0
    blind = 5

    table.chips = 0
    player1.chips = 100
    player2.chips = 100
    player2.chips = 100
    
    player1.draw(deck,2)
    player2.draw(deck,2)
    player3.draw(deck,2)

    player3.place_bet(blind)
    callrequ = blind

    while callrequ > 0 or turn < num_players:
        if turn == 0:
            print("Player 1")
            status = player1.play(callrequ)
            turn += 1
            callrequ = status
            table.showchips()
        elif turn ==1:
            print("Player 2")
            status = player2.play(callrequ)
            turn += 1
            callrequ = status
            table.showchips()
        elif turn ==2:
            print("Player 3")
            status = player3.play(callrequ)
            turn += 1
            callrequ = status
            table.showchips()

    else:
        if turn == 1:
            player2.receive_chips(table.chips)
            print("Player 2 wins")
            print(table.chips)
        elif turn == 0:
            player1.receive_chips(table.chips)
            print("Player 1 wins")
            print(table.chips)

begin_hand(3)

    