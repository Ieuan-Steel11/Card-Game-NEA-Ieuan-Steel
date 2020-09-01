import deck_of_cards as deckoc
import player as pl
import pyfiglet as pg
import sys


deck = deckoc.Deck()  # creates new deck object
player1 = pl.Player(deck)  # creates player 1 object
player2 = pl.Player(deck)  # creates player 2 object


def playRound():
    deck.shuffle()
    # shuffles order of all cards
    print("Player 1 starts")

    player1_new_card = player1.deal()
    deckoc.createAsciiCard(player1_new_card)
    player1.cards_drawn += 1
    # deals card and prints it as ascii art

    print("Player two's go")

    player2_new_card = player2.deal()
    deckoc.createAsciiCard(player2_new_card)
    player2.cards_drawn += 1
    # deals card and prints it as ascii art

    winning_card = deckoc.decideWin(player1_new_card, player2_new_card)
    print("This card won: \n")
    deckoc.createAsciiCard(winning_card)
    # decides winning card with function and prints the winning card

    with open("results.txt", "a") as file:
        # opens text file in writing mode
        if winning_card == player1_new_card:
            # if player1 cards' one
            file.write(f"{player1_user}: {winning_card[1]} {winning_card[0]} won \n")
            # writes who won and with which card
            pg.figlet_format(f"{player1_user} wins this round")
            # writes in ascii art
            player1.hands_won += 1

        elif winning_card == player2_new_card:
            # if player2 cards' one
            file.write(f"{player2_user}: {winning_card[1]} {winning_card[0]} won \n")
            # writes who won and with which card
            pg.figlet_format(f"{player2_user} wins this round")
            # writes in ascii art
            player2.hands_won += 1


def endGame():
    player1.logout()
    player2.logout()
    # puts up logout prompt

    with open("results.txt", "w") as file:
        if player1.hands_won > player2.hands_won:
            # if player 1 won more hands than player 2
            file.write(f"{player1_user} won {player1.hands_won} hand(s) \n \n")
            # writes the amount of hands won

        elif player2.hands_won > player1.hands_won:
            # if player 1 won more hands than player 2
            file.write(f"{player2_user} won {player2.hands_won} hands \n \n")
            # writes the amount of hands won

    sys.exit()
    # quits python script

def startGame():
    global player1_user
    global player2_user
    # global variables, usernames
    welcome = pg.figlet_format("Welcome to The Game!")
    print(welcome)
    # prints ascii art of "Welcome to The Game!"
    player1_user = input("What do you want your leaderboard name to be player 1? \n")
    player2_user = input("What do you want your leaderboard name to be player 2? \n")
    # gets names for leaderboards
    player1.login()
    player2.login()
    # logs both players in
    if not player1.loggedIn and not player2.loggedIn:
        sys.exit()
        # if they aren't logged in quit

    # brings up login prompt for both player

def MainLoop():
    startGame()
    # logs in and prints welcome and gathers leaderboard names

    while True:
        playRound()
        # main game taking turns
        i = 0
        playAgain = input("Do you want to Quit or Play again (q/p)? \n")
        # input to decide whether to quit or not

        # Play Again Loop #

        while i < 7:
            # seven attempts to quit or play again otherwise it quits
            if playAgain:
                # if it isn't an empty string
                if playAgain.lower() == "q" or "p":
                    if playAgain == "q":
                        endGame()
                        # ends game
                    elif playAgain == "p":
                        break
                        # leaves play again loop to go to main game loop
                else:
                    print("ValueError: You can only enter p or q")
                    i += 1
                    continue
            else:
                # if it's an empty string resets
                continue
                i += 1


if __name__ == "__main__":
    # if this is the main file and not imported and called something else
    MainLoop()
    # runs game
