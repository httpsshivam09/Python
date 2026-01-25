print("Hello World!")                                                    # Print Hello World to the console

name = "Shivam Patel"
Dob = "20 July 2005"                                                     # Store date of birth

print(name.upper() + " " + Dob)                                          # Convert name to uppercase and concatenate with DOB

num1 = 10.58562                                       
num2 = 54710.55                                       
sum = num1 + num2                                     

print("The sum of " + str(num1) + " and " + str(num2) + " is " + str(sum))  
print("The Round off value of " + str(num1) + " is " + str(round(num1, 1))) 

def addition(a, b):                                   
    return a + b
result = addition(5, 10)                               
print("The addition result is: " + str(result))        

def subtraction(a, b):                                 
    return a - b
result = subtraction(10, 5)                          
print("The subtraction result is: " + str(result))

def multiplication(a, b):                              
    return a * b
result = multiplication(5, 10)                           
print("The multiplication result is: " + str(result))  

def division(a, b):                                   
    return a / b
result = division(10, 5)                                  
print("The division result is: " + str(result)) 

# ---------------------------------------------
num = 15                                                                   # if elif else conditional statement

if num > 0:                                                
    print("The number is positive")
elif num == 0:                                           
    print("The number is zero")
else:                                                     
    print("The number is negative")



my_list = [10, 20, 30, 40]                                                 # LIST is
print("Original List:", my_list)                                           #list methods


my_list[1] = 25                                                            # Modify element at index 1
print("After modification:", my_list)
print("First element:", my_list[0])                                        # Access first element
print("Last element:", my_list[-1])                                        # Access last element


my_list.append(50)                                                         # Add element at end
my_list.insert(2, 35)                                                      # Insert at index 2
my_list.extend([60, 70, 80])                                               # Add multiple elements at end
print("After adding elements:", my_list)


my_list.remove(25)                                                         # Remove first occurrence
my_list.pop()                                                              # Remove last element
my_list.pop(2)                                                             # Remove element at index 2
print("After removing elements:", my_list)


my_list = [5, 2, 8, 5, 2, 9]                                               # New list for demonstration
print("\nNew list:", my_list)

print("Count of 5:", my_list.count(5))                                     # Count occurrences
print("Index of 8:", my_list.index(8))                                     # Index of first occurrence

my_list.sort()                                                             # Sort ascending
print("Sorted list:", my_list)
my_list.sort(reverse=True)                                                 # Sort descending
print("Descending sorted list:", my_list)
my_list.reverse()                                                          # Reverse list
print("Reversed list:", my_list)

copied_list = my_list.copy()                                               # Shallow copy
print("Copied list:", copied_list)

print("Length:", len(my_list))                                             # Length of list
print("Max:", max(my_list))                                                # Maximum element
print("Min:", min(my_list))                                                # Minimum element
print("Sum:", sum(my_list))                                                # Sum of elements
