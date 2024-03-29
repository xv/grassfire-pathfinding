import prompts
import numpy

class Grid:
  # Indicators
  GRID_IND_DEFAULT = 0
  GRID_IND_OBSTACLE = -1
  GRID_IND_STARTING_CELL = 1
  GRID_IND_DESTINATION_CELL = 2
  GRID_IND_EXPANSION = 3
  GRID_IND_PATH = 4

  def __init__(self, rows, columns, obstacle_percentage, 
               start_cell, dest_cell):
    '''
    Initializes the Grid class.

    Parameters:
      rows: The number of rows.
      columns: The number of columns.
      obstacle_percentage: Percentage of obstacles.
      start_cell: Tuple of row and column values representing the starting cell.
      dest_cell: Tuple of row and column values representing the destination cell.
    '''
    self.rows = rows
    self.columns = columns
    self.obstacle_percentage = obstacle_percentage
    self.start_cell = start_cell
    self.dest_cell = dest_cell

  @classmethod
  def init_from_user_input(cls):
    '''
    Constructs the Grid class from user input.
    '''
    rows = prompts.get_ranged_int("Rows: ", 8)
    columns = prompts.get_ranged_int("Columns: ", 8)
    obstacles = prompts.get_ranged_int("Obstacles (%): ", 10, 50)
    start_cell = prompts.get_matrix_coords(
      "Starting cell (ROW, COL): ",
      0, rows - 1, 0, columns - 1
    )
    
    dest_cell = prompts.get_matrix_coords(
      "Destination cell (ROW, COL): ",
      0, rows - 1, 0, columns - 1
    )
    
    return cls(
      rows, columns, obstacles,
      start_cell, dest_cell
    )

  def _fill_obstacles(self, matrix):
    '''
    Adds obstacle cells.

    Parameters:
      matrix: The generated matrix to plot obstacles on.
    '''
    obstacles = numpy.random.ranf((self.rows, self.columns))
    percentage = self.obstacle_percentage / 100
    matrix[(obstacles <= percentage)] = self.GRID_IND_OBSTACLE

  def _set_starting_cell(self, matrix, cell):
    '''
    Sets the starting cell.

    Parameters:
      matrix: The generated matrix to plot the starting cell on.
    '''
    row, col = cell[0], cell[1]
    matrix[row][col] = self.GRID_IND_STARTING_CELL

  def _set_destination_cell(self, matrix, cell):
    '''
    Sets the destination cell.

    Parameters:
      matrix: The generated matrix to plot the destination cell on.
    '''
    row, col = cell[0], cell[1]
    matrix[row][col] = self.GRID_IND_DESTINATION_CELL

  def generate_matrix(self):
    '''
    Generates a matrix based on the parameters provided in the constructor.
    '''
    matrix = numpy.full((self.rows, self.columns), self.GRID_IND_DEFAULT)
    self._fill_obstacles(matrix)
    self._set_starting_cell(matrix, self.start_cell)
    self._set_destination_cell(matrix, self.dest_cell)
    return matrix

  def plot_path(self, matrix, path):
    '''
    Plots the path in the matrix by updating values of indices associated
    with the path.

    Parameters:
      matrix: The generated matrix to plot the path on.
      path: list of tuples of rows and columns of coordinates from the
            starting cell to the destination cell.
    '''
    for coord in path[1:-1]: # Skip start and dest cells
      row, col = coord[0], coord[1]
      matrix[row][col] = Grid.GRID_IND_PATH

  def print_grid_description(self):
    '''
    Prints a description of the generated matrix.
    '''
    print("Generated a grid of size {}x{} and an obstacle percentage of {}% "
          "with a starting\ncell at {} and a destination cell at {}"
          .format(self.rows, self.columns, self.obstacle_percentage,
                  self.start_cell, self.dest_cell))