def find_union_and_intersection(list1, list2):
    # Convert lists to sets
    set1 = set(list1)
    set2 = set(list2)

    # Union of sets
    union_set = set1.union(set2)
    print("Union of list1 and list2:", union_set)

    # Intersection of sets
    intersection_set = set1.intersection(set2)
    print("Intersection of list1 and list2:", intersection_set)


if _name_ == "_main_":
    # User input for list1
    list1_str = input("Enter elements of list1 separated by spaces: ")
    list1 = [int(x) for x in list1_str.split()]

    # User input for list2
    list2_str = input("Enter elements of list2 separated by spaces: ")
    list2 = [int(x) for x in list2_str.split()]

    find_union_and_intersection(list1, list2)
