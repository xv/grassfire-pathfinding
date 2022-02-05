Dependencies
------------
This program requires the libraries `numpy` and `pygame` to be installed. You may install these libraries using `pip` as follows:
```
$ pip install numpy
$ pip install pygame
```
Alternatively, consult the installation web pages for [numpy](https://numpy.org/install/) and [pygame](https://www.pygame.org/wiki/GettingStarted) for other installation options.

Run
---
Simply run `main.py` in a terminal to start the program and provide parameters via input. You may alternatively modify the source code file to comment out the line that invokes `Grid.init_from_user_input()` and manually construct the `Grid` class parameters as you see fit.

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
The generated matrix is passed down to the Pygame module `grid_gui` and the GUI is automatically built based on the received information. Below is an example of the GUI.

![gui](/images/gui_01.png)

Pygame GUI Color Legend:
* ![#ff0000](https://via.placeholder.com/15/ff0000/000000?text=+) Starting cell
* ![#00ff00](https://via.placeholder.com/15/00ff00/000000?text=+) Destination cell
* ![#505050](https://via.placeholder.com/15/505050/000000?text=+) Obstacle
* ![#c0c0c0](https://via.placeholder.com/15/c0c0c0/000000?text=+) Path from the starting cell to destination cell

Legal
-----
This project is distributed under the terms of the [MIT License](LICENSE).
