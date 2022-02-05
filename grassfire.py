from collections import deque
from grid import Grid
from numpy import ndarray

class Grassfire:
  def __init__(self, grid: ndarray):
    self.grid = grid

  def _find_shortest_path(self, grid, start, dest):
    # N(-1,0), S(1,0), E(0,1), W(0,-1)
    dir_vertical, dir_horizontal = [-1, 1, 0, 0], [0, 0, 1, -1]
    possible_directions = 4

    path = []
    history = []
    queue = deque([(start, [start])])

    while len(queue) > 0:
      node = queue.popleft()
      row, col = node[0]
      
      if (row, col) == dest:
        # Destination reached
        path = node[1]
        break
      
      # Record historical nodes/cells so they don't get explored again
      history.append((row, col))
      
      for i in range(possible_directions):
        current_row = dir_vertical[i] + row
        current_col = dir_horizontal[i] + col
        current_cell = (current_row, current_col)
        
        if current_row < 0 or current_col < 0:
          continue
        
        if current_row >= len(grid) or \
           current_col >= len(grid[current_row]):
          continue
        
        if grid[current_row][current_col] == Grid.GRID_IND_OBSTACLE:
         continue
        
        if current_cell in history:
          continue
        
        queue.append((current_cell, [*node[1], current_cell]))
      
    return path

  def run(self, start, dest):
    return self._find_shortest_path(self.grid, start, dest)
