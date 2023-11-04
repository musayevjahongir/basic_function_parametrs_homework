# Create a function named calculate_average that takes a list of numbers as a parameter.
# Inside the function, calculate the average of all the numbers in the given list.
# Return the average.
# Return the average.
from basic_function_parameter02 import calculate_sum
def calculate_average(lst):
    s=calculate_sum(lst)
    ort=s/len(lst)
    return ort
print(calculate_average([1,2,3,4,5,6,7,8,9]))