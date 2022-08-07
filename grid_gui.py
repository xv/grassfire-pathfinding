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

class GridPlot():
  cell_rects = []
  generated_matrix = []
  exploration_path = []

  def __init__(self, grid_rows, grid_columns, block_size):
    pygame.init()
    pygame.display.set_caption("Grid Plot")

    self.grid_rows = grid_rows
    self.grid_columns = grid_columns
    self.block_size = block_size
    self._set_window_size()
    self.clock = pygame.time.Clock()

  def _set_window_size(self):
    window_size = [
      (self.block_size * self.grid_columns) + (self.grid_columns - 1),
      (self.block_size * self.grid_rows) + (self.grid_rows - 1)
    ]
    pygame.display.set_mode(window_size)

  def _build_grid_rects(self):
    for row in range(self.grid_rows):
      for col in range(self.grid_columns):
        rect = pygame.Rect(
          col * (self.block_size + 1),
          row * (self.block_size + 1),
          self.block_size, self.block_size
        )
        self.cell_rects.append((rect, COLOR_WHITE))
  
  def _draw_grid_rects(self, surface):
    for grid_rect, color in self.cell_rects:
      pygame.draw.rect(surface, color, grid_rect)

  def _fill_from_exploration_path(self):
    for i, rect in enumerate(self.cell_rects):
      row = rect[0].y // self.block_size
      col = rect[0].x // self.block_size
      for j, coord in enumerate(self.exploration_path):
        if row == coord[0] and col == coord[1]:
          if j == 0:
            # Starting cell
            self.cell_rects[i] = (rect[0], COLOR_RED)
          elif j == len(self.exploration_path) - 1:
            # Destination cell
            self.cell_rects[i] = (rect[0], COLOR_GREEN)
          else:
            # Exploration path
            self.cecell_rectslls[i] = (rect[0], COLOR_GREY)
  
  def _fill_from_generated_matrix(self):
    for i, rect in enumerate(self.cell_rects):
      row = rect[0].y // self.block_size
      col = rect[0].x // self.block_size
      
      if self.generated_matrix[row][col] == Grid.GRID_IND_STARTING_CELL:
        self.cell_rects[i] = (rect[0], COLOR_RED)
      elif self.generated_matrix[row][col] == Grid.GRID_IND_OBSTACLE:
        self.cell_rects[i] = (rect[0], COLOR_DARK_GREY)
      elif self.generated_matrix[row][col] == Grid.GRID_IND_EXPANSION:
        self.cell_rects[i] = (rect[0], COLOR_YELLOW)
      elif self.generated_matrix[row][col] == Grid.GRID_IND_PATH:
        self.cell_rects[i] = (rect[0], COLOR_GREY)
      elif self.generated_matrix[row][col] == Grid.GRID_IND_DESTINATION_CELL:
        self.cell_rects[i] = (rect[0], COLOR_GREEN)

  def run(self):
    surface = pygame.display.get_surface()
    surface.fill(COLOR_BLACK)
    
    # Builds the grid rectangles (cells) based on the specified number of
    # rows, columns, and the size of the block
    self._build_grid_rects()

    # Colorizes the grid cells based on whether they represent a starting cell,
    # destination cell, exploration path or obstacle
    #
    # This method differs from fill_from_exploration_path() such that the latter
    # only colorizes the starting and destination cells, and the exploration
    # path (obstacles not included)
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