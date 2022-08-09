def get_ranged_int(prompt, min, max = None):
  '''
  Prompts the user to input an integer between a minimum and a maximum.

  Parameters:
    prompt: A message to display for the prompt.
    min: Minimum integer input.
    max: Maximum integer input.

  Returns:
    Integer.
  '''
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
  '''
  Prompts the user to input two comma separated integers to represent the 2D
  coordinates of a matrix element.

  Parameters:
    prompt: A message to display for the prompt.
    row_min: Minimum row value allowed.
    row_max: Maximum row value allowed.
    col_min: Minimum column value allowed.
    col_min: Maximum column value allowed.

  Returns:
    Tuple containing row and column input.
  '''
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

def get_yes_no(prompt):
  '''
  Prompts the user to input a case-insensitive "y", "yes", "n" or "no".

  Parameters:
    prompt: A message to display for the prompt.

  Returns:
    Boolean; True if input is "y" or "yes, False if input is "n" or "no"
  '''
  while True:
    value = input(prompt)
    if any(value.lower() == v for v in ["y", "yes"]):
      ret = True
      break
    elif any(value.lower() == v for v in ["n", "no"]):
      ret = False
      break
    elif value == "":
      ret = True
      break
    else:
      print("Please answer with either Y or N")
      continue
  return ret