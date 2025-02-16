# Snake Game

A simple Snake Game implemented in Python using the `turtle` module. This project was developed as part of a Python course and demonstrates fundamental concepts of object-oriented programming (OOP), game logic, and user interaction.

## Features
- Classic snake movement and food consumption mechanics
- Collision detection with walls and the snake's own body
- Score tracking with a persistent high score stored in `data.txt`
- Simple controls using arrow keys to navigate the snake
- Start and restart functionality using the SPACE key

## How to Play
- Press `SPACE` to start the game.
- Use the `Arrow Keys` to move the snake:
  - `Up` → Move up
  - `Down` → Move down
  - `Left` → Move left
  - `Right` → Move right
- Eat the blue food to grow the snake and increase your score.
- Avoid crashing into the walls or yourself!
- If you crash, the game will display "GAME OVER" and you can restart by pressing `SPACE` again.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/rom4kov/snake_game.git
   cd snake_game
   ```
2. Ensure you have Python installed (recommended: Python 3.x).

3. I tested the game on Arch Linux, so if you're also running Arch, you'll need to install tkinter for the program to run:
   ```
   sudo pacman -S tkinter
   ```

3. Run the game:
   ```sh
   python main.py
   ```

## File Structure
- `main.py`: The main game loop, initializes the game and handles input.
- `snake.py`: Defines the `Snake` class and movement logic.
- `food.py`: Handles food spawning and random placement.
- `scoreboard.py`: Manages scorekeeping and high score persistence.
- `data.txt`: Stores the highest score achieved.

## Dependencies
This project uses Python's built-in `turtle` module and does not require external dependencies (except for tkinter on Arch Linux).


## Demo
![demo](https://github.com/user-attachments/assets/d9029155-2e8c-46fa-89ee-485a2f1b6475)


---

Enjoy the game and happy coding!

