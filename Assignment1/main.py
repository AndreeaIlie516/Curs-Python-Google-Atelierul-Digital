def print_list(list_to_print):
    print("The list is: " + str(list_to_print))


def print_order_ascending(list_to_copy):
    new_list = list_to_copy.copy()
    new_list.sort()
    print("The ordered list in ascending order is: " + str(new_list))


def print_order_descending(list_to_copy):
    new_list = list_to_copy.copy()
    new_list.sort(reverse=True)
    print("The ordered list in descending order is: " + str(new_list))


def print_elements_with_even_index(list_to_slice):
    new_list_sliced = list_to_slice[::2]
    print("The elements on the even positions in the list are: " + str(new_list_sliced))


def print_elements_with_odd_index(list_to_slice):
    new_list_sliced = list_to_slice[1::2]
    print("The elements on the odd positions in the list are: " + str(new_list_sliced))


def print_elements_multiplies_of_3(list_to_check):
    new_list = []
    for i in list_to_check:
        if i % 3 == 0:
            new_list.append(i)
    print("The elements which are multiplies of 3 in the list are: " + str(new_list))


if __name__ == '__main__':
    my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
    print_list(my_list)
    print_order_ascending(my_list)
    print_order_descending(my_list)
    print_elements_with_even_index(my_list)
    print_elements_with_odd_index(my_list)
    print_elements_multiplies_of_3(my_list)
