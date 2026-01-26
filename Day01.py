# # -----------------------------
# # Basic Print Statement
# # -----------------------------
# print("Hello World!")


# # -----------------------------
# # Variables and String Operations
# # -----------------------------
# name = "Shivam Patel"
# dob = "20 July 2005"

# # Convert name to uppercase and print with DOB
# print(name.upper() + " " + dob)


# # -----------------------------
# # Numeric Operations
# # -----------------------------
# num1 = 10.58562
# num2 = 54710.55

# total = num1 + num2
# print("The sum of", num1, "and", num2, "is", total)

# # Round off num1 to 1 decimal place
# print("The round off value of", num1, "is", round(num1, 1))


# # -----------------------------
# # Functions
# # -----------------------------
# def addition(a, b):
#     return a + b

# def subtraction(a, b):
#     return a - b

# def multiplication(a, b):
#     return a * b

# def division(a, b):
#     return a / b


# print("Addition result:", addition(5, 10))
# print("Subtraction result:", subtraction(10, 5))
# print("Multiplication result:", multiplication(5, 10))
# print("Division result:", division(10, 5))


# # -----------------------------
# # If-Elif-Else Statement
# # -----------------------------
# num = 15

# if num > 0:
#     print("The number is positive")
# elif num == 0:
#     print("The number is zero")
# else:
#     print("The number is negative")


# # -----------------------------
# # List and List Methods
# # -----------------------------
# my_list = [10, 20, 30, 40]
# print("Original list:", my_list)

# # Modify elements
# my_list[1] = 25
# print("After modification:", my_list)

# # Access elements
# print("First element:", my_list[0])
# print("Last element:", my_list[-1])

# # Add elements
# my_list.append(50)
# my_list.insert(2, 35)
# my_list.extend([60, 70, 80])
# print("After adding elements:", my_list)

# # Remove elements
# my_list.remove(25)
# my_list.pop()
# my_list.pop(2)
# print("After removing elements:", my_list)


# # -----------------------------
# # More List Operations
# # -----------------------------
# my_list = [5, 2, 8, 5, 2, 9]
# print("\nNew list:", my_list)

# print("Count of 5:", my_list.count(5))
# print("Index of 8:", my_list.index(8))

# my_list.sort()
# print("Sorted list:", my_list)

# my_list.sort(reverse=True)
# print("Descending sorted list:", my_list)

# my_list.reverse()
# print("Reversed list:", my_list)

# copied_list = my_list.copy()
# print("Copied list:", copied_list)

# print("Length:", len(my_list))
# print("Max value:", max(my_list))
# print("Min value:", min(my_list))
# print("Sum:", sum(my_list))                                                # Sum of elements



# import os                                                                    #taking input in python

# number = input("Enter the names of folder to be created with space between them: ").split()
# print(number)
# for i in number:
#     print(os.listdir(i))  



# try:                                                                          #exception handeling using
#     num1 = int(input("Enter first number: "))                                 #multiple try catch block
#     num2 = int(input("Enter second number: "))

#     result = num1 / num2

# except ValueError:
#     print("❌ Error: Please enter only numbers")

# except ZeroDivisionError:
#     print("❌ Error: Cannot divide by zero")

# except Exception as e:
#     print("❌ Unknown error:", e)

# else:
#     print("✅ Result:", result)

# finally:
#     print("🔁 Program finished")




student = {                                                  #dictionary and its important methods
    "name": "Shivam",       
    "age": 18,              
    "course": "CSIT"        
}

# Access value
print(student["name"])      # Shivam  -> access by key

# Using get() -> safe access
print(student.get("age"))   # 18
print(student.get("grade", "Not Assigned"))  # Not Assigned -> default value if key not present

# Add / Update key-value
student["grade"] = "A"      # add new key
student["age"] = 19         # update existing key
print(student)

# Remove key
student.pop("course")       # removes "course"
print(student)

# Remove last inserted item (Python 3.7+)
student.popitem()           # removes last key-value pair
print(student)

# Check if key exists
print("name" in student)    # True
print("course" in student)  # False

# Loop through dictionary
for key, value in student.items():  # items() -> key & value
    print(key, ":", value)

# Get all keys
print(student.keys())        # dict_keys(['name', 'age'])

# Get all values
print(student.values())      # dict_values(['Shivam', 19])

# Copy dictionary
new_student = student.copy()
print(new_student)
