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
    self.rect = rect
    self.color = color

  def __str__(self):
    return f"({self.rect}, {self.color})"

class GridPlot():
  def __init__(self, grid_rows, grid_columns, block_size):
    pygame.init()
    pygame.display.set_caption("Grid Plot")

    self.grid_rows = grid_rows
    self.grid_columns = grid_columns
    self.block_size = block_size

    self.cell_rects = []
    self.generated_matrix = []
    self.exploration_path = []

    self._set_window_size()
    self.clock = pygame.time.Clock()

  def _set_window_size(self):
    window_size = [
      (self.block_size * self.grid_columns) + (self.grid_columns - 1),
      (self.block_size * self.grid_rows) + (self.grid_rows - 1)
    ]
    pygame.display.set_mode(window_size)

  def add_grid_cell(self, rect, color):
    cell = Cell(rect, color)
    self.cell_rects.append(cell)

  def _build_grid_rects(self):
    for row in range(self.grid_rows):
      for col in range(self.grid_columns):
        rect = pygame.Rect(
          col * (self.block_size + 1),
          row * (self.block_size + 1),
          self.block_size, self.block_size
        )
        self.add_grid_cell(rect, COLOR_WHITE)
  
  def _draw_grid_rects(self, surface):
    for cell in self.cell_rects:
      pygame.draw.rect(surface, cell.color, cell.rect)

  def _fill_from_exploration_path(self):
    for cell in self.cell_rects:
      row = cell.rect.y // self.block_size
      col = cell.rect.x // self.block_size
      for j, coord in enumerate(self.exploration_path):
        if row == coord[0] and col == coord[1]:
          if j == 0:
            # Starting cell
            cell.color = COLOR_RED
          elif j == len(self.exploration_path) - 1:
            # Destination cell
            cell.color = COLOR_GREEN
          else:
            # Exploration path
            cell.color = COLOR_GREY
  
  def _fill_from_generated_matrix(self):
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
    surface = pygame.display.get_surface()
    surface.fill(COLOR_BLACK)
    
    # Builds the grid rectangles (cells) based on the specified number of
    # rows, columns, and the size of the block
    self._build_grid_rects()

    # Colorizes the grid cells based on whether they represent a starting cell,
    # destination cell, exploration path or obstacle
    #
    # Alternatively, _fill_from_exploration_path() can be used to colorize
    # only the starting and destination cells, and the path between them
    self._fill_from_generated_matrix()

    # Draws the actual rectangles
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