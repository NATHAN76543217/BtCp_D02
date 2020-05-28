#!/usr/bin/python3

def ft_filter(function_to_apply, list_of_inputs):
    for entry in list_of_inputs:
        if not function_to_apply(entry):
            list_of_inputs.remove(entry)
    return list_of_inputs
