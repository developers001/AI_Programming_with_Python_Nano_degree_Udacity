def common_element(list1, list2):
    for i in list1:
        if i in list2:
            return True
        else:
            return False

# Example usage
list1 = ["Tom", "Bob", "Sue", "Rachel"]
list2 = ["Bob", "Susan", "Roger", "Mike"]
print(common_element(list1, list2))

