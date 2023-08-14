def function(value1, value2):
    if isinstance(value1, str) and isinstance(value2, str):
      print(f'{value1} + {value2} = {value1 + value2}')
      print('The rest of the operations are not applicable​')
    elif isinstance(value1, int) and isinstance(value2, int):
      print(f'{value1} + {value2} = {value1 + value2}')
      print(f'{value1} - {value2} = {value1 - value2}')
      print(f'{value1} * {value2} = {value1 * value2}')
      if value2 != 0:
        print(f'{value1} / {value2} = {value1 / value2}')
      else:
        print(f'{value1} / {value2} = error: cannot divided by 0')
    elif isinstance(value1, int):
      value1_str = str(value1)
      print(f'{value1_str} + {value2} = {value1_str + value2}')
      print(f'{value1} * {value2} = {value1 * value2}')
    else:
      value2_str = str(value2)
      print(f'{value1} + {value2_str} = {value1 + value2_str}')
      print(f'{value1} * {value2} = {value1 * value2}')
      
function(2, 3)
function('Hi', 'Raju')
function(2, 'raju')