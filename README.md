# Expense Tracker

A simple command-line expense tracker written in Python. Add, view, total, and delete expenses from a menu, with your data saved between runs.

## Features

- Add an expense with an amount, category, and description
- View all saved expenses in a numbered list
- Show the total amount spent
- Delete an expense by its number
- Input validation for amounts and menu choices
- Expenses are loaded on start and saved on exit

## Requirements

- Python 3.8 or newer (no external packages needed)

## Installation

1. Download and install [Visual Studio Code](https://code.visualstudio.com/).
2. Download and install [Python](https://www.python.org/downloads/). On Windows, check **Add Python to PATH** during setup.
3. On this GitHub page, click the green **Code** button, then **Download ZIP**.
4. Unzip the downloaded file.
5. Open VS Code, go to **File > Open Folder**, and select the unzipped folder.
6. Open `expense_tracker.py` and click the **Run** (play) button in the top right, or press `F5`.

## Usage

You can also run it from the VS Code terminal (**Terminal > New Terminal**):

```bash
python expense_tracker.py
```

You'll see this menu:

```
=== Expense Tracker ===
1. Add expense
2. View expenses
3. Show total
4. Delete expense
5. Quit
Enter your choice (1-5):
```

Type a number and follow the prompts. Choose **5** to save and quit.

## Project Structure

```
.
├── expense_tracker.py   # main program
└── README.md
```

## License

MIT
