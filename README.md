Dependencies
------------
This program requires the packages `numpy` and `pygame` to be installed. You may install these packages with `pip` in a Python 3 virtual environment (venv) by entering the commands below from within the project's directory.

#### Windows (Command Prompt):
```
> python -m venv grassfire_env
> grassfire_env\Scripts\activate.bat
> pip install -r requirements.txt
```

#### POSIX (Bash):
On Linux, you may need to install `python3-venv` beforehand.
```
$ python3 -m venv grassfire_env
$ source grassfire_env/bin/activate
$ pip install -r requirements.txt
```

Run
---
Simply run `main.py` in a terminal to start the program and provide parameters via input as prompted. You may alternatively modify the source code file to comment out the line that invokes `Grid.init_from_user_input()` and manually construct the `Grid` class parameters as you see fit.

The terminal outputs a matrix like:
```
[[ 0  1  0 -1 -1  0  0  0]
 [ 0  3  3 -1  0  0  0  0]
 [-1 -1  3  3  3  3 -1  0]
 [ 0  0 -1  0 -1  3  0  0]
 [-1  0  0 -1  0  3  0  0]
 [-1 -1  0 -1  2  3 -1  0]
 [ 0  0  0  0  0  0  0  0]
 [ 0  0  0  0 -1  0  0  0]]
 ```
Where the numbers in the matrix are represented as:
* Obstacle (-1)
* Default fill (0)
* Starting cell (1)
* Destination cell (2)
* Path from the starting cell to destination cell (3)
 
### Pygame GUI
The generated matrix is passed down to the Pygame module `grid_gui` and the GUI is automatically built based on the received information. Below is an image of the GUI that is generated from the matrix output above.

![gui](/images/gui_01.png)

Pygame GUI Color Legend:
* ![#ff0000](https://via.placeholder.com/15/ff0000/ff0000.png) Starting cell
* ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00.png) Destination cell
* ![#505050](https://via.placeholder.com/15/505050/505050.png) Obstacle
* ![#c0c0c0](https://via.placeholder.com/15/c0c0c0/c0c0c0.png) Path from the starting cell to destination cell

Legal
-----
This project is distributed under the terms of the [MIT License](LICENSE).
