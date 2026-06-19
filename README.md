# Hangman

A classic Hangman game built with Python and Pygame featuring interactive hangman drawing, keyboard input, and scoring.

## Features

- Interactive hangman drawing that progresses with each wrong guess
- Keyboard input for letter guessing
- Score tracking across rounds
- Multiple hangman state images for visual feedback
- Colorful Pygame-based UI

## Screenshots

![Game Screenshot 1](Image%201.png)
![Game Screenshot 2](Image%202.png)
![Game Screenshot 3](Image%203.png)
![Game Screenshot 4](Image%204.png)

## How to Play

1. The game selects a random word
2. Guess letters one at a time using the keyboard
3. Each correct guess reveals the letter in the word
4. Each wrong guess adds a part to the hangman drawing
5. Guess the word before the hangman is fully drawn to win!

## Installation

### Using Pipenv

```bash
pip install pipenv
pipenv install
pipenv run python Pygame2.py
```

### Using pip

```bash
pip install -r requirements.txt
python Pygame2.py
```

## Controls

- **Keyboard letters A-Z**: Guess a letter
- The game automatically handles input validation

## File Structure

```
Hangman/
├── Pygame2.py              # Main game script
├── Pipfile                 # Pipenv dependencies
├── Pipfile.lock            # Pipenv lock file
├── hangman0.png - hangman6.png  # Hangman state images
├── man.png                 # Man image
├── Image 1.png - Image 4.png    # Screenshots
└── README.md               # Project documentation
```

## Tech Stack

- **Python** - Core game logic
- **Pygame** - Graphics and input handling

## License

MIT License - see the [LICENSE](LICENSE) file for details.
