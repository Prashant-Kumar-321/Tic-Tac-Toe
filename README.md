# Tic-Tac-Toe Game

This is a simple classic Tic-Tac-Toe game built in Python. Two players can play against each other by taking turns to place their marks (X and O) on a 3x3 grid.

## Features
- Two-player mode (Human vs Human).
- Single Player mode (Human vs Computer).

## How to Play
1. Navigate to the project directory.
2. Run the Python script `python main.py`.
3. Enter the player names when prompted.
4. Players take turns to enter their moves by specifying the cell number(1-9) where they want to place their mark.  
5. The game continues until one player wins or the game ends in a draw.
6. To play again, simply restart the script.

## Requirements
- Python 3.x

## Installation
1. Clone the repository:
   ```
   git clone <repository_url>  
   ```

2. Navigate to the project directory:
   ```
   cd tic-tac-toe
   ```

3. Create a virtual environment (optional but recommended):
   ```
   Linux/Mac:
   python3 -m venv venv
   source venv/bin/activate 

   Windows:
   python -m venv venv
   venv\Scripts\activate
   ```

4. Run the game:
   ```
   python main.py
   ```  

## Run tests

Note: You should have `pytest` installed. You can install it using pip:
```pip install pytest```


To run the unit test for Tic-Tac-Toe game, use the following command from the project directory:
```
python -m pytest -q 
```

Run a single test file:
```
python -m pytest -q path/to/test/file.py -s
```

Run a particular test function from a test file: 
```
python -m pytest -q path/to/test/file.py::test_function_name -s

"-s" flag is used to see print statements in the test output.
```


## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests. 
For future improvements, consider adding
- Undo move feature.
- An AI opponent for single-player mode.
- A graphical user interface (GUI) for better user experience.
- Online multiplayer functionality.
- Score tracking and statistics.

# Minor Issues
1. Update render method in board.py to make it dynamic and should be able to handle different board sizes.


## License
This project is licensed under the MIT License.


## Author
[Prashant Kumar Gupta](https://github.com/Prashant-Kumar-321)

[LinkedIn](https://www.linkedin.com/in/prashantkumar222/)