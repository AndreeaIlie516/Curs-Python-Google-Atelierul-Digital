def compute_sum_of_all_numbers_in_interval(n):
    if n == 0:
        return 0
    return n + compute_sum_of_all_numbers_in_interval(n - 1)


def compute_sum_of_even_numbers_in_interval(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + compute_sum_of_even_numbers_in_interval(n - 2)
    return compute_sum_of_even_numbers_in_interval(n - 1)


def compute_sum_of_odd_numbers_in_interval(n):
    if n == 0 or n == -1:
        return 0
    if n % 2 == 1:
        return n + compute_sum_of_odd_numbers_in_interval(n - 2)
    return compute_sum_of_odd_numbers_in_interval(n - 1)
