### Python courses


#### Fifth Part
Python Classes/Objects

Python Inheritance

Python Iterators

Python Polymorphism

Python Scope

Python Modules

Here’s the structured content for the fifth part of your Python course:

---

## **Python Classes/Objects**
Classes are blueprints for creating objects, and objects are instances of classes.

### **Example 1: Creating a Class and Object**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 25)
print(p1.name, p1.age)
```

### **Example 2: Adding Methods to a Class**
```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

p1 = Person("Alice")
p1.greet()
```

### **Example 3: Modifying Object Attributes**
```python
class Car:
    def __init__(self, brand):
        self.brand = brand

car1 = Car("Toyota")
car1.brand = "Honda"
print(car1.brand)
```

### **Example 4: Deleting Object Properties**
```python
class Car:
    def __init__(self, brand):
        self.brand = brand

car1 = Car("Toyota")
del car1.brand
```

### **Example 5: Using `__str__` Method**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

p1 = Person("Alice", 25)
print(p1)
```

---

## **Python Inheritance**
Inheritance allows a class to inherit properties and methods from another class.

### **Example 1: Creating a Derived Class**
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

d = Dog()
d.speak()
```

### **Example 2: Overriding Parent Class Methods**
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()
```

### **Example 3: Using `super()` to Call Parent Methods**
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Buddy", "Labrador")
print(d.name, d.breed)
```

### **Example 4: Multiple Inheritance**
```python
class Parent1:
    def method1(self):
        print("Method from Parent1")

class Parent2:
    def method2(self):
        print("Method from Parent2")

class Child(Parent1, Parent2):
    pass

c = Child()
c.method1()
c.method2()
```

### **Example 5: Multilevel Inheritance**
```python
class Grandparent:
    def method1(self):
        print("Grandparent method")

class Parent(Grandparent):
    def method2(self):
        print("Parent method")

class Child(Parent):
    def method3(self):
        print("Child method")

c = Child()
c.method1()
c.method2()
c.method3()
```

---

## **Python Iterators**
An iterator is an object that contains a sequence of values and can be iterated upon.

### **Example 1: Using an Iterator with a List**
```python
numbers = [1, 2, 3, 4]
it = iter(numbers)

print(next(it))
print(next(it))
```

### **Example 2: Creating a Custom Iterator Class**
```python
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

counter = Counter(1, 5)
for num in counter:
    print(num)
```

### **Example 3: Iterating Over a Tuple**
```python
fruits = ("apple", "banana", "cherry")
it = iter(fruits)

print(next(it))
print(next(it))
```

### **Example 4: Using `iter()` and `next()` on Strings**
```python
text = "hello"
it = iter(text)

print(next(it))
print(next(it))
```

### **Example 5: Using a Generator as an Iterator**
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)
```

---

## **Python Polymorphism**
Polymorphism allows different classes to share the same method name.

### **Example 1: Function with Different Objects**
```python
class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Bark"

def animal_sound(animal):
    print(animal.sound())

c = Cat()
d = Dog()

animal_sound(c)
animal_sound(d)
```

### **Example 2: Method Overriding**
```python
class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

sq = Square(4)
print(sq.area())
```

### **Example 3: Using `super()` with Overridden Methods**
```python
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        super().show()
        print("Child method")

c = Child()
c.show()
```

### **Example 4: Operator Overloading**
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
result = v1 + v2
print(result.x, result.y)
```

### **Example 5: Method Overloading with Default Values**
```python
class Math:
    def add(self, x, y=0):
        return x + y

m = Math()
print(m.add(2, 3))
print(m.add(5))
```

---

## **Python Scope**
Scope defines where variables can be accessed.

### **Example 1: Local and Global Scope**
```python
x = 10

def func():
    x = 5
    print(x)

func()
print(x)
```

### **Example 2: Using `global` Keyword**
```python
x = 10

def modify():
    global x
    x = 20

modify()
print(x)
```

### **Example 3: Function with Enclosing Scope (Closure)**
```python
def outer():
    x = 10
    def inner():
        print(x)
    inner()

outer()
```

### **Example 4: Using `nonlocal` Keyword**
```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)

outer()
```

### **Example 5: Nested Functions and Scope**
```python
def outer(x):
    def inner(y):
        return x + y
    return inner

closure = outer(5)
print(closure(3))
```

---

## **Python Modules**
Modules are reusable pieces of code stored in separate files.

### **Example 1: Importing a Module**
```python
import math
print(math.sqrt(16))
```

### **Example 2: Importing Specific Functions**
```python
from math import pow
print(pow(2, 3))
```

### **Example 3: Creating and Importing a Custom Module**
```python
# mymodule.py
def greet(name):
    return f"Hello, {name}"

# main.py
import mymodule
print(mymodule.greet("Alice"))
```

### **Example 4: Using `as` for Aliases**
```python
import math as m
print(m.factorial(5))
```

### **Example 5: Listing Available Functions in a Module**
```python
import math
print(dir(math))
```


### **1. Python Classes/Objects**
**Content:**
- What are classes and objects? (Blueprints for creating objects).
- Defining a class and creating objects.
- The `__init__` method (constructor).
- Instance variables and methods.
- The `self` keyword.

**Examples:**
1. Define a class `Car` with attributes `make` and `model`.
2. Create an object of the `Car` class and access its attributes.
3. Add a method `display_info()` to the `Car` class to print its details.
4. Use the `__init__` method to initialize object attributes.
5. Create multiple objects of the `Car` class and compare their attributes.

**Additional Examples:**
6. Add a method `update_model()` to change the model of a car.
7. Use the `__str__` method to define a string representation of an object.
8. Create a class `BankAccount` with methods `deposit()` and `withdraw()`.
9. Add a class variable to count the number of objects created.
10. Use the `__del__` method to define behavior when an object is deleted.

---

### **2. Python Inheritance**
**Content:**
- What is inheritance? (Creating a new class from an existing class).
- Syntax of inheritance in Python.
- The `super()` function.
- Method overriding.
- Types of inheritance (single, multiple, multilevel, hierarchical).

**Examples:**
1. Create a base class `Animal` and a derived class `Dog`.
2. Use the `super()` function to call the base class constructor.
3. Override a method in the derived class.
4. Create a class `Cat` that also inherits from `Animal`.
5. Demonstrate multiple inheritance with a class `Bird` that inherits from `Animal` and `Flyable`.

**Additional Examples:**
6. Create a multilevel inheritance chain (e.g., `Vehicle` → `Car` → `SportsCar`).
7. Use hierarchical inheritance with multiple derived classes (e.g., `Shape` → `Circle`, `Square`).
8. Override the `__str__` method in a derived class.
9. Use the `isinstance()` function to check if an object is an instance of a class.
10. Use the `issubclass()` function to check if a class is a subclass of another.

---

### **3. Python Iterators**
**Content:**
- What are iterators? (Objects that allow traversal through all elements of a collection).
- The `iter()` and `next()` functions.
- Creating custom iterators using `__iter__()` and `__next__()`.
- The `StopIteration` exception.
- Common use cases for iterators.

**Examples:**
1. Use `iter()` and `next()` to iterate over a list.
2. Create a custom iterator for a class `Counter`.
3. Use the `__iter__()` and `__next__()` methods in a class.
4. Handle the `StopIteration` exception in a custom iterator.
5. Use an iterator to generate Fibonacci numbers.

**Additional Examples:**
6. Create an iterator that iterates over a range of numbers in reverse order.
7. Use an iterator to iterate over a string character by character.
8. Create an iterator that generates an infinite sequence of even numbers.
9. Use an iterator to iterate over a dictionary's keys and values.
10. Combine multiple iterators using the `itertools` module.

---

### **4. Python Polymorphism**
**Content:**
- What is polymorphism? (Ability to use a single interface for different data types).
- Method overriding and operator overloading.
- Duck typing in Python.
- Polymorphism with functions and objects.
- Common use cases for polymorphism.

**Examples:**
1. Demonstrate method overriding with a base class `Shape` and derived classes `Circle` and `Square`.
2. Use operator overloading to define the `+` operator for a custom class.
3. Demonstrate duck typing with functions that accept different types of objects.
4. Use polymorphism to call the same method on different objects.
5. Override the `__len__()` method to define the length of an object.

**Additional Examples:**
6. Use polymorphism to implement a function that works with different types of collections.
7. Override the `__add__()` method to define custom addition for a class.
8. Demonstrate polymorphism with the `len()` function on different objects.
9. Use polymorphism to implement a generic `draw()` method for different shapes.
10. Override the `__eq__()` method to define custom equality for a class.

---

### **5. Python Scope**
**Content:**
- What is scope? (Visibility of variables within different parts of a program).
- Local vs global scope.
- The `global` keyword.
- Nonlocal scope in nested functions.
- Common scope-related errors and how to avoid them.

**Examples:**
1. Demonstrate local scope with a variable inside a function.
2. Use the `global` keyword to modify a global variable inside a function.
3. Demonstrate nonlocal scope in a nested function.
4. Create a function with a local variable that shadows a global variable.
5. Use the `globals()` and `locals()` functions to view variable scope.

**Additional Examples:**
6. Demonstrate scope in a class with instance variables and methods.
7. Use the `nonlocal` keyword to modify a variable in an enclosing function.
8. Create a closure with a nested function that captures local variables.
9. Demonstrate scope in a lambda function.
10. Use the `del` statement to delete a variable and demonstrate scope.

---

### **6. Python Modules**
**Content:**
- What are modules? (Files containing Python code that can be imported).
- Creating and importing modules.
- The `import` statement and its variations (`from ... import`, `import ... as`).
- Standard library modules (`math`, `random`, `datetime`, etc.).
- Installing and using third-party modules with `pip`.

**Examples:**
1. Create a module `mymodule.py` and import it into another script.
2. Use the `math` module to perform mathematical operations.
3. Use the `random` module to generate random numbers.
4. Use the `datetime` module to get the current date and time.
5. Install a third-party module using `pip` and import it.

**Additional Examples:**
6. Use the `os` module to interact with the operating system.
7. Use the `sys` module to access command-line arguments.
8. Create a package with multiple modules and import them.
9. Use the `__name__` attribute to check if a module is run as a script.
10. Use the `itertools` module to work with iterators and combinations.

---

### **Additional Examples for Each Section**

#### **Python Classes/Objects**
11. Create a class `Rectangle` with methods to calculate area and perimeter.
12. Use the `@property` decorator to define a read-only attribute.
13. Create a class `Student` with attributes `name`, `age`, and `grade`.
14. Use the `__dict__` attribute to view an object's attributes.
15. Create a class `Employee` with a class method to create objects from a CSV file.

#### **Python Inheritance**
11. Create a class `Person` with derived classes `Student` and `Teacher`.
12. Use multiple inheritance to create a class `HybridCar` that inherits from `Car` and `ElectricVehicle`.
13. Override the `__add__()` method in a derived class.
14. Use the `super()` function to call a method from the base class.
15. Create a class `Shape` with derived classes `Circle`, `Rectangle`, and `Triangle`.

#### **Python Iterators**
11. Create an iterator that generates prime numbers.
12. Use the `itertools.cycle()` function to create an infinite iterator.
13. Create an iterator that iterates over a list in chunks.
14. Use the `itertools.chain()` function to combine multiple iterators.
15. Create an iterator that generates a sequence of dates.

#### **Python Polymorphism**
11. Use polymorphism to implement a generic `area()` method for different shapes.
12. Override the `__str__()` method in multiple classes to provide custom string representations.
13. Use polymorphism to implement a generic `play()` method for different musical instruments.
14. Override the `__getitem__()` method to enable indexing for a custom class.
15. Use polymorphism to implement a generic `save()` method for different file formats.

#### **Python Scope**
11. Demonstrate scope in a class method with instance variables.
12. Use the `globals()` function to modify a global variable.
13. Create a nested function with a nonlocal variable and demonstrate its scope.
14. Use the `locals()` function to view local variables in a function.
15. Demonstrate scope in a lambda function with captured variables.

#### **Python Modules**
11. Use the `json` module to work with JSON data.
12. Use the `re` module to perform regular expression operations.
13. Create a custom module with utility functions and import it.
14. Use the `subprocess` module to run shell commands from Python.
15. Use the `collections` module to work with specialized container datatypes.

---

This structure should provide a solid foundation for the fifth part of your Python course. Let me know if you'd like further assistance!

Certainly! Below is the structured outline for the fifth part of your Python course, including content and **5 Python sample codes** for each title. I've also added **5 more examples** for each section to ensure comprehensive coverage.

---

### **1. Python Classes/Objects**
**Content:**
- What are classes and objects? (Blueprints for creating objects).
- Defining a class and creating objects.
- The `__init__` method (constructor).
- Instance variables and methods.
- The `self` keyword.

**Sample Codes:**
1. Define a class `Car` with attributes `make` and `model`.
   ```python
   class Car:
       def __init__(self, make, model):
           self.make = make
           self.model = model

   my_car = Car("Toyota", "Corolla")
   print(my_car.make, my_car.model)  # Output: Toyota Corolla
   ```
2. Add a method `display_info()` to the `Car` class to print its details.
   ```python
   class Car:
       def __init__(self, make, model):
           self.make = make
           self.model = model

       def display_info(self):
           print(f"{self.make} {self.model}")

   my_car = Car("Toyota", "Corolla")
   my_car.display_info()  # Output: Toyota Corolla
   ```
3. Use the `__str__` method to define a string representation of an object.
   ```python
   class Car:
       def __init__(self, make, model):
           self.make = make
           self.model = model

       def __str__(self):
           return f"{self.make} {self.model}"

   my_car = Car("Toyota", "Corolla")
   print(my_car)  # Output: Toyota Corolla
   ```
4. Create multiple objects of the `Car` class and compare their attributes.
   ```python
   car1 = Car("Toyota", "Corolla")
   car2 = Car("Honda", "Civic")
   print(car1.make == car2.make)  # Output: False
   ```
5. Add a class variable to count the number of objects created.
   ```python
   class Car:
       count = 0

       def __init__(self, make, model):
           self.make = make
           self.model = model
           Car.count += 1

   car1 = Car("Toyota", "Corolla")
   car2 = Car("Honda", "Civic")
   print("Total cars:", Car.count)  # Output: Total cars: 2
   ```

**Additional Examples:**
6. Use the `@property` decorator to define a read-only attribute.
   ```python
   class Car:
       def __init__(self, make, model):
           self.make = make
           self.model = model

       @property
       def full_name(self):
           return f"{self.make} {self.model}"

   my_car = Car("Toyota", "Corolla")
   print(my_car.full_name)  # Output: Toyota Corolla
   ```
7. Create a class `Student` with attributes `name`, `age`, and `grade`.
   ```python
   class Student:
       def __init__(self, name, age, grade):
           self.name = name
           self.age = age
           self.grade = grade

   student = Student("John", 15, "10th")
   print(student.name, student.age, student.grade)  # Output: John 15 10th
   ```
8. Use the `__dict__` attribute to view an object's attributes.
   ```python
   my_car = Car("Toyota", "Corolla")
   print(my_car.__dict__)  # Output: {'make': 'Toyota', 'model': 'Corolla'}
   ```
9. Create a class `Employee` with a class method to create objects from a CSV file.
   ```python
   class Employee:
       def __init__(self, name, age):
           self.name = name
           self.age = age

       @classmethod
       def from_csv(cls, csv_string):
           name, age = csv_string.split(",")
           return cls(name, int(age))

   emp = Employee.from_csv("John,30")
   print(emp.name, emp.age)  # Output: John 30
   ```
10. Use the `__del__` method to define behavior when an object is deleted.
    ```python
    class Car:
        def __init__(self, make, model):
            self.make = make
            self.model = model

        def __del__(self):
            print(f"{self.make} {self.model} is deleted")

    my_car = Car("Toyota", "Corolla")
    del my_car  # Output: Toyota Corolla is deleted
    ```

---

### **2. Python Inheritance**
**Content:**
- What is inheritance? (Creating a new class from an existing class).
- Syntax of inheritance in Python.
- The `super()` function.
- Method overriding.
- Types of inheritance (single, multiple, multilevel, hierarchical).

**Sample Codes:**
1. Create a base class `Animal` and a derived class `Dog`.
   ```python
   class Animal:
       def speak(self):
           print("Animal speaks")

   class Dog(Animal):
       def bark(self):
           print("Dog barks")

   my_dog = Dog()
   my_dog.speak()  # Output: Animal speaks
   my_dog.bark()   # Output: Dog barks
   ```
2. Use the `super()` function to call the base class constructor.
   ```python
   class Animal:
       def __init__(self, name):
           self.name = name

   class Dog(Animal):
       def __init__(self, name, breed):
           super().__init__(name)
           self.breed = breed

   my_dog = Dog("Buddy", "Golden Retriever")
   print(my_dog.name, my_dog.breed)  # Output: Buddy Golden Retriever
   ```
3. Override a method in the derived class.
   ```python
   class Animal:
       def speak(self):
           print("Animal speaks")

   class Dog(Animal):
       def speak(self):
           print("Dog barks")

   my_dog = Dog()
   my_dog.speak()  # Output: Dog barks
   ```
4. Create a class `Cat` that also inherits from `Animal`.
   ```python
   class Cat(Animal):
       def meow(self):
           print("Cat meows")

   my_cat = Cat()
   my_cat.speak()  # Output: Animal speaks
   my_cat.meow()   # Output: Cat meows
   ```
5. Demonstrate multiple inheritance with a class `Bird` that inherits from `Animal` and `Flyable`.
   ```python
   class Flyable:
       def fly(self):
           print("I can fly")

   class Bird(Animal, Flyable):
       pass

   my_bird = Bird("Sparrow")
   my_bird.speak()  # Output: Animal speaks
   my_bird.fly()    # Output: I can fly
   ```

**Additional Examples:**
6. Create a multilevel inheritance chain (e.g., `Vehicle` → `Car` → `SportsCar`).
   ```python
   class Vehicle:
       def move(self):
           print("Vehicle is moving")

   class Car(Vehicle):
       def drive(self):
           print("Car is driving")

   class SportsCar(Car):
       def race(self):
           print("Sports car is racing")

   my_sports_car = SportsCar()
   my_sports_car.move()  # Output: Vehicle is moving
   my_sports_car.drive() # Output: Car is driving
   my_sports_car.race()  # Output: Sports car is racing
   ```
7. Use hierarchical inheritance with multiple derived classes (e.g., `Shape` → `Circle`, `Square`).
   ```python
   class Shape:
       def area(self):
           pass

   class Circle(Shape):
       def __init__(self, radius):
           self.radius = radius

       def area(self):
           return 3.14 * self.radius**2

   class Square(Shape):
       def __init__(self, side):
           self.side = side

       def area(self):
           return self.side**2

   my_circle = Circle(5)
   print("Circle area:", my_circle.area())  # Output: Circle area: 78.5
   my_square = Square(4)
   print("Square area:", my_square.area())  # Output: Square area: 16
   ```
8. Override the `__str__` method in a derived class.
   ```python
   class Animal:
       def __init__(self, name):
           self.name = name

       def __str__(self):
           return f"Animal: {self.name}"

   class Dog(Animal):
       def __str__(self):
           return f"Dog: {self.name}"

   my_dog = Dog("Buddy")
   print(my_dog)  # Output: Dog: Buddy
   ```
9. Use the `isinstance()` function to check if an object is an instance of a class.
   ```python
   my_dog = Dog("Buddy")
   print(isinstance(my_dog, Animal))  # Output: True
   ```
10. Use the `issubclass()` function to check if a class is a subclass of another.
    ```python
    print(issubclass(Dog, Animal))  # Output: True
    ```

---

### **3. Python Iterators**
**Content:**
- What are iterators? (Objects that allow traversal through all elements of a collection).
- The `iter()` and `next()` functions.
- Creating custom iterators using `__iter__()` and `__next__()`.
- The `StopIteration` exception.
- Common use cases for iterators.

**Sample Codes:**
1. Use `iter()` and `next()` to iterate over a list.
   ```python
   my_list = [1, 2, 3]
   my_iter = iter(my_list)
   print(next(my_iter))  # Output: 1
   print(next(my_iter))  # Output: 2
   ```
2. Create a custom iterator for a class `Counter`.
   ```python
   class Counter:
       def __init__(self, start, end):
           self.current = start
           self.end = end

       def __iter__(self):
           return self

       def __next__(self):
           if self.current >= self.end:
               raise StopIteration
           self.current += 1
           return self.current - 1

   for num in Counter(1, 5):
       print(num)  # Output: 1 2 3 4
   ```
3. Use the `__iter__()` and `__next__()` methods in a class.
   ```python
   class MyRange:
       def __init__(self, start, end):
           self.start = start
           self.end = end

       def __iter__(self):
           return self

       def __next__(self):
           if self.start >= self.end:
               raise StopIteration
           self.start += 1
           return self.start - 1

   for num in MyRange(1, 5):
       print(num)  # Output: 1 2 3 4
   ```
4. Handle the `StopIteration` exception in a custom iterator.
   ```python
   my_iter = iter([1, 2, 3])
   while True:
       try:
           print(next(my_iter))
       except StopIteration:
           break
   # Output: 1 2 3
   ```
5. Use an iterator to generate Fibonacci numbers.
   ```python
   class Fibonacci:
       def __init__(self, limit):
           self.limit = limit
           self.a, self.b = 0, 1

       def __iter__(self):
           return self

       def __next__(self):
           if self.a > self.limit:
               raise StopIteration
           result = self.a
           self.a, self.b = self.b, self.a + self.b
           return result

   for num in Fibonacci(10):
       print(num)  # Output: 0 1 1 2 3 5 8
   ```

**Additional Examples:**
6. Create an iterator that iterates over a range of numbers in reverse order.
   ```python
   class ReverseRange:
       def __init__(self, start, end):
           self.start = start
           self.end = end

       def __iter__(self):
           return self

       def __next__(self):
           if self.start <= self.end:
               raise StopIteration
           self.start -= 1
           return self.start + 1

   for num in ReverseRange(5, 1):
       print(num)  # Output: 5 4 3 2
   ```
7. Use an iterator to iterate over a string character by character.
   ```python
   my_string = "hello"
   my_iter = iter(my_string)
   for char in my_iter:
       print(char)  # Output: h e l l o
   ```
8. Create an iterator that generates an infinite sequence of even numbers.
   ```python
   class EvenNumbers:
       def __init__(self):
           self.num = 0

       def __iter__(self):
           return self

       def __next__(self):
           self.num += 2
           return self.num

   even_iter = EvenNumbers()
   for _ in range(5):
       print(next(even_iter))  # Output: 2 4 6 8 10
   ```
9. Use an iterator to iterate over a dictionary's keys and values.
   ```python
   my_dict = {"a": 1, "b": 2, "c": 3}
   my_iter = iter(my_dict.items())
   for key, value in my_iter:
       print(key, value)  # Output: a 1 b 2 c 3
   ```
10. Combine multiple iterators using the `itertools` module.
    ```python
    import itertools
    iter1 = iter([1, 2, 3])
    iter2 = iter([4, 5, 6])
    combined = itertools.chain(iter1, iter2)
    for num in combined:
        print(num)  # Output: 1 2 3 4 5 6
    ```

---

### **4. Python Polymorphism**
**Content:**
- What is polymorphism? (Ability to use a single interface for different data types).
- Method overriding and operator overloading.
- Duck typing in Python.
- Polymorphism with functions and objects.
- Common use cases for polymorphism.

**Sample Codes:**
1. Demonstrate method overriding with a base class `Shape` and derived classes `Circle` and `Square`.
   ```python
   class Shape:
       def area(self):
           pass

   class Circle(Shape):
       def __init__(self, radius):
           self.radius = radius

       def area(self):
           return 3.14 * self.radius**2

   class Square(Shape):
       def __init__(self, side):
           self.side = side

       def area(self):
           return self.side**2

   shapes = [Circle(5), Square(4)]
   for shape in shapes:
       print(shape.area())  # Output: 78.5 16
   ```
2. Use operator overloading to define the `+` operator for a custom class.
   ```python
   class Point:
       def __init__(self, x, y):
           self.x = x
           self.y = y

       def __add__(self, other):
           return Point(self.x + other.x, self.y + other.y)

   p1 = Point(1, 2)
   p2 = Point(3, 4)
   p3 = p1 + p2
   print(p3.x, p3.y)  # Output: 4 6
   ```
3. Demonstrate duck typing with functions that accept different types of objects.
   ```python
   def print_area(shape):
       print(shape.area())

   class Circle:
       def __init__(self, radius):
           self.radius = radius

       def area(self):
           return 3.14 * self.radius**2

   class Square:
       def __init__(self, side):
           self.side = side

       def area(self):
           return self.side**2

   print_area(Circle(5))  # Output: 78.5
   print_area(Square(4))  # Output: 16
   ```
4. Use polymorphism to call the same method on different objects.
   ```python
   class Dog:
       def speak(self):
           print("Woof!")

   class Cat:
       def speak(self):
           print("Meow!")

   animals = [Dog(), Cat()]
   for animal in animals:
       animal.speak()  # Output: Woof! Meow!
   ```
5. Override the `__len__()` method to define the length of an object.
   ```python
   class MyList:
       def __init__(self, items):
           self.items = items

       def __len__(self):
           return len(self.items)

   my_list = MyList([1, 2, 3, 4])
   print(len(my_list))  # Output: 4
   ```

**Additional Examples:**
6. Use polymorphism to implement a function that works with different types of collections.
   ```python
   def print_length(collection):
       print(len(collection))

   print_length([1, 2, 3])  # Output: 3
   print_length("hello")     # Output: 5
   ```
7. Override the `__eq__()` method to define custom equality for a class.
   ```python
   class Point:
       def __init__(self, x, y):
           self.x = x
           self.y = y

       def __eq__(self, other):
           return self.x == other.x and self.y == other.y

   p1 = Point(1, 2)
   p2 = Point(1, 2)
   print(p1 == p2)  # Output: True
   ```
8. Use polymorphism to implement a generic `draw()` method for different shapes.
   ```python
   class Circle:
       def draw(self):
           print("Drawing a circle")

   class Square:
       def draw(self):
           print("Drawing a square")

   shapes = [Circle(), Square()]
   for shape in shapes:
       shape.draw()  # Output: Drawing a circle Drawing a square
   ```
9. Override the `__getitem__()` method to enable indexing for a custom class.
   ```python
   class MyList:
       def __init__(self, items):
           self.items = items

       def __getitem__(self, index):
           return self.items[index]

   my_list = MyList([1, 2, 3, 4])
   print(my_list[2])  # Output: 3
   ```
10. Use polymorphism to implement a generic `save()` method for different file formats.
    ```python
    class TextFile:
        def save(self):
            print("Saving as text file")

    class PDFFile:
        def save(self):
            print("Saving as PDF file")

    files = [TextFile(), PDFFile()]
    for file in files:
        file.save()  # Output: Saving as text file Saving as PDF file
    ```

---

### **5. Python Scope**
**Content:**
- What is scope? (Visibility of variables within different parts of a program).
- Local vs global scope.
- The `global` keyword.
- Nonlocal scope in nested functions.
- Common scope-related errors and how to avoid them.

**Sample Codes:**
1. Demonstrate local scope with a variable inside a function.
   ```python
   def my_function():
       x = 10  # Local variable
       print(x)

   my_function()  # Output: 10
   # print(x)  # Error: x is not defined outside the function
   ```
2. Use the `global` keyword to modify a global variable inside a function.
   ```python
   x = 5

   def my_function():
       global x
       x = 10

   my_function()
   print(x)  # Output: 10
   ```
3. Demonstrate nonlocal scope in a nested function.
   ```python
   def outer():
       x = 10

       def inner():
           nonlocal x
           x = 20

       inner()
       print(x)  # Output: 20

   outer()
   ```
4. Create a function with a local variable that shadows a global variable.
   ```python
   x = 5

   def my_function():
       x = 10  # Local variable shadows the global variable
       print(x)

   my_function()  # Output: 10
   print(x)       # Output: 5
   ```
5. Use the `globals()` and `locals()` functions to view variable scope.
   ```python
   x = 5

   def my_function():
       y = 10
       print("Globals:", globals())
       print("Locals:", locals())

   my_function()
   ```

**Additional Examples:**
6. Demonstrate scope in a class with instance variables and methods.
   ```python
   class MyClass:
       def __init__(self, x):
           self.x = x  # Instance variable

       def print_x(self):
           print(self.x)

   obj = MyClass(10)
   obj.print_x()  # Output: 10
   ```
7. Use the `nonlocal` keyword to modify a variable in an enclosing function.
   ```python
   def outer():
       x = 10

       def inner():
           nonlocal x
           x = 20

       inner()
       print(x)  # Output: 20

   outer()
   ```
8. Create a closure with a nested function that captures local variables.
   ```python
   def outer():
       x = 10

       def inner():
           print(x)

       return inner

   my_func = outer()
   my_func()  # Output: 10
   ```
9. Demonstrate scope in a lambda function.
   ```python
   x = 5
   my_lambda = lambda: x + 10
   print(my_lambda())  # Output: 15
   ```
10. Use the `del` statement to delete a variable and demonstrate scope.
    ```python
    x = 10
    print(x)  # Output: 10
    del x
    # print(x)  # Error: x is not defined
    ```

---

### **6. Python Modules**
**Content:**
- What are modules? (Files containing Python code that can be imported).
- Creating and importing modules.
- The `import` statement and its variations (`from ... import`, `import ... as`).
- Standard library modules (`math`, `random`, `datetime`, etc.).
- Installing and using third-party modules with `pip`.

**Sample Codes:**
1. Create a module `mymodule.py` and import it into another script.
   ```python
   # mymodule.py
   def greet(name):
       print(f"Hello, {name}!")

   # main.py
   import mymodule
   mymodule.greet("John")  # Output: Hello, John!
   ```
2. Use the `math` module to perform mathematical operations.
   ```python
   import math
   print(math.sqrt(16))  # Output: 4.0
   ```
3. Use the `random` module to generate random numbers.
   ```python
   import random
   print(random.randint(1, 10))  # Output: Random number between 1 and 10
   ```
4. Use the `datetime` module to get the current date and time.
   ```python
   from datetime import datetime
   print(datetime.now())  # Output: Current date and time
   ```
5. Install a third-party module using `pip` and import it.
   ```bash
   pip install numpy
   ```
   ```python
   import numpy as np
   print(np.array([1, 2, 3]))  # Output: [1 2 3]
   ```

**Additional Examples:**
6. Use the `os` module to interact with the operating system.
   ```python
   import os
   print(os.getcwd())  # Output: Current working directory
   ```
7. Use the `sys` module to access command-line arguments.
   ```python
   import sys
   print(sys.argv)  # Output: List of command-line arguments
   ```
8. Create a package with multiple modules and import them.
   ```python
   # mypackage/mymodule.py
   def greet(name):
       print(f"Hello, {name}!")

   # main.py
   from mypackage import mymodule
   mymodule.greet("John")  # Output: Hello, John!
   ```
9. Use the `__name__` attribute to check if a module is run as a script.
   ```python
   # mymodule.py
   if __name__ == "__main__":
       print("Running as a script")
   else:
       print("Imported as a module")
   ```
10. Use the `itertools` module to work with iterators and combinations.
    ```python
    import itertools
    for combination in itertools.combinations([1, 2, 3], 2):
        print(combination)  # Output: (1, 2) (1, 3) (2, 3)
    ```

---

---

This structured content provides clear explanations and hands-on examples. Let me know if you need modifications or additional topics! 🚀

