def get_unique_elements(list1):
    
  unique_elements = []
  for element in list1:
    if element not in unique_elements:
      unique_elements.append(element)
  return unique_elements


if __name__ == "__main__":
  list1 = [1, 2, 3, 90, 4, 5, 1, 2, 3, 784]
  unique_elements = get_unique_elements(list1)
  print(unique_elements)
