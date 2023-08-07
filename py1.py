#count word frequency
def count_word_frequency(paragraph,word):
    word_list = paragraph.lower().split()
    word_count = word_list.count(word.lower())
    return word_count

paragraph = "My name is Shivanshi Singh, register number 2347254 year 2023-2025 and my domain is music store management system.The Music Store Management System is a comprehensive solution for managing a music store's inventory and sales. The music store offers a wide range of musical instruments, albums, and CDs to its customers. The Music Store Management System ensures efficient management of these items and tracks sales data for better decision-making."

word =  input("Enter the word to count frequency: ")
frequency = count_word_frequency(paragraph, word)
print(f"The frequency of the word '{word}' in the paragraph is: {frequency}")

#python program to display all the datatypes of selected specific element in the paragraph.
paragraph = "My name is Shivanshi Singh, register number 2347254 year 2023-2025 and my domain is music store management system.The Music Store Management System is a comprehensive solution for managing a music store's inventory and sales. The music store offers a wide range of musical instruments, albums, and CDs to its customers. The Music Store Management System ensures efficient management of these items and tracks sales data for better decision-making."
\
words = paragraph.split(" ")
for i in words:
    for j in i:
        if (ord(j) >= 48 and ord(j) <= 57):
            if "." in i:
                print(i, " is float.")
                break
            else:
                print(i, " is Integer.")
                break
        else:
            print(i, " is String")
            break
    else:
        print("word not found")

#program to count the number of alphabets, numeric and other special symbols in the paragraph.
def count(paragraph):
    alpha_count = 0
    numeric_count = 0
    special_count = 0

    for char in paragraph:
        if char.isalpha():
            alpha_count += 1
        elif char.isdigit():
            numeric_count += 1
        else:
            special_count += 1

    return alpha_count, numeric_count, special_count

paragraph = "My name is Shivanshi Singh, register number 2347254 year 2023-2025 and my domain is music store management system.The Music Store Management System is a comprehensive solution for managing a music store's inventory and sales. The music store offers a wide range of musical instruments, albums, and CDs to its customers. The Music Store Management System ensures efficient management of these items and tracks sales data for better decision-making."

alpha, numeric, special = count(paragraph)
print(f"Number of Alphabets: {alpha}")
print(f"Number of Numeric Characters: {numeric}")
print(f"Number of Special Symbols: {special}")
