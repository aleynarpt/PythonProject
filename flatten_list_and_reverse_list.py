# First Question:
# Write a function that flattens a list. Its elements can consist of multi-layered lists or non-scalar data
# For example;
# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# output: [1,'a','cat',2,3,'dog',4,5]

list1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten_list(list1):
    flattened = []
    for item in list1:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

output_1 = flatten_list(list1)
print(output_1)


# Second Question
# Write a function that reverses the elements in the given list. If the elements inside the list also contain the list, reverse their elements as well.
# For example;
# input: [[1, 2], [3, 4], [5, 6, 7]]
# output: [[[7, 6, 5], [4, 3], [2, 1]]


list2 = [[1, 2], [3, 4], [5, 6, 7]]

def reverse_list(list2):
    reversed_list = []
    for item in list2[::-1]:
        if isinstance(item, list):
            reversed_list.append(reverse_list(item))
        else:
            reversed_list.append(item)
    return reversed_list

output_2 = reverse_list(list2)
print(output_2)