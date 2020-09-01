from random import shuffle
from termcolor import cprint


def createAsciiCard(card):
    suit = ["Y", "B", "R"]
    colors = ["yellow", "grey", "red"]
    # create an empty list of list, each sublist is a line
    lines = [[] for i in range(9)]

    # "King" should be "K" and "10" should still be "10"
    if card[0] == 10:  # ten is the only one who's rank is 2 char long
        rank = card[0]
        space = ''  # if we write "10" on the card that line will be 1 char to long
    else:
        rank = card[0]  # some have a rank of 'King' this changes that to a simple 'K' ("King" doesn't fit)
        space = ' '  # no "10", we use a blank space to will the void
        # get the cards suit in two steps

    if card[1] == "yellow":
        j = 0
    elif card[1] == "black":
        j = 1
    elif card[1] == "red":
        j = 2

    # add the individual card on a line by line basis
    lines[0].append('┌─────────┐')
    lines[1].append('│{}{}       │'.format(rank, space))  # use two {} one for char, one for space or char
    lines[2].append('│         │')
    lines[3].append('│         │')
    lines[4].append('│    {}    │'.format(suit[j]))
    lines[5].append('│         │')
    lines[6].append('│         │')
    lines[7].append('│       {}{}│'.format(space, rank))
    lines[8].append('└─────────┘')

    result = []
    for index, line in enumerate(lines):
        result.append(''.join(lines[index]))
        # loops through each line and joins them to one string

    cprint('\n'.join(result), colors[j])


def decideWin(card1, card2):
    # function to decide who wins with every combination of colors and numbers

    if card1[1] == "red":

        if card2[1] == "black":
            return card1
        elif card2[1] == "yellow":
            return card2
        elif card2[1] == "red":
            # if same color use numbers to decide
            if int(card1[0]) > int(card2[0]):
                # turn them into ints as they're stored as numbers in a string
                return card1
            else:
                return card2

    elif card1[1] == "yellow":

        if card2[1] == "black":
            return card2
        elif card2[1] == "red":
            return card1
        elif card2[1] == "yellow":
            # if same color use numbers
            if int(card1[0]) > int(card2[0]):
                # turn them into ints so they can be compared
                return card1
            else:
                return card2

    elif card1[1] == "black":

        if card2[1] == "red":
            return card1
        elif card2[1] == "yellow":
            return card2
        elif card2[1] == "black":
            # if they're the same color
            if int(card1[0]) > int(card2[0]):
                # turn them to ints to be compared
                return card1
            else:
                return card2


class Deck:
    # creates a class for each card
    def __init__(self):
        self.allowed_colors = ["yellow", "red", "black"]
        self.allowed_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # allowed colors and values for making cards
        self.cards = []
        # where all the cards are going to be stored

        for color in self.allowed_colors:
            # loop through all colors
            for value in self.allowed_values:
                # loop through all values for each color
                self.cards.append([value, color])
                # creates the deck of cards as a 2D list

    def count(self):
        return len(self.cards)
        # returns amount of cards left

    def _deal(self, num):
        count = self.count()  # amount of cards in deck
        actual = min([count, num])
        # removes whichever value is lower the amount left in deck or amount wanted to be removed

        if count == 0:
            # if  no cards are left in deck
            raise ValueError("All cards have been dealt")

        dealtCards = self.cards[-actual:]
        # saves the removed cards to a variable called dealt_cards
        self.cards = self.cards[:-actual]
        # makes the deck lose the cards
        return dealtCards

    def dealCard(self):
        return Deck._deal(self, 1)[0]
        # uses _deal method to deal one card

    def shuffle(self):
        return shuffle(self.cards)
