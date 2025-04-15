
### Python courses


#### Fouth Part
Python While Loops

Python For Loops

Python Functions

Python Lambda

Python Arrays

Here’s the structured content for the fourth part of your Python course:

---

## **Python While Loops**
The `while` loop executes a block of code as long as a condition is `True`.

### **Example 1: Basic While Loop**
```python
x = 1
while x <= 5:
    print(x)
    x += 1
```

### **Example 2: Using Break Statement**
```python
x = 1
while x <= 5:
    if x == 3:
        break
    print(x)
    x += 1
```

### **Example 3: Using Continue Statement**
```python
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)
```

### **Example 4: Using Else with While**
```python
x = 1
while x < 5:
    print(x)
    x += 1
else:
    print("Loop completed")
```

### **Example 5: Infinite Loop (Use with Caution)**
```python
x = 1
while True:
    print(x)
    x += 1
    if x > 5:
        break
```

---

## **Python For Loops**
The `for` loop iterates over a sequence.

### **Example 1: Looping Through a List**
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### **Example 2: Looping Through a Range of Numbers**
```python
for i in range(1, 6):
    print(i)
```

### **Example 3: Using Break Statement**
```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

### **Example 4: Using Continue Statement**
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

### **Example 5: Looping Through a Dictionary**
```python
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(key, ":", value)
```

---

## **Python Functions**
Functions are reusable blocks of code.

### **Example 1: Defining and Calling a Function**
```python
def greet():
    print("Hello, world!")

greet()
```

### **Example 2: Function with Parameters**
```python
def add(x, y):
    return x + y

print(add(5, 3))
```

### **Example 3: Function with Default Parameters**
```python
def greet(name="Guest"):
    print("Hello,", name)

greet()
greet("Alice")
```

### **Example 4: Function Returning Multiple Values**
```python
def get_coordinates():
    return 10, 20

x, y = get_coordinates()
print(x, y)
```

### **Example 5: Recursive Function**
```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

---

## **Python Lambda**
Lambda functions are anonymous, one-liner functions.

### **Example 1: Basic Lambda Function**
```python
square = lambda x: x ** 2
print(square(5))
```

### **Example 2: Lambda with Multiple Arguments**
```python
add = lambda x, y: x + y
print(add(3, 7))
```

### **Example 3: Using Lambda in `map()`**
```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)
```

### **Example 4: Using Lambda in `filter()`**
```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
```

### **Example 5: Using Lambda in `sorted()`**
```python
students = [("Alice", 25), ("Bob", 22), ("Charlie", 23)]
students.sort(key=lambda x: x[1])
print(students)
```

---

## **Python Arrays**
Arrays store multiple values of the same type.

### **Example 1: Creating an Array (Using `array` Module)**
```python
import array
numbers = array.array('i', [1, 2, 3, 4])
print(numbers)
```

### **Example 2: Accessing Array Elements**
```python
print(numbers[0])  # First element
print(numbers[-1])  # Last element
```

### **Example 3: Modifying an Array**
```python
numbers[1] = 10
print(numbers)
```

### **Example 4: Adding Elements to an Array**
```python
numbers.append(5)
print(numbers)
```

### **Example 5: Removing Elements from an Array**
```python
numbers.remove(3)
print(numbers)
```
### **1. Python While Loops**
**Content:**
- What are `while` loops? (Repeated execution of a block of code while a condition is true).
- Syntax of a `while` loop.
- Using `break` and `continue` in `while` loops.
- Infinite loops and how to avoid them.
- Common use cases for `while` loops.

**Examples:**
1. Write a `while` loop to print numbers from 1 to 5.
2. Use a `while` loop to calculate the sum of numbers from 1 to 10.
3. Use `break` to exit a `while` loop when a condition is met.
4. Use `continue` to skip an iteration in a `while` loop.
5. Create an infinite loop and use `break` to exit it.

**Additional Examples:**
6. Use a `while` loop to find the factorial of a number.
7. Use a `while` loop to repeatedly prompt the user for input until they enter "quit".
8. Use a `while` loop to reverse a string.
9. Use a `while` loop to find the first 10 even numbers.
10. Use a `while` loop to simulate a simple guessing game.

---

### **2. Python For Loops**
**Content:**
- What are `for` loops? (Iterating over a sequence of items).
- Syntax of a `for` loop.
- Using `range()` in `for` loops.
- Nested `for` loops.
- Common use cases for `for` loops.

**Examples:**
1. Write a `for` loop to print numbers from 1 to 5.
2. Use a `for` loop to iterate over a list of strings.
3. Use `range()` to generate a sequence of numbers in a `for` loop.
4. Use a nested `for` loop to create a multiplication table.
5. Use a `for` loop to calculate the sum of numbers in a list.

**Additional Examples:**
6. Use a `for` loop to find the largest number in a list.
7. Use a `for` loop to count the occurrences of a specific item in a list.
8. Use a `for` loop to iterate over a dictionary and print key-value pairs.
9. Use a `for` loop to flatten a nested list.
10. Use a `for` loop to generate a list of squares using list comprehension.

---

### **3. Python Functions**
**Content:**
- What are functions? (Reusable blocks of code).
- Defining and calling functions.
- Function parameters and return values.
- Default arguments and keyword arguments.
- Variable scope (local vs global variables).

**Examples:**
1. Define a function to greet a user by name.
2. Write a function to add two numbers and return the result.
3. Use default arguments in a function.
4. Use keyword arguments to call a function.
5. Define a function with a local variable and demonstrate its scope.

**Additional Examples:**
6. Write a function to calculate the factorial of a number.
7. Write a function to check if a string is a palindrome.
8. Use a function to find the maximum of three numbers.
9. Write a function to generate Fibonacci numbers.
10. Use a function to count the occurrences of each character in a string.

---

### **4. Python Lambda**
**Content:**
- What are lambda functions? (Anonymous, single-expression functions).
- Syntax of a lambda function.
- Using lambda functions with `map()`, `filter()`, and `reduce()`.
- Common use cases for lambda functions.

**Examples:**
1. Write a lambda function to add two numbers.
2. Use a lambda function to square a number.
3. Use `map()` with a lambda function to double each item in a list.
4. Use `filter()` with a lambda function to filter even numbers from a list.
5. Use `reduce()` with a lambda function to find the product of numbers in a list.

**Additional Examples:**
6. Use a lambda function to sort a list of tuples by the second element.
7. Use a lambda function to find the maximum number in a list.
8. Use a lambda function to concatenate two strings.
9. Use a lambda function to check if a number is even.
10. Use a lambda function to sort a list of strings by length.

---

### **5. Python Arrays**
**Content:**
- What are arrays? (Containers for storing multiple values of the same type).
- Differences between arrays and lists.
- Using the `array` module to create and manipulate arrays.
- Common array operations (slicing, appending, etc.).
- When to use arrays instead of lists.

**Examples:**
1. Create an array of integers using the `array` module.
2. Append an item to an array using `append()`.
3. Access elements of an array using indexing.
4. Slice an array to extract a subarray.
5. Convert an array to a list using `tolist()`.

**Additional Examples:**
6. Use `extend()` to add multiple items to an array.
7. Use `insert()` to add an item at a specific position in an array.
8. Remove an item from an array using `remove()`.
9. Reverse an array using `reverse()`.
10. Use `count()` to count the occurrences of an item in an array.

---

### **Additional Examples for Each Section**

#### **Python While Loops**
11. Use a `while` loop to find the smallest number divisible by 7 and 5.
12. Use a `while` loop to simulate a countdown timer.
13. Use a `while` loop to find the sum of digits of a number.
14. Use a `while` loop to generate the Fibonacci sequence up to a certain limit.
15. Use a `while` loop to repeatedly prompt the user for a valid input.

#### **Python For Loops**
11. Use a `for` loop to iterate over a string and count vowels.
12. Use a `for` loop to generate a list of prime numbers.
13. Use a `for` loop to iterate over a list of dictionaries and print specific values.
14. Use a `for` loop to create a list of tuples from two lists.
15. Use a `for` loop to iterate over a file line by line.

#### **Python Functions**
11. Write a function to calculate the area of a circle.
12. Write a function to check if a number is prime.
13. Write a function to reverse a string.
14. Write a function to find the GCD of two numbers.
15. Write a function to generate a list of random numbers.

#### **Python Lambda**
11. Use a lambda function to sort a list of strings alphabetically.
12. Use a lambda function to find the square root of a number.
13. Use a lambda function to filter out negative numbers from a list.
14. Use a lambda function to sort a list of dictionaries by a specific key.
15. Use a lambda function to find the average of a list of numbers.

#### **Python Arrays**
11. Use `fromlist()` to add a list of items to an array.
12. Use `frombytes()` and `tobytes()` to convert an array to bytes and vice versa.
13. Use `buffer_info()` to get the memory address and length of an array.
14. Use `itemsize` to get the size of a single array element in bytes.
15. Use `array` to store and manipulate a large sequence of numbers efficiently.

---

This structure should provide a solid foundation for the fourth part of your Python course. Let me know if you'd like further assistance!

Certainly! Below is the structured outline for the fourth part of your Python course, including content and **5 Python sample codes** for each title. I've also added **5 more examples** for each section to ensure comprehensive coverage.

---

### **1. Python While Loops**
**Content:**
- What are `while` loops? (Repeated execution of a block of code while a condition is true).
- Syntax of a `while` loop.
- Using `break` and `continue` in `while` loops.
- Infinite loops and how to avoid them.
- Common use cases for `while` loops.

**Sample Codes:**
1. Write a `while` loop to print numbers from 1 to 5.
   ```python
   i = 1
   while i <= 5:
       print(i)
       i += 1
   ```
2. Use a `while` loop to calculate the sum of numbers from 1 to 10.
   ```python
   total = 0
   i = 1
   while i <= 10:
       total += i
       i += 1
   print("Sum:", total)
   ```
3. Use `break` to exit a `while` loop when a condition is met.
   ```python
   i = 1
   while True:
       if i > 5:
           break
       print(i)
       i += 1
   ```
4. Use `continue` to skip an iteration in a `while` loop.
   ```python
   i = 0
   while i < 5:
       i += 1
       if i == 3:
           continue
       print(i)
   ```
5. Create an infinite loop and use `break` to exit it.
   ```python
   while True:
       user_input = input("Enter 'quit' to exit: ")
       if user_input == "quit":
           break
   ```

**Additional Examples:**
6. Use a `while` loop to find the factorial of a number.
   ```python
   num = 5
   factorial = 1
   while num > 0:
       factorial *= num
       num -= 1
   print("Factorial:", factorial)
   ```
7. Use a `while` loop to repeatedly prompt the user for input until they enter "quit".
   ```python
   while True:
       user_input = input("Enter something (or 'quit' to exit): ")
       if user_input == "quit":
           break
       print("You entered:", user_input)
   ```
8. Use a `while` loop to reverse a string.
   ```python
   text = "hello"
   reversed_text = ""
   i = len(text) - 1
   while i >= 0:
       reversed_text += text[i]
       i -= 1
   print("Reversed:", reversed_text)
   ```
9. Use a `while` loop to find the first 10 even numbers.
   ```python
   count = 0
   num = 0
   while count < 10:
       if num % 2 == 0:
           print(num)
           count += 1
       num += 1
   ```
10. Use a `while` loop to simulate a simple guessing game.
    ```python
    secret_number = 7
    while True:
        guess = int(input("Guess the number (1-10): "))
        if guess == secret_number:
            print("You guessed it!")
            break
        else:
            print("Try again!")
    ```

---

### **2. Python For Loops**
**Content:**
- What are `for` loops? (Iterating over a sequence of items).
- Syntax of a `for` loop.
- Using `range()` in `for` loops.
- Nested `for` loops.
- Common use cases for `for` loops.

**Sample Codes:**
1. Write a `for` loop to print numbers from 1 to 5.
   ```python
   for i in range(1, 6):
       print(i)
   ```
2. Use a `for` loop to iterate over a list of strings.
   ```python
   fruits = ["apple", "banana", "cherry"]
   for fruit in fruits:
       print(fruit)
   ```
3. Use `range()` to generate a sequence of numbers in a `for` loop.
   ```python
   for i in range(5):
       print(i)
   ```
4. Use a nested `for` loop to create a multiplication table.
   ```python
   for i in range(1, 6):
       for j in range(1, 6):
           print(f"{i} * {j} = {i * j}")
   ```
5. Use a `for` loop to calculate the sum of numbers in a list.
   ```python
   numbers = [1, 2, 3, 4, 5]
   total = 0
   for num in numbers:
       total += num
   print("Sum:", total)
   ```

**Additional Examples:**
6. Use a `for` loop to find the largest number in a list.
   ```python
   numbers = [10, 20, 5, 30, 15]
   max_num = numbers[0]
   for num in numbers:
       if num > max_num:
           max_num = num
   print("Max:", max_num)
   ```
7. Use a `for` loop to count the occurrences of a specific item in a list.
   ```python
   fruits = ["apple", "banana", "apple", "cherry", "apple"]
   count = 0
   for fruit in fruits:
       if fruit == "apple":
           count += 1
   print("Apples:", count)
   ```
8. Use a `for` loop to iterate over a dictionary and print key-value pairs.
   ```python
   my_dict = {"name": "John", "age": 30, "city": "New York"}
   for key, value in my_dict.items():
       print(f"{key}: {value}")
   ```
9. Use a `for` loop to flatten a nested list.
   ```python
   nested_list = [[1, 2], [3, 4], [5, 6]]
   flat_list = []
   for sublist in nested_list:
       for item in sublist:
           flat_list.append(item)
   print("Flat list:", flat_list)
   ```
10. Use a `for` loop to generate a list of squares using list comprehension.
    ```python
    squares = [x**2 for x in range(5)]
    print("Squares:", squares)
    ```

---

### **3. Python Functions**
**Content:**
- What are functions? (Reusable blocks of code).
- Defining and calling functions.
- Function parameters and return values.
- Default arguments and keyword arguments.
- Variable scope (local vs global variables).

**Sample Codes:**
1. Define a function to greet a user by name.
   ```python
   def greet(name):
       print(f"Hello, {name}!")
   greet("John")
   ```
2. Write a function to add two numbers and return the result.
   ```python
   def add(a, b):
       return a + b
   result = add(5, 3)
   print("Sum:", result)
   ```
3. Use default arguments in a function.
   ```python
   def greet(name="Guest"):
       print(f"Hello, {name}!")
   greet()
   greet("Alice")
   ```
4. Use keyword arguments to call a function.
   ```python
   def greet(name, age):
       print(f"Hello, {name}! You are {age} years old.")
   greet(age=30, name="John")
   ```
5. Define a function with a local variable and demonstrate its scope.
   ```python
   def my_function():
       x = 10  # Local variable
       print(x)
   my_function()
   # print(x)  # Error: x is not defined outside the function
   ```

**Additional Examples:**
6. Write a function to calculate the factorial of a number.
   ```python
   def factorial(n):
       if n == 0:
           return 1
       else:
           return n * factorial(n - 1)
   print("Factorial of 5:", factorial(5))
   ```
7. Write a function to check if a string is a palindrome.
   ```python
   def is_palindrome(s):
       return s == s[::-1]
   print(is_palindrome("madam"))  # Output: True
   ```
8. Use a function to find the maximum of three numbers.
   ```python
   def max_of_three(a, b, c):
       return max(a, b, c)
   print("Max:", max_of_three(10, 20, 15))
   ```
9. Write a function to generate Fibonacci numbers.
   ```python
   def fibonacci(n):
       a, b = 0, 1
       for _ in range(n):
           print(a, end=" ")
           a, b = b, a + b
   fibonacci(10)
   ```
10. Use a function to count the occurrences of each character in a string.
    ```python
    def count_chars(s):
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        return char_count
    print(count_chars("hello"))
    ```

---

### **4. Python Lambda**
**Content:**
- What are lambda functions? (Anonymous, single-expression functions).
- Syntax of a lambda function.
- Using lambda functions with `map()`, `filter()`, and `reduce()`.
- Common use cases for lambda functions.

**Sample Codes:**
1. Write a lambda function to add two numbers.
   ```python
   add = lambda a, b: a + b
   print("Sum:", add(5, 3))
   ```
2. Use a lambda function to square a number.
   ```python
   square = lambda x: x**2
   print("Square:", square(5))
   ```
3. Use `map()` with a lambda function to double each item in a list.
   ```python
   numbers = [1, 2, 3, 4, 5]
   doubled = list(map(lambda x: x * 2, numbers))
   print("Doubled:", doubled)
   ```
4. Use `filter()` with a lambda function to filter even numbers from a list.
   ```python
   numbers = [1, 2, 3, 4, 5]
   evens = list(filter(lambda x: x % 2 == 0, numbers))
   print("Evens:", evens)
   ```
5. Use `reduce()` with a lambda function to find the product of numbers in a list.
   ```python
   from functools import reduce
   numbers = [1, 2, 3, 4, 5]
   product = reduce(lambda x, y: x * y, numbers)
   print("Product:", product)
   ```

**Additional Examples:**
6. Use a lambda function to sort a list of tuples by the second element.
   ```python
   tuples = [(1, 2), (3, 1), (5, 4)]
   sorted_tuples = sorted(tuples, key=lambda x: x[1])
   print("Sorted:", sorted_tuples)
   ```
7. Use a lambda function to find the maximum number in a list.
   ```python
   numbers = [10, 20, 5, 30, 15]
   max_num = reduce(lambda x, y: x if x > y else y, numbers)
   print("Max:", max_num)
   ```
8. Use a lambda function to concatenate two strings.
   ```python
   concat = lambda s1, s2: s1 + s2
   print("Concatenated:", concat("Hello", "World"))
   ```
9. Use a lambda function to check if a number is even.
   ```python
   is_even = lambda x: x % 2 == 0
   print("Is 4 even?", is_even(4))
   ```
10. Use a lambda function to sort a list of strings by length.
    ```python
    fruits = ["apple", "banana", "cherry", "date"]
    sorted_fruits = sorted(fruits, key=lambda x: len(x))
    print("Sorted by length:", sorted_fruits)
    ```

---

### **5. Python Arrays**
**Content:**
- What are arrays? (Containers for storing multiple values of the same type).
- Differences between arrays and lists.
- Using the `array` module to create and manipulate arrays.
- Common array operations (slicing, appending, etc.).
- When to use arrays instead of lists.

**Sample Codes:**
1. Create an array of integers using the `array` module.
   ```python
   import array
   my_array = array.array('i', [1, 2, 3, 4, 5])
   print(my_array)
   ```
2. Append an item to an array using `append()`.
   ```python
   my_array.append(6)
   print(my_array)
   ```
3. Access elements of an array using indexing.
   ```python
   print(my_array[0])  # Output: 1
   ```
4. Slice an array to extract a subarray.
   ```python
   print(my_array[1:4])  # Output: array('i', [2, 3, 4])
   ```
5. Convert an array to a list using `tolist()`.
   ```python
   my_list = my_array.tolist()
   print(my_list)
   ```

**Additional Examples:**
6. Use `extend()` to add multiple items to an array.
   ```python
   my_array.extend([7, 8, 9])
   print(my_array)
   ```
7. Use `insert()` to add an item at a specific position in an array.
   ```python
   my_array.insert(2, 10)
   print(my_array)
   ```
8. Remove an item from an array using `remove()`.
   ```python
   my_array.remove(10)
   print(my_array)
   ```
9. Reverse an array using `reverse()`.
   ```python
   my_array.reverse()
   print(my_array)
   ```
10. Use `count()` to count the occurrences of an item in an array.
    ```python
    print(my_array.count(5))  # Output: 1
    ```

---




---

This structured content provides clear explanations and hands-on examples. Let me know if you need modifications or additional topics! 🚀

