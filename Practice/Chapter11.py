# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class Two_D_Vector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
        print('2d Constructor Called!!')
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class Three_D_Vector(Two_D_Vector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
        print("Constructor Called Three D")
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

# C = Two_D_Vector(50,60)
# D = Three_D_Vector(10,20,30)

# C.show()
# D.show()



# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals:
    @staticmethod
    def __init__(self):
        print("Animal Constructor Called!")

class Pets(Animals):
    @staticmethod
    def __init__(self):
        print("Pets Called!!")

class Dog(Pets):
    def __init__(self):
        print("Dog Called!!")

    @staticmethod
    def bark():
        print("Woof Woof")


# d = Dog()
# d.bark()

"""3. Create a class ‘Employee’ and add salary and increment properties to it.
Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary."""

class Employee:
    salary = 500
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment / 100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment = ((salary / self.salary) - 1) * 100



e = Employee()
# print(e.salaryAfterIncrement)
# e.salaryAfterIncrement = 280
# print(e.increment)


# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.
# 

class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i

    def __add__(self,c2):
        return Complex(self.r + c2.r, self.i + c2.i) # <__main__.Complex object at 0x0000020A7D6D4E10>
    
    # def __mul__(self,c2):
    #     return 
    
    def __str__(self):
        return f"{self.r}r + {self.i}i "

# c1 = Complex(1,2)
# c2 = Complex(3,4)

# print(c1 + c2)


# 5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.


# class vector:
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
    
#     def __add__(self,other):
#         result = vector(self.x + other.x, self.y + other.y, self.z + other.z)
#         return result
    
#     def __mul__(self,other):
#         result = self.x * other.x + self.y * other.y + self.z * other.z
#         return result
    
#     def __str__(self):
#         return f"Vector({self.x}, {self.y}, {self.z})"

# Testing 
# v1 = vector(1,2,3)
# v2 = vector(4,5,6)
# v3 = vector(7,8,9)

"""print(v1 + v2) # Vector(5, 7, 9)
print(v1 * v2) # 32

print(v1 + v3) # Vector(8, 10, 12)
print(v1 * v3) # 50"""


# 6. Write __str__() method to print the vector as follows: 7i + 8j +10k
 
class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self,other):
        result = vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self,other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

# v1 = vector(1,2,3)
# v2 = vector(4,5,6)
# v3 = vector(7,8,9)
# print(v1 + v2)
# print(v1 * v2)


# 7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class vector:
    def __init__(self, list):
        self.list = list
    
    def __len__(self):
        return len(self.list)
    


v1 = vector([1,2,3])
# print(v1 + v2)
# print(v1 * v2)
print(len(v1))