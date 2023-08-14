def have_common_member(list1, list2):
    return any(item in list2 for item in list1)

# Prompt the user to enter the first list
list1 = input("Enter the first list (space-separated): ").split()

# Prompt the user to enter the second list
list2 = input("Enter the second list (space-separated): ").split()

# Check if the lists have a common member
has_common_member = have_common_member(list1, list2)

# Display the result
if has_common_member:
    print("The lists have at least one common member.")
else:
    print("The lists do not have any common member.")
