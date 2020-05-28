#!/usr/bin/python3

# def ft_map(function_to_apply, list_of_inputs):
#     new = []
#     for entry in list_of_inputs:
#         new.append(function_to_apply(entry))
#     return new

def ft_map(function_to_apply, list_of_inputs):
    i = 0
    for entry in list_of_inputs:
        list_of_inputs[i] = function_to_apply(entry)
        i += 1
    return list_of_inputs
