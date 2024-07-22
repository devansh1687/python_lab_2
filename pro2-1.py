def interchange(lst):
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst
my_list = [1, 2, 3, 4, 5]
print("Original List: ", my_list)
print("List after interchange: ", interchange(my_list))
