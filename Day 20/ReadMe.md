# Snake Game 🐍

A classic Snake game implemented using Python's Turtle module. Guide the snake to eat food, grow longer, and avoid collisions with walls and yourself. High scores are saved between sessions!

## Features ✨
- **Score Tracking**: Earn points by eating food.
- **High Score System**: Persistent high score saved in `data.txt`.
- **Collision Detection**: Walls and self-collisions reset the game.
- **Smooth Controls**: Responsive arrow key movements.
- **Dynamic Food Spawning**: Food appears randomly on the screen.

## Requirements 🛠️
- Python 3.x
- `turtle` module (included in the standard library)

## How to Run 🚀
1. Ensure all files (`data.txt`, `food.py`, `main.py`, `scoredboard.py`, `snake.py`) are in the same directory.
2. Run the game:
   ```bash
   python main.py
   ```

## Controls 🎮
- **Up Arrow**: Move upward
- **Down Arrow**: Move downward
- **Left Arrow**: Move left
- **Right Arrow**: Move right

## File Overview 📁
- `data.txt`: Stores the high score.
- `food.py`: Handles food creation and random spawning.
- `main.py`: Main game loop, screen setup, and collision logic.
- `scoredboard.py`: Manages score display, updates high score, and game-over messages.
- `snake.py`: Defines the snake's movement, growth, and reset behavior.

## Notes 📝
- The high score is automatically updated in `data.txt` if beaten.
- The game resets on wall or self-collision but preserves the high score.
- The snake speeds up slightly as it grows longer (fixed movement interval).
