#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [3, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 10)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, 20)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, 30)
print("nb_print: {:d}".format(nb_print))
