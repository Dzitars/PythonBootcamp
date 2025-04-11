import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rpc = [rock,paper,scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

if player_choice >= 0 and player_choice <= 2:
    print(f"{rpc[player_choice]}\nComputer chose: \n{rpc[computer_choice]}")

if player_choice > 2 or player_choice < 0:
    print("You typed an invalid number. You Lose!")
elif player_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and player_choice == 2:
    print("You Lose!")
elif computer_choice > player_choice:
    print("You Lose!")
elif computer_choice < player_choice:
    print("You Win!")
elif computer_choice == player_choice:
    print("It's a Draw!")

