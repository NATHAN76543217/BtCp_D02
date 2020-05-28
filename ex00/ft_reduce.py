#!/usr/bin/python3

def ft_reduce(function_to_apply, list_of_inputs):
    if not isinstance(function_to_apply, type(ft_reduce)):
        raise TypeError("first param must be a function ")
    first = 1
    res = list_of_inputs[0]
    for entry in list_of_inputs:
        if not first:
            res = function_to_apply(res, entry)
        first = 0
    return res
