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
Simply run `main.py` in a terminal to start the program and provide parameters via input as prompted.

The terminal outputs a matrix like:
```
[[ 0 -1  0  0 -1  0 -1  0]
 [ 0  1  3  0  0  0  0  0]
 [-1 -1  3 -1  0  0 -1  0]
 [ 0 -1  3  3  0  0  0 -1]
 [ 0  0 -1  3 -1  0  0  0]
 [-1  0  0  3  3  3  0  0]
 [ 0 -1  0 -1 -1  2  0  0]
 [ 0  0  0 -1  0  0  0  0]]
 ```
Where the numbers in the matrix are represented as:
* Obstacle (-1)
* Default fill (0)
* Starting cell (1)
* Destination cell (2)
* Path from the starting cell to destination cell (3)
 
### Pygame GUI
The generated matrix is passed down to the Pygame module `grid_gui` and the GUI is automatically built based on the received information. Below is an image of the GUI that is generated from the matrix output above.

![grid](/images/grid.png)

Pygame GUI Color Legend:
* ![#ff0000](https://via.placeholder.com/15/ff0000/ff0000.png) Starting cell
* ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00.png) Destination cell
* ![#505050](https://via.placeholder.com/15/505050/505050.png) Obstacle
* ![#c0c0c0](https://via.placeholder.com/15/c0c0c0/c0c0c0.png) Path from the starting cell to destination cell

### Customization
* You can modify `main.py` to comment out the line that invokes `Grid.init_from_user_input()` and manually construct the parameters of the `Grid` class if you wish to run a pre-set grid without having to input parameters into the terminal every time the program is run.
    * Example: `grid = Grid(8, 8, 20, (1, 1), (6, 5))`<br>The above will create a matrix of 8 rows and 8 columns, an obstacle concentration of 20%, a starting cell at the 2nd row and 2nd column, and a destination cell at the 7th row and 6th column.

* You can modify `main.py` to enable the plotting of cells the algorithm had visited while searching for the destination cell. This can be done by setting the boolean `plot_expansion` parameter of the `Grassfire` class constructor. If this option is enabled, the value of the matrix element that corresponds to the visited cell will be set to `4` instead of the default `0`.

Legal
-----
This project is distributed under the terms of the [MIT License](LICENSE).
