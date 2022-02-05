def get_ranged_int(prompt, min, max=None):
  while True:
    try:
      value = int(input(prompt))
    except ValueError:
      print("Input is of invalid format")
      continue

    if value < min:
      print(f"Minimum value cannot be less than {min}")
      continue
    elif max is not None and value > max:
      print(f"Maximum value cannot be larger than {max}")
      continue
    else:
      break
  return value

def get_matrix_coords(prompt, row_min, row_max, col_min, col_max):
  while True:
    try:
      value = tuple(int(i) for i in input(prompt).split(","))
    except ValueError:
      print("2D Coordinates must contain 2 integers separated by a comma")
      continue
    
    if len(value) < 2:
      print("Incomplete 2D coordinate")
      continue
    elif len(value) > 2:
      print("2D cooridnate cannot contain more than two values")
      continue
    elif value[0] < row_min:
      print(f"Row value ({value[0]}) must be at least {row_min}")
      continue
    elif value[0] > row_max:
      print(f"Row value ({value[0]}) cannot exceed a maximum of {row_max}")
      continue
    elif value[1] < col_min:
      print(f"Column value ({value[1]}) must be at least {col_min}")
      continue
    elif value[1] > col_max:
      print(f"Column value ({value[1]}) cannot exceed a maximum of {col_max}")
      continue
    else:
      break
  return value
