#      Create a LIST with your domain attributes, insert the elements using the append (), insert(), extend() and add any iterables (tuples, sets, dictionaries etc.) to the list (Use all the methods ).
#                 Create a list with numeric and perform the following operations.
#       Write a program to swap the first and last elements in a list.
#       Write a program to find the sum of the digits in a list.
#       Write a program to find the smallest element in a list.

# Take inputs for domain attributes
domain_attributes = []
num_attributes = int(input("Enter the number of domain attributes: "))
for i in range(num_attributes):
    attribute = input(f"Enter domain attribute {i+1}: ")
    domain_attributes.append(attribute)

# Insert elements using append()
domain_attributes.append(input("Enter an attribute to append: "))

# Insert elements using insert()
position = int(input("Enter the position to insert a new attribute: "))
domain_attributes.insert(position, input("Enter an attribute to insert: "))

# Take inputs for the tuple to extend
more_attributes_tuple_input = input("Enter additional attributes to extend (comma-separated): ")
more_attributes_tuple = tuple(more_attributes_tuple_input.split(','))
domain_attributes.extend(more_attributes_tuple)

# Take inputs for the set to extend
more_attributes_set_input = input("Enter additional attributes to extend (comma-separated): ")
more_attributes_set = set(more_attributes_set_input.split(','))
domain_attributes.extend(more_attributes_set)

# Take inputs for numeric elements
numeric_list = []
num_elements = int(input("Enter the number of numeric elements: "))
for i in range(num_elements):
    element = int(input(f"Enter numeric element {i+1}: "))
    numeric_list.append(element)

# Swap the first and last elements in the list
numeric_list[0], numeric_list[-1] = numeric_list[-1], numeric_list[0]

# Find the sum of the digits in the list
sum_of_digits = sum(numeric_list)

# Find the smallest element in the list
smallest_element = min(numeric_list)

# Print the results
print("Domain Attributes List:", domain_attributes)
print("Numeric List:", numeric_list)
print("Sum of Digits:", sum_of_digits)
print("Smallest Element:", smallest_element)

#Dictionary
# Function to sort the dictionary by keys in ascending order
def sort_dictionary_by_keys(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[0]))
    return sorted_dict

# Function to find the sum of all values in the dictionary
def sum_of_values(dictionary):
    total_sum = sum(dictionary.values())
    return total_sum

# Function to sort the dictionary by values in descending order using lambda function
def sort_dictionary_by_values_desc(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

# Take inputs for creating the dictionary
num_entries = int(input("Enter the number of dictionary entries: "))
user_dict = {}
for i in range(num_entries):
    key = input(f"Enter key {i+1}: ")
    value = float(input(f"Enter value for {key}: "))
    user_dict[key] = value

# Sort the dictionary by keys in ascending order
sorted_dict_by_keys = sort_dictionary_by_keys(user_dict)

# Find the sum of all values in the dictionary
total_sum_values = sum_of_values(user_dict)

# Sort the dictionary by values in descending order
sorted_dict_by_values_desc = sort_dictionary_by_values_desc(user_dict)

# Print the results
print("Dictionary sorted by keys in ascending order:", sorted_dict_by_keys)
print("Sum of all values in the dictionary:", total_sum_values)
print("Dictionary sorted by values in descending order:", sorted_dict_by_values_desc)
