from grid import Grid
from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_DARK_GREY = (80, 80, 80)
COLOR_GREY = (192, 192, 192)

class Cell:
  def __init__(self, rect, color):
    '''
    Initializes the Cell class.

    Parameters:
      rect: Rectangle of the grid cell.
      color: An RGB value to associate with the grid cell.
    '''
    self.rect = rect
    self.color = color

  def __str__(self):
    return f"({self.rect}, {self.color})"

class GridPlot():
  def __init__(self, rows, columns, block_size):
    '''
    Initializes the GridPlot class.

    Parameters:
      rows: Number of rows in the grid.
      columns: Number of columns in the grid.
      block_size: The size of the grid cell. This value cannot be less than
                  either the number of rows or number of columns.
    '''
    pygame.init()
    pygame.display.set_caption("Grid Plot")

    self.rows = rows
    self.columns = columns
    self.block_size = block_size

    self.cell_rects = []
    self.generated_matrix = []

    self._set_window_size()
    self.clock = pygame.time.Clock()

  def _set_window_size(self):
    '''
    Automatically sets the window size according the number of rows and
    columns.
    '''
    window_size = [
      (self.block_size * self.columns) + (self.columns - 1),
      (self.block_size * self.rows) + (self.rows - 1)
    ]
    pygame.display.set_mode(window_size)

  def add_grid_cell(self, rect, color):
    '''
    Appends a new Cell object to the list of grid cells.

    Parameters:
      rect: Rectangle of the grid cell.
      color: An RGB value to associate with the grid cell.
    '''
    cell = Cell(rect, color)
    self.cell_rects.append(cell)

  def _build_grid(self):
    '''
    Builds each grid cell based on the number of rows and columns, and its
    position within in the grid.
    '''
    for row in range(self.rows):
      for col in range(self.columns):
        rect = pygame.Rect(
          col * (self.block_size + 1),
          row * (self.block_size + 1),
          self.block_size, self.block_size
        )
        self.add_grid_cell(rect, COLOR_WHITE)
  
  def _draw_grid_rects(self, surface):
    '''
    Draws the rectangles of each grid cell on screen.

    Parameters:
      surface: Pygame's drawing surface.
    '''
    for cell in self.cell_rects:
      pygame.draw.rect(surface, cell.color, cell.rect)

  def _colorize_from_matrix(self):
    '''
    Colorizes the grid cells according to data from the generated matrix to
    represents starting and destination cells, obstacles, and the path from
    the starting cell to the destination cell.
    '''
    if len(self.generated_matrix) == 0:
      return
    
    for cell in self.cell_rects:
      row = cell.rect.y // self.block_size
      col = cell.rect.x // self.block_size
      
      if self.generated_matrix[row][col] == Grid.GRID_IND_STARTING_CELL:
        cell.color = COLOR_RED
      elif self.generated_matrix[row][col] == Grid.GRID_IND_OBSTACLE:
        cell.color = COLOR_DARK_GREY
      elif self.generated_matrix[row][col] == Grid.GRID_IND_EXPANSION:
        cell.color = COLOR_YELLOW
      elif self.generated_matrix[row][col] == Grid.GRID_IND_PATH:
        cell.color = COLOR_GREY
      elif self.generated_matrix[row][col] == Grid.GRID_IND_DESTINATION_CELL:
        cell.color = COLOR_GREEN

  def run(self):
    '''
    Shows the GUI.
    '''
    surface = pygame.display.get_surface()
    surface.fill(COLOR_BLACK)
    
    self._build_grid()
    self._colorize_from_matrix()
    self._draw_grid_rects(surface)
    
    pygame.display.flip()

    done = False
    while not done:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()
        elif event.type == pygame.KEYDOWN and \
             event.key == pygame.K_SPACE:
          done = True
      self.clock.tick(30)