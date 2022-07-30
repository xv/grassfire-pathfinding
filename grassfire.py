from collections import deque
from grid import Grid

class Grassfire:
  def __init__(self, grid):
    self.grid = grid

  def _is_cell_valid(self, cell):
    row, col = cell[0], cell[1]
    if row < 0 or row >= len(self.grid) or \
       col < 0 or col >= len(self.grid[row]):
      return False

    if self.grid[row][col] == Grid.GRID_IND_OBSTACLE:
      return False
    return True

  def _find_shortest_path(self, start, dest):
    # N(-1,0), S(1,0), E(0,1), W(0,-1)
    dir_vertical, dir_horizontal = [-1, 1, 0, 0], [0, 0, 1, -1]
    possible_directions = 4

    queue = deque([(start, [start])])
    visited = [start]

    while len(queue) > 0:
      path = queue.popleft()
      row, col = path[0]
      
      if (row, col) == dest:
        # Destination reached
        return path[1]
      
      for i in range(possible_directions):
        cell = (dir_vertical[i] + row, dir_horizontal[i] + col)
        if not self._is_cell_valid(cell) or cell in visited:
          continue
        
        queue.append((cell, [*path[1], cell]))
        visited.append(cell)
    return []

  def run(self, start, dest):
    return self._find_shortest_path(start, dest)
