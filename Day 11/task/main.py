import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    """Returns a random card from the 'cards' list"""
    return random.choice(cards)

def refresh_screen():
    """Clears the screen and reprints the logo"""
    print("\n" * 20)
    print(art.logo)

def play_blackjack():
    """Main game loop"""
    player_hand = []
    computer_hand = []
    player_score = 0
    computer_score = 0

    refresh_screen()
    player_drawing = True
    player_hand.append(draw_card())
    player_hand.append(draw_card())

    computer_hand.append(draw_card())
    computer_hand.append(draw_card())

    while player_drawing:
        player_score = sum(player_hand)
        computer_score = sum(computer_hand)

        if computer_score == 21:
            # print("Computer has drawn 21, you lose!")
            player_drawing = False
        elif player_score == 21:
            # print("You have drawn 21, you win!")
            player_drawing = False

        if player_score > 21:
            if 11 in player_hand:
                player_hand[player_hand.index(11)] = 1
                player_score = sum(player_hand)
            if player_score > 21:
                # print("You have overdrawn, you lose!")
                player_drawing = False

        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        if player_drawing:
            draw_again = input("Type 'y' to get another card, type 'n' to pass: ")

            if draw_again == 'y':
                player_hand.append(draw_card())
            else:
                player_drawing = False

    computer_drawing = True
    while computer_drawing:
        if computer_score > 21:
            if 11 in computer_hand:
                computer_hand[computer_hand.index(11)] = 1
                computer_score = sum(computer_hand)

        if computer_score > 17 or player_score > 21 or computer_score > player_score:
            computer_drawing = False
        else:
            computer_hand.append(draw_card())
            computer_score = sum(computer_hand)

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

    if computer_score > 21:
        print("The computer has overdrawn, you win!")
    elif player_score > 21:
        print("You overdrew, the computer won!")
    elif player_score > computer_score:
        print("You drew higher, you win!")
    elif player_score == computer_score:
        print("It's a draw!")
    else:
        print("The computer won!")


playing = True
while playing:
    cont_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if cont_playing == 'y':
        play_blackjack()
    else:
        playing = False