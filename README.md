# Car Racing Game - Pygame Implementation

## Overview
This repository contains a simple **Car Racing Game** built using Python and the **Pygame** library. The player controls a car that navigates through an endless road while avoiding obstacles and collecting items to earn points. The game increases in challenge as the player progresses, with smoother gameplay and a user-friendly interface.

## Features
- **Smooth gameplay** with responsive controls.
- **Obstacles** that must be avoided to survive.
- **Items** that can be collected to increase the score.
- Simple and visually appealing **user interface**.
- Game Over screen with options to restart or quit.

---

## Prerequisites
Ensure you have the following installed on your system:
- **Python 3.10 or higher**
- **Pygame 2.5.1** or later

To install Pygame, use:
```bash
pip install pygame
```

---

## How to Run the Game
1. Clone the repository:
   ```bash
   git clone https://github.com/83Gh0st/car_sim_terminal.git
   ```
2. Navigate to the project directory:
   ```bash
   cd car_sim_terminal
   ```
3. Run the game:
   ```bash
   python3 car.py
   ```

---

## Gameplay Instructions
1. **Start the Game**:
   - Run the game using the above command.

2. **Controls**:
   - Use the **Left Arrow Key** to move the car left.
   - Use the **Right Arrow Key** to move the car right.

3. **Objective**:
   - Avoid red obstacles.
   - Collect yellow items to increase your score.

4. **Game Over**:
   - If the car collides with an obstacle, the game ends.
   - Restart by pressing **R**.
   - Quit by pressing **Q**.

---

## Code Overview
The code is divided into logical sections for better readability and maintainability:

### Constants
Defined variables for screen dimensions, colors, car size, and speeds:
```python
WIDTH = 400
HEIGHT = 600
CAR_WIDTH = 30
CAR_HEIGHT = 40
FPS = 60
CAR_SPEED = 10
OBSTACLE_SPEED = 3
ITEM_SPEED = 3
```

### Colors
Used RGB values to define colors:
```python
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHT_GRAY = (211, 211, 211)
```

### Functions
1. **`draw_car(x, y)`**:
   - Draws the player-controlled car at the specified coordinates.

2. **`draw_obstacles(obstacles)`**:
   - Draws red rectangular obstacles.

3. **`draw_items(items)`**:
   - Draws yellow collectible items.

4. **`draw_score(score)`**:
   - Displays the current score at the top-left corner of the screen.

5. **`draw_game_over()`**:
   - Displays the "Game Over" message and instructions to restart or quit.

6. **`update_obstacles()`**:
   - Updates obstacle positions and handles collisions with the car.

7. **`update_items()`**:
   - Updates item positions and handles item collection.

8. **`handle_input()`**:
   - Handles keyboard input for car movement.

9. **`main()`**:
   - The main game loop that:
     - Handles events.
     - Updates game objects (obstacles, items, etc.).
     - Draws all game elements on the screen.
     - Detects game over conditions.

---

## File Structure
```
car-racing-game/
├── car.py          # Main game logic
├── README.md       # Documentation (this file)
```

---

## Adjusting Difficulty
To make the game easier or harder, modify the following constants in `car.py`:
- **`OBSTACLE_SPEED`**: Increase for faster obstacles, decrease for slower obstacles.
- **`ITEM_SPEED`**: Adjust the speed at which items fall.
- **`random.randint()`** in the `main()` function:
  - Reduce the range for more frequent obstacles.
  - Increase the range for less frequent obstacles.

Example:
```python
# Adjust obstacle frequency
if random.randint(0, 15) < 3:
    obstacle_x = random.randint(0, WIDTH - CAR_WIDTH)
    obstacles.append(pygame.Rect(obstacle_x, 0, CAR_WIDTH, CAR_HEIGHT))

# Adjust item frequency
if random.randint(0, 15) == 0:
    item_x = random.randint(0, WIDTH - 20)
    items.append([item_x, 0])
```

---

## Future Improvements
Potential enhancements include:
- Adding levels with increasing difficulty.
- Introducing power-ups for temporary speed boosts or shields.
- Implementing a pause menu.
- Adding sound effects and background music.

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch-name
   ```
5. Open a Pull Request.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments
- Built with [Pygame](https://www.pygame.org/).
- Inspired by classic arcade-style racing games.

