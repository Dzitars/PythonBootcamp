from game_data import data
import art
import random

def clear_screen():
    print("\n" * 20)

def get_description(entry):
    return f"{entry['name']}, a {entry['description']} from {entry['country']}"

def game():
    still_playing = True
    score = 0

    while still_playing:
        print(art.logo)

        if score > 0:
            print(f"You're right! Current score: {score}.")

        round_data = {
            "A" : random.choice(data),
            "B" : random.choice(data)
        }

        if round_data["A"]["follower_count"] > round_data["B"]["follower_count"]:
            highest = "A"
        else:
            highest = "B"

        print("Compare A: " + get_description(round_data["A"]))
        print(art.vs)
        print("Against B: " + get_description(round_data["B"]))
        # print(highest) # for testing

        player_choice = str.upper(input("Who has more followers? Type 'A' or 'B': "))

        if player_choice == highest:
            score += 1
            clear_screen()
        else:
            still_playing = False

    clear_screen()
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}")

game()