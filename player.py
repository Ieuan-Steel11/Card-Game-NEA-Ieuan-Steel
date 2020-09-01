import security as sec


class Player:
    # class for players

    def __init__(self, deck):
        self.hands_won = 0
        # to count how many times player has won
        self.cards_drawn = 0
        # counts how many cards are drawn for the round
        self.deck = deck
        # to pass in deck so it can be used in class methods
        self.loggedIn = False
        # to check if they are logged in

    def deal(self):
        card = self.deck.dealCard()
        # deals new card
        return card

    def login(self):
        self.start = sec.Start()
        # creates start object
        self.start.startWindow()
        # runs main window
        if self.start.loggedIn:
            self.loggedIn = True
            # returns true to be able to test if someone's logged in Main.py

    @classmethod  # classmethod decorator so its treats as a method not a function
    def logout(cls):
        sec.logout()
        # opens logout window
