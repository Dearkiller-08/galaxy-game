# 🚀 Galaxy Game

![Galaxy Game Preview](images/game-preview.png)

A stunning 3D perspective space runner game built with Python and Kivy. Navigate through an endless galaxy tunnel while avoiding obstacles in this visually captivating arcade-style game.

## ✨ Features

- **3D Perspective Graphics** - Immersive tunnel effect with perspective transformation
- **Smooth Gameplay** - 60 FPS fluid animations and responsive controls
- **Dynamic Obstacles** - Procedurally generated tile patterns
- **Cross-Platform** - Runs on Windows, macOS, and Linux

## 🛠️ Technologies

- **Python 3.x** - Core game logic
- **Kivy Framework** - GUI and graphics rendering
- **Custom 3D Transforms** - Mathematical perspective calculations

## 🎮 Controls

- **Desktop**: Arrow keys or A/D to steer left/right
- **Mobile**: Touch controls (tap left/right side of screen)

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/Dearkiller-08/galaxy-game.git
cd galaxy-game

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install kivy

# Run the game
python main.py
```

## 📂 Project Structure

```
galaxy/
├── main.py           # Game core and main loop
├── transforms.py     # 3D perspective mathematics
├── user_actions.py   # Input handling and controls
├── menu.py          # Menu system
├── galaxy.kv        # UI layout
├── fonts/           # Custom game fonts
└── images/          # Game assets and preview
```

## 🎯 Key Achievements

- Implemented custom 3D perspective transformation algorithms
- Created smooth procedural content generation
- Designed responsive cross-platform user interface
- Optimized performance for 60 FPS gameplay

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.
