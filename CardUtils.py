import random

class Card:
    suits = {
        0: "s",
        1: "c",
        2: "h",
        3: "d"
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f" {self.rank}{self.suits[self.suit]} "

class Deck:
    def __init__(self):
        self.cards = []
        self.discard = []
        self.build()

    def build(self):
        # black cards
        for rank in range(1, 14):
            self.cards.append(Card(rank, 0))
            self.cards.append(Card(rank, 1))

        # red cards
        for rank in range(1, 14):
            if rank > 10 or rank == 1:
                continue
            self.cards.append(Card(rank, 2))
            self.cards.append(Card(rank, 3))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

    def add_to_discard(self, card):
        self.discard.append(card)

    def cards_remaining(self):
        return len(self.cards)
