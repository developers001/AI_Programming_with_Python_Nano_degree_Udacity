#Write a Python program/function to combine two dictionary adding values for common keys.eg.d1 = {'a': 100, 'b': 200, 'c':300}d2 = {'a': 300, 'b': 200, 'd':400}Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
def combine_dictionaries(dict1, dict2):
  """
  Combines two dictionaries adding values for common keys.

  Args:
    dict1: The first dictionary.
    dict2: The second dictionary.

  Returns:
    A new dictionary with the combined values.
  """

  combined_dict = dict1.copy()
  for key, value in dict2.items():
    if key in combined_dict:
      combined_dict[key] += value
    else:
      combined_dict[key] = value
  return combined_dict


if __name__ == "__main__":
  dict1 = {'a': 100, 'b': 200, 'c':300}
  dict2 = {'a': 300, 'b': 200, 'd':400}
  combined_dict = combine_dictionaries(dict1, dict2)
  print(combined_dict)
