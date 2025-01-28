    
# Turtle Race Game

A simple Python game where you predict which colored turtle will win a race to the finish line. Built using the `turtle` module.

## Features
- Predict the winning turtle's color before the race starts.
- Six colorful turtles race with randomized movement speeds.
- Instant feedback on whether your prediction was correct.
- Visual race animation with the `turtle` graphics library.

## Requirements
- Python 3.x
- `turtle` module (comes pre-installed with Python standard library)

## How to Play
1. Run the script in a Python environment.
2. A pop-up window will ask for your color prediction (options: red, orange, yellow, green, blue, purple).
3. Watch the turtles race across the screen!
4. The winner is declared when any turtle reaches the right edge of the screen.
5. You'll see a console message indicating if your prediction was correct.

## Game Rules
- Six turtles start at the left side of the screen with vertical spacing
- Each turtle moves forward by random distances (0-10 pixels) per turn
- First turtle to cross the 210px x-coordinate wins
- Race continues until there's a winner
- Valid color predictions: red, orange, yellow, green, blue, purple

## Code Structure
1. Initializes screen with 500x300 pixel dimensions
2. Creates six turtle objects with different colors
3. Sets up starting positions
4. Takes user prediction through a dialog box
5. Runs the race loop with random movements
6. Checks for winner and compares with user's prediction

## Example Output
```console
You've won! The blue turtle is the winner!
