import prompts
import numpy

class Grid:
  # Indicators
  GRID_IND_DEFAULT = 0
  GRID_IND_OBSTACLE = -1
  GRID_IND_STARTING_CELL = 1
  GRID_IND_DESTINATION_CELL = 2
  GRID_IND_PATH = 3
  GRID_IND_EXPANSION = 4

  def __init__(self, rows, columns, obstacle_percentage, 
               start_cell, dest_cell): 
    self.rows = rows
    self.columns = columns
    self.obstacle_percentage = obstacle_percentage
    self.start_cell = start_cell
    self.dest_cell = dest_cell

  @classmethod
  def init_from_user_input(cls):
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
          "with a starting\ncell at {} and a destination cell at {}"
          .format(self.rows, self.columns, self.obstacle_percentage,
                  self.start_cell, self.dest_cell))