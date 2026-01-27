

class student:                         # del kayword use in python
    def __init__(self, name):
        self.name = name

s1 = student("Shivam")
print(s1.name)                          #this will print name 
del s1                                  #atribute is deleted by del keyword
print(s1.name) 