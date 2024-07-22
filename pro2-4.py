def element_exists(lst, elem):
    return elem in lst
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_element = 5

if element_exists(my_list, target_element):
    print(f"{target_element} exists in the list!")
else:
    print(f"{target_element} does not exist in the list.")
