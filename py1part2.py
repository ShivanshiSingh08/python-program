#set operations

music_set = {10, 3.14, 'guitar', True, 'piano', 'drums'}
print("Original Set:", music_set)

popped_element = music_set.pop()
print("Popped Element:", popped_element)


music_set.discard('guitar')
print("Set after discarding 'guitar':", music_set)

music_set.clear()
print("Set after clear():", music_set)

del music_set 
# sorting in descending order
music_set = {'vocals', 'guitar', 'piano', 'drums', 'bass', 'keyboard'}
print("Updated Set in descending order:", sorted(music_set, reverse=True))

#packing and unpacking
music_tuple = ('Music Store', 'retail store', 100,'Sales')
store_name, category, num_items, department = music_tuple
print("Tuple Elements:")
print("Store Name:", store_name)
print("Category:", category)
print("Number of Items:", num_items)
print("Department:", department)

#frequency of character
domain_name = "'m','u','s','i','c','s','t','o','r','e','m','a','n','a','g','e','m','e','n','t','s','y','s','t','e','m'"
char_to_count = input("Enter a character to count its occurrences: ")
count_occurrences = 0
for char in domain_name:
    if char == char_to_count:
        count_occurrences += 1

print(f"Count of '{char_to_count}' in the domain name: {count_occurrences}")
#slicing
domain_name = "music store management system"
print("Original Domain Name:", domain_name)

print("\nSlicing Possibilities:")
print("1. First 5 characters:", domain_name[:5])
print("2. Last 5 characters:", domain_name[-5:])
print("3. Characters from index 5 to 14:", domain_name[5:15])
print("4. Characters with a step of 2:", domain_name[::2])
print("5. Reversed string:", domain_name[::-1])

# Negative indexing
print("\nNegative Indexing:")
print("1. Last character:", domain_name[-1])
print("2. Second last character:", domain_name[-2])
print("3. Third last character:", domain_name[-3])
