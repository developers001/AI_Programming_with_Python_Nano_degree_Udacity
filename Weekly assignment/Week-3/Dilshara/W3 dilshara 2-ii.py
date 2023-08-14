def has_common_member():
    list1 = input("Enter the first list of members (comma-separated): ").split(",")
    list2 = input("Enter the second list of members (comma-separated): ").split(",")
    
    for member in list1:
        if member.strip() in list2:
            return True
    
    return False


# Call the function to check for common members
result = has_common_member()

# Print the result
if result:
    print("The lists have at least one common member.")
else:
    print("The lists do not have any common members.")
