from grid import Grid
from grid_gui import GridPlot
from grassfire import Grassfire

if __name__ == "__main__":
  print("Generating grid...\n")
  # grid = Grid(8, 8, 20, (1, 1), (6, 5))
  grid = Grid.init_from_user_input()
  generated_grid = grid.generate_grid()
  print()
  print(generated_grid)
  print()
  grid.print_grid_description()
  
  print("\nSolving...\n")
  algo = Grassfire(generated_grid)
  path = algo.run(grid.start_cell, grid.dest_cell)
  
  path_size = len(path)
  if path_size > 0:
    print(f"\u2192 It took {path_size} steps to reach destination")
    print(f"\u2192 Path: {path}\n")
  else:
    print("\u2192 No solution!\n")
    exit()

  print("Plotting path...\n")
  grid.plot_path(generated_grid, path)
  print(generated_grid)

  print("\nPlotting grid in GUI...")
  grid_gui = GridPlot(grid.rows, grid.columns, 40)
  grid_gui.generated_matrix = generated_grid
  grid_gui.exploration_path = path
  grid_gui.run()