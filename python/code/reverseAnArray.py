'''
Write a function to reverse an array or string
Difficulty Level : Basic
Last Updated : 08 Sep, 2020
 
Given an array (or string), the task is to reverse the array/string.
Examples : 
 

Input  : array[] = ["a", "b", "c"]
Output : array[] = ["c", "b", "a"]

Input :  array[] = [1, 2, 3, 4, 5]
Output : array[] = [5, 4, 3, 2, 1]
'''

#list slicing
def reverse_array_or_string(array):
    return array[::-1]


#for both types of variables
def reverse_array_or_string(array):
    if isinstance(array,str):
        array = list(array)
        array = "".join(reverse_array(array))
        return array
    elif isinstance(array, list):
        return reverse_array(array)
    else:
        return "it is not a list or array"


#for only arrays not strings
def reverse_array(array):
    array = list(array)
    n = len(array) - 1
    i = 0
    while i < n:
        array[i],array[n] = array[n],array[i]
        i = i + 1
        n = n - 1
    return array
