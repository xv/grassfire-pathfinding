from grid import Grid
from grid_gui import GridPlot
from grassfire import Grassfire
from prompts import get_yes_no

def show_grid_window():
  gui = GridPlot(grid.rows, grid.columns, 40)
  gui.generated_matrix = matrix
  gui.run()

if __name__ == "__main__":
  print("Generating grid...\n")

  grid = Grid.init_from_user_input()
  matrix = grid.generate_matrix()

  print()
  grid.print_grid_description()
  
  print("\nSolving...\n")
  
  algo = Grassfire(matrix)
  path = algo.find_path(grid.start_cell, grid.dest_cell)
  
  path_size = len(path)
  if path_size > 0:
    print(f"\u2192 It took {path_size} steps to reach destination")
    print(f"\u2192 Path: {path}\n")
  else:
    print("\u2192 No solution!\n")
    show_gui = get_yes_no("Do you want to see the grid GUI anyway? (Y/N): ")
    if show_gui:
      show_grid_window()
    else:
      exit()

  print("Plotting path in matrix...\n")

  grid.plot_path(matrix, path)
  print(matrix)

  print("\nPlotting matrix in GUI...")

  show_grid_window()