
# Battleship Game Project

**Author: Yilin Huang <yhuan259@jhu.edu> Zhaoyang Min <zmin6@jhu.edu>**  
**Course: EN.540.635.01.FA24 Software Carpentry**

## Project Overview

The `Battleship.py` script is an implementation of the classic **Battleship Game**, providing a text-based gameplay experience. The script allows for flexible customization of the board size and ship configurations, and it includes core mechanics for placing ships, tracking attacks, and determining the outcome of the game. This project demonstrates clean, modular code design suitable for further extension into graphical or networked versions.

---

## How to Use

### Requirements

- Python 3.x or higher
- No additional libraries are required.  

### Running the Game

1. Open a terminal or command prompt.
2. Navigate to the directory containing the `Battleship.py` file.
3. Run the script with:
   ```bash
   python Battleship.py
   ```
4. Follow the on-screen instructions to play the game. Enter coordinates (e.g., "B3") when prompted to attack a cell.

### Example Gameplay

#### **Input Example**
```plaintext
Enter coordinates to attack (e.g., "A5"): B3
```

#### **Output Example**
```plaintext
Hit! Ship sunk!
Ships remaining: 3
```

#### **Gameplay Flow**
1. The board is initialized with hidden ships.
2. Players take turns attacking grid cells.
3. Feedback is provided for each attack:
   - **Hit**: The attack hits a ship.
   - **Miss**: The attack hits an empty cell.
   - **Sunk**: All parts of a ship have been hit.
4. The game ends when all ships are sunk.

---

## Code Architecture

### Class: `Board`

#### **Purpose**
The `Board` class is the foundational component of the game. It manages the grid layout, ship placement, attack handling, and the status of the game.

#### **Attributes**
- `size`: Integer indicating the board dimensions (default is 10x10).
- `grid`: A 2D list representing the state of each cell:
  - `'.'`: Empty cell
  - `'S'`: Ship
  - `'X'`: Hit
  - `'O'`: Miss
- `ships`: List of tuples, where each tuple represents a ship with the format `(row, col, length, orientation)`.
- `ships_remaining`: Integer tracking the number of ships that have not been completely sunk.

#### **Methods**
1. **`__init__(size=10)`**
   - Initializes an empty game board of size `size x size`.
   - Sets up attributes like `grid`, `ships`, and `ships_remaining`.

2. **`place_ship(row, col, length, orientation)`**
   - Places a ship on the board based on the provided parameters:
     - `row` and `col`: Starting position of the ship.
     - `length`: Length of the ship.
     - `orientation`: `'H'` for horizontal or `'V'` for vertical placement.
   - Validates the position to prevent overlapping or out-of-bound placement.

3. **`validate_position(row, col, length, orientation)`**
   - Checks if a ship can be placed at the specified location without violating game rules.

4. **`attack(row, col)`**
   - Processes an attack on the cell `(row, col)`:
     - Updates `grid` to `'X'` for a hit or `'O'` for a miss.
     - Tracks hits and updates `ships_remaining` if a ship is sunk.

5. **`is_game_over()`**
   - Returns `True` if all ships are sunk, signaling the end of the game.

6. **`print_board(show_ships=False)`**
   - Displays the current state of the board.
   - If `show_ships` is `True`, reveals ship locations for debugging purposes.

---

## Features

1. **Dynamic Board Size**  
   - The game board size is customizable, allowing for various gameplay scales.

2. **Ship Placement**  
   - Ships can be placed in horizontal (`'H'`) or vertical (`'V'`) orientation.
   - Automatic validation prevents invalid placement.

3. **Real-Time Feedback**  
   - Indicates hits, misses, and sunk ships during gameplay.

4. **Game Over Detection**  
   - Automatically checks if all ships are sunk.

5. **Text-Based Interface**  
   - Simple, terminal-based user interaction for accessibility and portability.

---

## How to Customize

### Board Size
To change the default board size, update the `Board` class constructor in the script:
```python
board = Board(size=15)  # Creates a 15x15 board
```

### Ship Configurations
Modify the `place_ship()` calls to add or change ships:
```python
board.place_ship(2, 3, 4, 'H')  # Places a horizontal ship of length 4 starting at (2, 3)
```

### Adding Features
1. **AI Opponent**:
   - Implement decision-making for placing ships and choosing attack coordinates.
2. **Graphical Interface**:
   - Use libraries like `tkinter` or `pygame` for a GUI.
3. **Multiplayer Mode**:
   - Enable two players to compete in a networked or local setting.

---

## How to Speed Up the Code

1. **Precompute Valid Positions**  
   - Cache possible ship placements for faster validation.

2. **Optimize Attack Handling**  
   - Use hash-based data structures to speed up grid lookups.

3. **Parallel Processing**  
   - Simulate multiple games or AI strategies concurrently.

---

## Example Workflow

1. **Initialization**:
   - The board is created, and ships are placed.
   - The user sees an empty grid.

2. **Gameplay Loop**:
   - Players attack by entering coordinates.
   - Feedback is provided for each attack.

3. **Game Over**:
   - The game ends when all ships are sunk.

---

## Troubleshooting

- **Invalid Input**:  
  Ensure coordinates are in the format `LetterNumber` (e.g., `B3`).  

- **Ship Placement Issues**:  
  Check for overlapping or out-of-bound placements during setup.  

- **Board Size Errors**:  
  Ensure the `size` attribute is a positive integer.

---

## Potential Enhancements

1. **Difficulty Levels**  
   - Add options for easy, medium, and hard gameplay.  

2. **Replayability**  
   - Save game results and provide a replay feature.  

3. **Thematic Variations**  
   - Customize ship types, board designs, or gameplay rules for unique experiences.

---

## Dependencies

- **Python >= 3.x**
- No external libraries required.  

---
