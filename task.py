import random
from itertools import zip_longest

# Rock Paper Scissors ASCII Art

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choices = ["rock", "paper", "scissors"]

while True:
    person = input('Welcome to the game of rock, paper and scissors. Please type "rock", "paper" or "scissors": ').lower()

    if person in choices:
        break
    else:
        print("Invalid choice. Please type rock, paper or scissors.")

computer = random.choice(choices)

images = {"rock": rock, "paper": paper, "scissors": scissors}

print(f"{'You chose: ' + person:<30}{'Computer chose: ' + computer} ")
user_image = images[person].strip().splitlines()
computer_image = images[computer].strip().splitlines()
for user_line, computer_line in zip_longest(user_image, computer_image, fillvalue=""):
    print(f"{user_line:<30} {computer_line}")

if person == computer:
    print('It\'s a tie!')


elif person == "rock" and computer == "scissors":
    print('(rock beats scissors. You win!)')


elif person == "scissors" and computer == "paper":
    print ('Scissors can cut paper. You win!')


elif person == "paper" and computer == "rock":
    print('Paper beats rock. You Win!')

else:
    print('You lose! ')





