from grid import Grid
import pygame

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_DARK_GREY = (80, 80, 80)
COLOR_GREY = (192, 192, 192)

class GridPlot():
  cells = []
  generated_matrix = []
  exploration_path = []

  def __init__(self, grid_rows: int, grid_columns: int, block_size: int):
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

  def _set_grid_rect(self):
    for row in range(self.grid_rows):
      for col in range(self.grid_columns):
        rect = pygame.Rect(
          col * (self.block_size + 1),
          row * (self.block_size + 1),
          self.block_size, self.block_size
        )
        self.cells.append((rect, COLOR_WHITE))
  
  def _draw_grid_rects(self, surface):
    for grid_rect, color in self.cells:
      pygame.draw.rect(surface, color, grid_rect)

  def _fill_from_exploration_path(self):
    for i, rect in enumerate(self.cells):
      row = rect[0].y // self.block_size
      col = rect[0].x // self.block_size
      for j, coord in enumerate(self.exploration_path):
        if row == coord[0] and col == coord[1]:
          if j == 0:
            # Starting cell
            self.cells[i] = (rect[0], COLOR_RED)
          elif j == len(self.exploration_path) - 1:
            # Destination cell
            self.cells[i] = (rect[0], COLOR_GREEN)
          else:
            # Exploration path
            self.cells[i] = (rect[0], COLOR_GREY)
  
  def _fill_from_generated_matrix(self):
    for i, rect in enumerate(self.cells):
      row = rect[0].y // self.block_size
      col = rect[0].x // self.block_size
      if self.generated_matrix[row][col] == Grid.GRID_IND_STARTING_CELL:
        self.cells[i] = (rect[0], COLOR_RED)
      elif self.generated_matrix[row][col] == Grid.GRID_IND_OBSTACLE:
        self.cells[i] = (rect[0], COLOR_DARK_GREY)
      elif self.generated_matrix[row][col] == Grid.GRID_IND_PATH:
        self.cells[i] = (rect[0], COLOR_GREY)
      elif self.generated_matrix[row][col] == Grid.GRID_IND_DESTINATION_CELL:
        self.cells[i] = (rect[0], COLOR_GREEN)

  def run(self):
    surface = pygame.display.get_surface()
    surface.fill(COLOR_BLACK)
    
    # Builds the grid rectangles (blocks) based on the specified number of
    # rows, columns, and the size of the block
    self._set_grid_rect()

    # Colorizes the grid cells based on whether they represent a starting cell,
    # destination cell, exploration path or obstacle
    #
    # This method differs from fill_from_exploration_path() such that the latter
    # only colorizes the starting and destination cells, and the exploration
    # path
    self._fill_from_generated_matrix()

    # Draws the actual rectangles
    self._draw_grid_rects(surface)

    done = False
    while not done:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()
        elif event.type == pygame.KEYDOWN and \
             event.key == pygame.K_SPACE:
          done = True

      pygame.display.flip()
      self.clock.tick(30)