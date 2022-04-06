
'''
Deck of cards and players
'''

import random as r
import Card_dict as c


class Player:
    
    # Holds all player data and their hand
    
    def __init__(self, name, deck, hs_i):
        
        # hs_i = handsize initial. Ie, for blackjack/texas hold 'em: 2, for 5 card draw: 5
        
        self.hs_i = hs_i
        
        self.name = name
        self.hand = Hand()
        
        # Which deck this player is using to draw from
        
        self.playdeck = deck
        self.initial(self.hs_i)
    
    def add(self, card):
        
        # Adds a specific card to hand
        
        self.hand.addCard(card)
        
    def hit(self):
        
        # Adds random card to hand from deck
        
        self.playdeck.deal(self)
        
    def drop(self, cardout):
        
        # Removes a specific card from hand
        
        self.hand.remCard(cardout)
        
    def swapHit(self, cardout):
        
        # Removes a specific card and adds a random one from the deck
        
        self.drop(cardout)
        self.hit()
        
    def swapCard(self, cardin, cardout):
        
        # Removes a specific card and adds a specific card
        
        self.drop(cardout)
        self.add(cardin)
        
    def initial(self, size):
        
        # Sets up initial hand based on hs_i
        
        for i in range(size):
            self.hit()
        
    def newhand(self):
        
        # Creates a new hand from the deck
        
        self.hand.Clear()
        self.initial()
        
    def printHand(self):
        
        # Prints the current content of the hand
        
        self.hand.printHand()


class Card:
    
    # A class that contains data of a given card
    
    def __init__(self, val, suit):
        
        self.suit = suit            # Card's suit
        self.val = c.CardDict[val]  # Card's numeric value
        self.title = val + suit[0]  # Card's full title (shorthand)
        
    def AceSwitch(self):
        
        # Changes ace from high to low
        
        if(self.val == 11):
            self.val = 1
        elif(self.val == 1):
            self.val = 11
        
        
class Hand:
    
    def __init__(self):
        
        self.cards = []
        
    def addCard(self, card):
        
        # Adds a specific card to a hand
        
        self.cards.append(card)
        
    def remCard(self, card):
        
        # Removes a specific card from a hand
        
        self.cards.remove(card)
        
    def Clear(self):
        
        # Empties the hand
        
        self.cards = []
    
    def printHand(self):
        
        # Prints the hand in a scuffed but understandable format
        
        print('[', end = '')
        for i_card in self.cards:
            print(i_card.title, end = ", ")
        print(']')
    
    
class Deck:
    
    def __init__(self):
        
        self.cards = []
        self.reset()
        
    def deal(self, player):
        
        # Deals a specific player the topmost card on the deck
        
        card_out = self.cards[0]
        self.cards.pop(0)
        player.hand.addCard(card_out)
        
    def shuffleDeck(self):
        
        # Shuffles the deck using random's shuffle function
        
        r.shuffle(self.cards)
        
    def reset(self):
        
        # Sets the deck back to a filled and randomized state
        
        self.cards = []

        for m_suit in c.SuitList:
            for m_card in c.CardList:
                self.cards.append(Card(m_card, m_suit))
                
        self.shuffleDeck()
    
    def printDeck(self):
        
        # Prints the deck in a scuffed but understandable manner
        
        print('[', end = '')
        for i_card in self.cards:
            print(i_card.title, end = ", ")
        print(']')