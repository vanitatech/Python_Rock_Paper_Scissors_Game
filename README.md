# Rock Paper Scissors Game 🎮

A command-line Rock Paper Scissors game built with Python. The player competes against a computer opponent that randomly selects rock, paper, or scissors.

## Features

* 🎮 Play Rock Paper Scissors against the computer
* 🤖 Computer makes a random choice
* ✅ Validates the player's input
* 🔄 Accepts uppercase and lowercase input
* 🖼️ Displays Rock, Paper and Scissors using ASCII art
* 📐 Displays the player's and computer's choices side by side
* 🏆 Determines the winner or a draw
* ❌ Handles invalid user input

## Technologies Used

* Python 3
* Python `random` module
* Python `itertools.zip_longest`
* Git
* GitHub

## How It Works

The player is asked to choose:

```text
rock
paper
scissors
```

The program validates the input before continuing.

The computer then randomly selects one of the three choices using Python's `random.choice()` function.

The program compares both choices and determines whether the player:

* Wins
* Loses
* Draws

ASCII art is displayed for both choices.

## Example

```text
Welcome to the game of rock, paper and scissors.
Please type "rock", "paper" or "scissors": paper

You chose: paper               Computer chose: rock

     _______                     _______
---'    ____)____             ---'   ____)
           ______)                  (_____)
          _______)                  (_____)
         _______)                   (____)
---.__________)               ---.__(___)

Paper beats rock. You win!
```

## Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/vanitatech/Python_Rock_Paper_Scissors_Game.git
```

### 2. Navigate into the project

```bash
cd Python_Rock_Paper_Scissors_Game
```

### 3. Run the game

```bash
python task.py
```

On systems where `python` refers to Python 2, use:

```bash
python3 task.py
```

## What I Learned

This project helped me practise several fundamental Python concepts, including:

* Variables
* Lists
* Dictionaries
* `if`, `elif` and `else`
* `while` loops
* `for` loops
* User input
* Input validation
* Functions and methods
* Random selection
* String formatting
* f-strings
* `.lower()`
* `.strip()`
* `.splitlines()`
* `zip_longest()`

I also practised using Git and GitHub to manage and publish a Python project.

## Future Improvements

Potential future improvements include:

* Add a "Play Again" option
* Keep track of the player's score
* Keep track of the computer's score
* Add multiple rounds
* Add difficulty levels
* Improve the command-line interface
* Add automated tests

