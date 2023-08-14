#Write a Python function that takes two lists and returns True if they have at least one common member.eg. [“Tom”, “Bob”, “Sue”, “Rachel”],  [“Bob”, “Susan”, “Roger”, “Mike”]returns true as Bob is common.
def has_common_member(list1, list2):
  """
  Returns True if the two lists have at least one common member.

  Args:
    list1: The first list.
    list2: The second list.

  Returns:
    True if the two lists have at least one common member, False otherwise.
  """

  for item in list1:
    if item in list2:
      return True
  return False


if __name__ == "__main__":
  list1 = ["Tom", "Bob", "Sue", "Rachel"]
  list2 = ["Bob", "Susan", "Roger", "Mike"]
  print(has_common_member(list1, list2))
