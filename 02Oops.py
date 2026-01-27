# class student:                                 #### Object Oriented programming
#     name = "Shivam Patel"
#     DOB = 2005


# s1 = student






# class student:                                  ## init constructor
#     def __init__(self):
#         print("This is a init function")
#     name = "Shivam Patel"
#     DOB = 2005

# s1 = student()


# class student:                                   ##slef parameter in init constructor
#     def __init__(self, other_argument):
#         print("This is a init function")
#         self.argument = other_argument
#     name = "Shivam Patel"
#     DOB = 2005

# s1 = student("This is other aurgument passed to init function")
# print(s1.argument)



# class student:                          #printing the avearge marks of 3 subject of the student
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         avg = sum/3    
#         print("The average marks of " + self.name + " is " +  str(round(avg, 2)))

# s1 = student("Shivam Patel", [41, 45, 56])
# s1.get_avg()        



# class student:                                          #a static method that does not take self parameter
#     @staticmethod
#     def college(college_name):
#         print(college_name)

# s1 = student
# s1.college("MJPRU")




# class Account:
#     def __init__(self, account, balance):
#         self.acc = account
#         self.bal = balance

#     def debit(self, amount):
#         self.bal -= amount
#         print("Amount", amount, "is debited")

#     def credit(self, amount):
#         self.bal += amount
#         print("Amount", amount, "is credited")

#     def get_bal(self):
#         return self.bal


# acc1 = Account(999999, 10000)

# print("Initial Balance:", acc1.get_bal())

# acc1.debit(2000)
# print("Balance after debit:", acc1.get_bal())

# acc1.credit(5000)
# print("Balance after credit:", acc1.get_bal())
     




# class student:                         # del kayword use in python
#     def __init__(self, name):
#         self.name = name

# s1 = student("Shivam")
# print(s1.name)                          #this will print name 
# del s1                                  #object is deleted by del keyword
# # print(s1.name)                          #this will give error




# class car:                                  #inheritence
#     @staticmethod
#     def start():
#         print("Car Started")

#     def stop():
#         print("Car Stopped")    


# class Toyotacar(car):
#     def __init__(self, name):
#         self.name = name


# car1 = Toyotacar("Fortuner")
# car2 = Toyotacar("Nexon")
# print(car1.name)


# class Parent:                                #single inheritence
#     def show(self):
#         print("Parent class")

# class Child(Parent):
#     pass

# c = Child()
# c.show()


# class GrandParent:                            #multi-level inheritence
#     def gp(self):
#         print("Grand Parent")

# class Parent(GrandParent):
#     pass

# class Child(Parent):
#     pass

# c = Child()
# c.gp()

# class Father:                               #multilevel inheritence
#     def f(self):
#         print("Father")

# class Mother:
#     def m(self):
#         print("Mother")

# class Child(Father, Mother):
#     pass

# c = Child()
# c.f()
# c.m()



