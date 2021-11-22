from sum_module import *


def compute_sum_int_real_numbers(*args, **kwargs):
    sum_of_arguments = 0
    for args_index in args:
        if type(args_index) == type([]):
            for list_index in args_index:
                try:
                    number = float(list_index)
                    try:
                        number = int(number)
                    except ValueError:
                        pass
                    sum_of_arguments += number
                except ValueError:
                    pass
        else:
            try:
                number = float(args_index)
                try:
                    number = int(number)
                except ValueError:
                    pass
                sum_of_arguments += number
            except ValueError:
                pass
    return sum_of_arguments


def check_zero_number(number):
    try:
        number = int(number)
        return number
    except ValueError:
        return 0


if __name__ == '__main__':
    sum_of_arguments = compute_sum_int_real_numbers(1, 5, -3, 'abc', [12, 56, 'cad'], param_1=2)
    print("The sum of the arguments is: " + str(sum_of_arguments) + '.\n')

    number_to_check = input("Please insert a number: ")
    result_of_check = check_zero_number(number_to_check)
    if result_of_check != 0:
        print("You inserted the integer number " + str(result_of_check) + '.\n')
    else:
        print("You inserted a number which is not integer or a character which is not a number.\n")

    try:
        n = int(input("Please insert the upper extremity of the interval: "))
        sum_of_all_numbers_in_interval = compute_sum_of_all_numbers_in_interval(n)
        print("The sum of the interval is: " + str(sum_of_all_numbers_in_interval) + '\n')
    except ValueError as ve:
        print(ve)

    try:
        n = int(input("Please insert the upper extremity of the interval: "))
        sum_of_even_numbers_in_interval = compute_sum_of_even_numbers_in_interval(n)
        print("The sum of the interval is: " + str(sum_of_even_numbers_in_interval) + '\n')
    except ValueError as ve:
        print(ve)

    try:
        n = int(input("Please insert the upper extremity of the interval: "))
        sum_of_odd_numbers_in_interval = compute_sum_of_odd_numbers_in_interval(n)
        print("The sum of the interval is: " + str(sum_of_odd_numbers_in_interval) + '\n')
    except ValueError as ve:
        print(ve)
