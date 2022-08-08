from collections import deque
from grid import Grid

class Grassfire:
  def __init__(self, matrix, plot_expansion = True):
    '''
    Initializes the Grassfire class.

    Parameters:
      matrix: The generated matrix to run the algorithm on.
      plot_expansion: If true, values of matrix indices will be updated to
                      represent cells that have been visited during the
                      algorithm's runtime.
    '''
    self.matrix = matrix
    self.plot_expansion = plot_expansion

  def _is_cell_valid(self, cell):
    '''
    Validates a cell by checking its boundaries in the matrix and whether it
    represents an obstacle (obstacles are not valid).

    Returns:
      True if the cell is valid; False otherwise.
    '''
    row, col = cell[0], cell[1]
    if row < 0 or row >= len(self.matrix) or \
       col < 0 or col >= len(self.matrix[row]):
      return False

    if self.matrix[row][col] == Grid.GRID_IND_OBSTACLE:
      return False
    return True

  def find_path(self, start_cell, dest_cell):
    '''
    Runs the algorithm and attempts to find a path from the starting cell to
    the destination cell.

    Parameters:
      start_cell: The row and column values of the starting cell.
      dest_cell: The row and column values of the destination cell.

    Returns:
      If a path is found, a list containing tuples of row and column values
      will be returned; otherwise, an empty list is returned.
    '''
    # N(-1,0), S(1,0), E(0,1), W(0,-1)
    dir_vertical, dir_horizontal = [-1, 1, 0, 0], [0, 0, 1, -1]
    possible_directions = 4

    queue = deque([(start_cell, [start_cell])])
    visited = [start_cell]

    while len(queue) > 0:
      path = queue.popleft()
      row, col = path[0]
      
      if (row, col) == dest_cell:
        # Destination reached
        return path[1]
      
      for i in range(possible_directions):
        cell = (dir_vertical[i] + row, dir_horizontal[i] + col)
        if not self._is_cell_valid(cell) or cell in visited:
          continue
        
        queue.append((cell, [*path[1], cell]))
        visited.append(cell)

        if self.plot_expansion and cell != dest_cell:
          self.matrix[cell[0]][cell[1]] = Grid.GRID_IND_EXPANSION
    return []