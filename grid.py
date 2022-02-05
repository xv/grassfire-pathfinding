from decimal import Decimal, ROUND_HALF_UP
from math import ceil
import prompts
import numpy

class Grid:
  # Indicators
  GRID_IND_DEFAULT = 0
  GRID_IND_OBSTACLE = -1
  GRID_IND_STARTING_CELL = 1
  GRID_IND_DESTINATION_CELL = 2
  GRID_IND_PATH = 3

  def __init__(self, rows: int, columns: int, obstacle_percentage: int, 
               start_cell: tuple, dest_cell: tuple): 
    self.rows = rows
    self.columns = columns
    self.obstacle_percentage = obstacle_percentage
    self.start_cell = (start_cell[0] - 1, start_cell[1] - 1)
    self.dest_cell = (dest_cell[0] - 1, dest_cell[1] - 1)

  @classmethod
  def init_from_user_input(cls):
    rows = prompts.get_ranged_int("Rows: ", 8)
    columns = prompts.get_ranged_int("Columns: ", 8)
    obstacles = prompts.get_ranged_int("Obstacles (%): ", 10, 20)
    start_cell = prompts.get_matrix_coords(
      "Starting cell (ROW, COL): ",
      1, 1, 1, columns
    )
    
    # Greater than half the number of rows
    dest_row_min = ceil(rows / 2) + 1 
    # Greater than 2/3 of the number of columns
    dest_col_min = Decimal((2 / 3) * columns).quantize(0, ROUND_HALF_UP) + 1
    dest_cell = prompts.get_matrix_coords(
      "Destination cell (ROW, COL): ",
      dest_row_min, rows, dest_col_min, columns
    )
    
    return cls(
      rows, columns, obstacles,
      start_cell, dest_cell
    )

  def _fill_obstacles(self, grid):
    obstacles = numpy.random.ranf((self.rows, self.columns))
    percentage = self.obstacle_percentage / 100
    grid[(obstacles <= percentage)] = self.GRID_IND_OBSTACLE

  def _set_starting_cell(self, grid, cell):
    row, col = cell[0], cell[1]
    grid[row][col] = self.GRID_IND_STARTING_CELL

  def _set_destination_cell(self, grid, cell):
    row, col = cell[0], cell[1]
    grid[row][col] = self.GRID_IND_DESTINATION_CELL

  def generate_grid(self):
    grid = numpy.full((self.rows, self.columns), self.GRID_IND_DEFAULT)
    self._fill_obstacles(grid)
    self._set_starting_cell(grid, self.start_cell)
    self._set_destination_cell(grid, self.dest_cell)
    return grid

  def plot_path(self, grid, path):
    for coord in path[1:-1]: # Skip start and dest cells
      row, col = coord[0], coord[1]
      grid[row][col] = Grid.GRID_IND_PATH

  def print_grid_description(self):
    print("Generated a grid of size {}x{} and an obstacle percentage of {}% "
          "with a starting cell at {} and a destination cell at {}"
          .format(self.rows, self.columns, self.obstacle_percentage,
                  (self.start_cell[0] + 1, self.start_cell[1] + 1), 
                  (self.dest_cell[0] + 1, self.dest_cell[1] + 1)))