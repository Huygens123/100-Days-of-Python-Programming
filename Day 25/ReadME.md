# U.S. States Game

It is a fun and educational game that tests your knowledge of the geography of the United States. This Python project presents users with a blank map of the United States and challenges them to name all 50 states.

## Features

- Interactive U.S. map interface
- Real-time feedback as you correctly identify states
- State names appear on the map in their correct locations
- Tracks your score as you play
- Limited chances for incorrect guesses
- Option to exit the game and save unguessed states for future learning

## Requirements

- Python 3.x
- Turtle graphics library (included in standard Python)
- Pandas library
- A CSV file named `50_states.csv` containing state names and coordinates
- An image file named `blank_states_img.gif` (blank U.S. map)

## Installation

1. Ensure Python 3.x is installed on your system
2. Install the required Pandas library:
   ```
   pip install pandas
   ```
3. Place the `50_states.csv` file in the same directory as the script
4. Place the `blank_states_img.gif` file in the same directory as the script

## How to Play

1. Run the script:
   ```
   python us_states_game.py
   ```
2. A window will appear with a blank map of the United States
3. Enter the name of a U.S. state when prompted
4. If correct, the state name will appear on the map at its proper location
5. If incorrect, you'll lose one of your 5 chances
6. Continue guessing states until you've named all 50 or run out of chances
7. Type "Exit" at any time to quit the game

## Game Controls

- Type a state name in the input box and press Enter
- Type "Exit" to quit the game

## Learning Mode

If you exit the game before completing all 50 states, the program will create a CSV file named `states_to_learn.csv` containing all the states you missed. This feature helps you focus on the states you still need to learn.
