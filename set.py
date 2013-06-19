__author__ = 'Dan'

from random import randint


numbers = [1, 2, 3]
colors = ["green", "red", "purple"]
textures = ["solid", "shaded", "empty"]
shapes = ["oval", "diamond", "squiggle"]


class Card:
    def __init__(self, number, color, texture, shape):
        self.number = number
        self.color = color
        self.texture = texture
        self.shape = shape


def is_set(card1, card2, card3):
    isset = True
    if card1.number == card2.number and card1.number != card3.number:
        isset = False
    if card1.number != card2.number and card1.number == card3.number:
        isset = False
    if card1.color == card2.color and card1.color != card3.color:
        isset = False
    if card1.color != card2.color and card1.color == card3.color:
        isset = False
    if card1.texture == card2.texture and card1.texture != card3.texture:
        isset = False
    if card1.texture != card2.texture and card1.texture == card3.texture:
        isset = False
    if card1.shape == card2.shape and card1.shape != card3.shape:
        isset = False
    if card1.shape != card2.shape and card1.shape == card3.shape:
        isset = False
    return isset


def make_deck():
    deck = []
    for number in numbers:
        for color in colors:
            for texture in textures:
                for shape in shapes:
                    deck.append(Card(number, color, texture, shape))
    return deck


def shuffle_deck(deck):
    shuffled = []
    while len(deck) > 0:
        shuffled.append(deck.pop(randint(0,len(deck)-1)))
    return shuffled


def pretty_card(card):
    shape = card.shape
    if card.number == 2 or card.number == 3:
        shape += "s"
    return "%s %s %s %s" % (card.number, card.color, card.texture, shape)


def print_full_deck():
    deck = make_deck()
    for card in deck:
        print pretty_card(card)


def all_sets_on_table(table):
    """
    Prints a list of every set on a table
    Params:
    table: list of Cards
    Returns: List of sets of three cards that form a set. False if there are no sets
    """
    sets = []
    for card1 in table:
        for card2 in table[table.index(card1)+1:]:
            for card3 in table[table.index(card2)+1:]:
                if is_set(card1, card2, card3):
                    print is_set(card1,card2,card3)
                    print [pretty_card(card1), pretty_card(card2), pretty_card(card3)]
                    sets.append([card1, card2, card3])
    if not sets:
        return False
    else:
        prettysets = []
        for _set in sets:
            prettyset = []
            for card in _set:
                prettyset.append(pretty_card(card))
            prettysets.append(prettyset)
        return prettysets


def table_compare(table, card):
    """
    Compares a card object (Card) with a table of cards (list) to check for sets.
    Params:
    table: list of Cards
    card: Card object
    Returns: True if the card makes a set with any two cards in the table, False otherwise
    """
    sets = False
    for card1 in table[:-1]:
        for card2 in table[table.index(card1)+1:]:
            if is_set(card, card1, card2):
                sets = True
    return sets


def probability_set(num_tries=100):
    sets = 0.0
    for x in xrange(num_tries):
        mydeck = make_deck()
        card1 = mydeck.pop(randint(0,len(mydeck)-1))
        card2 = mydeck.pop(randint(0,len(mydeck)-1))
        card3 = mydeck.pop(randint(0,len(mydeck)-1))
        if is_set(card1, card2, card3):
            sets += 1
    return sets/num_tries


def max_group_no_sets():
    deck = shuffle_deck(make_deck())
    table = [deck.pop(), deck.pop()]
    while len(deck) > 0:
        card = deck.pop()
        if not table_compare(table, card):
            table.append(card)
    return table


def max_group_possibilities(num_loops=1000):
    maxes = {}
    for x in xrange(num_loops):
        max = len(max_group_no_sets())
        if max in maxes:
            maxes[max] += 1
        else:
            maxes[max] = 1
    return maxes


mydeck = shuffle_deck(make_deck())
mytable = []
for x in xrange(10):
    mytable.append(mydeck[x])
for card in mytable:
    print pretty_card(card)
print all_sets_on_table(mytable)
print type(all_sets_on_table(mytable))









