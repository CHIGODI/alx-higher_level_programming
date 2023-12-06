#!/usr/bin/python3


def weight_average(my_list=[]):

    if len(my_list) == 0:
        return 0
    weights = sum(num[1] for num in my_list)
    weighted_sum = sum(num[0] * num[1] for num in my_list)
    weighted_avg = weighted_sum / weights

    return weighted_avg
