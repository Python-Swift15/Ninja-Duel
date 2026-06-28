# Ninja Duel 🥷⚔️

A fullscreen 360° arena battle game built with Python Tkinter. Players control ninjas, aim in different directions, throw ninja stars, and battle either a friend or a computer opponent with different difficulty levels.

This project combines GUI development, animation, keyboard controls, mouse aiming, AI movement, collision detection, and game state management in Python.

## Features

- 🥷 Two-player ninja battle system
- 🎯 360° mouse aiming for Player 1
- ⭐ Throwing star projectile attacks
- ❤️ Lives system with heart icons
- 🤖 Computer opponent mode
- 🎮 Local friend battle mode
- 🔥 Easy, medium, and hard AI difficulty levels
- 🖥️ Fullscreen arena gameplay
- 🧱 Tiled background system
- 🏆 Win screen and main menu

## Requirements

- Python 3.x
- Tkinter
- Image assets in the required folder

## Installation

```bash
git clone https://github.com/your-username/Ninja-Duel.git
cd Ninja-Duel
```

## Usage

```bash
python3 main.py
```

## How to Play

1. Launch the game.
2. Choose a game mode from the main menu.
3. Move your ninja around the arena.
4. Aim with the mouse and throw stars at your opponent.
5. Reduce the opponent’s lives to zero to win.

## Controls

### Player 1

- **W** = Move up
- **A** = Move left
- **S** = Move down
- **D** = Move right
- **Mouse** = Aim
- **Left Click** = Throw star

### Player 2

- **Arrow Keys** = Move
- **Enter** = Throw star

### Menu

- **1** = VS Friend
- **2** = VS Computer Easy
- **3** = VS Computer Medium
- **4** = VS Computer Hard
- **M** = Return to menu after game over
- **Esc** = Quit

## Game Mechanics

- Each player starts with 3 lives.
- Stars travel in the direction they are aimed.
- Players can have up to 3 stars active before reloading.
- AI movement changes based on distance from Player 1.
- The game ends when one player loses all lives.

## Technical Details

- Built using `tkinter` for the game window and canvas
- Uses `PhotoImage` assets for ninjas, stars, hearts, and background tiles
- Uses `math.atan2()` for 360° aiming
- Uses `root.after()` for the main game loop
- Uses collision detection for projectile hits
- Uses keyboard and mouse event bindings for controls
- Supports fullscreen gameplay

## Future Enhancements

- Add sound effects and music
- Add more maps and arenas
- Add different ninja characters
- Add power-ups and special attacks
- Add score tracking
- Add pause menu
- Add smoother animations

## License

Open source - Feel free to take inspiration!