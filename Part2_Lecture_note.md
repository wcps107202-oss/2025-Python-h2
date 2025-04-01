
### Python courses



#### Second Part
Python Data Types

Python Numbers

Python Casting

Python Strings

Python Booleans

Python Operators

Here’s the structured content for the second part of your Python course:

---

## **Python Data Types**
Python has several built-in data types:
- `int` (integer)
- `float` (floating-point number)
- `str` (string)
- `bool` (boolean)
- `list` (ordered, mutable collection)
- `tuple` (ordered, immutable collection)
- `set` (unordered, unique items)
- `dict` (key-value pairs)

### **Example 1: Checking Data Types**
```python
x = 10
y = 3.14
z = "Hello"
print(type(x), type(y), type(z))
```

### **Example 2: List Data Type**
```python
fruits = ["apple", "banana", "cherry"]
print(fruits, type(fruits))
```

### **Example 3: Tuple Data Type**
```python
coordinates = (10, 20)
print(coordinates, type(coordinates))
```

### **Example 4: Dictionary Data Type**
```python
person = {"name": "Alice", "age": 25}
print(person, type(person))
```

### **Example 5: Set Data Type**
```python
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers, type(unique_numbers))
```

---

### **1. Python Data Types**
**Content:**
- Overview of Python's built-in data types.
- Categories of data types: Numeric, Sequence, Mapping, Set, Boolean, and None.
- How to check the data type of a variable using `type()`.
- Mutable vs Immutable data types.

**Examples:**
1. Check the data type of an integer, float, and string.
2. Create a list and check its data type.
3. Create a dictionary and check its data type.
4. Demonstrate the difference between mutable (list) and immutable (tuple) data types.
5. Use `type()` to identify the data type of a boolean value.

**Additional Examples:**
6. Create a set and check its data type.
7. Check the data type of `None`.
8. Create a complex number and check its data type.
9. Use `isinstance()` to verify if a variable is of a specific data type.
10. Compare the memory usage of different data types using `sys.getsizeof()`.

## **Python Numbers**
Python supports:
- `int` (whole numbers)
- `float` (decimal numbers)
- `complex` (complex numbers)

### **Example 1: Integer Type**
```python
x = 100
print(x, type(x))
```

### **Example 2: Float Type**
```python
y = 3.1415
print(y, type(y))
```

### **Example 3: Complex Number**
```python
z = 2 + 3j
print(z, type(z))
```

### **Example 4: Arithmetic with Numbers**
```python
a = 5
b = 2
print(a + b, a - b, a * b, a / b)
```

### **Example 5: Exponential and Modulus**
```python
print(2**3)  # 2 raised to the power 3
print(10 % 3)  # Remainder of 10/3
```

---

### **2. Python Numbers**
**Content:**
- Types of numeric data types: `int`, `float`, and `complex`.
- Arithmetic operations (+, -, *, /, %, **, //).
- Type conversion between numeric types.
- Working with large numbers and scientific notation.

**Examples:**
1. Perform basic arithmetic operations (e.g., `5 + 3 * 2`).
2. Convert a float to an integer using `int()`.
3. Use the modulus operator `%` to find the remainder.
4. Calculate the power of a number using `**`.
5. Use floor division `//` to divide and discard the remainder.

**Additional Examples:**
6. Work with complex numbers (e.g., `3 + 4j`).
7. Use scientific notation to represent large numbers (e.g., `1e6`).
8. Round a float to a specific number of decimal places using `round()`.
9. Check if a number is even or odd using the modulus operator.
10. Use the `math` module to perform advanced mathematical operations.

## **Python Casting**
Casting is used to convert data types.

### **Example 1: Converting String to Integer**
```python
num_str = "100"
num_int = int(num_str)
print(num_int, type(num_int))
```

### **Example 2: Converting Integer to Float**
```python
x = 10
y = float(x)
print(y, type(y))
```

### **Example 3: Converting Float to Integer**
```python
pi = 3.99
integer_pi = int(pi)
print(integer_pi, type(integer_pi))
```

### **Example 4: Converting Number to String**
```python
num = 123
num_str = str(num)
print(num_str, type(num_str))
```

### **Example 5: Casting User Input**
```python
age = int(input("Enter your age: "))
print("You are", age, "years old")
```

---

### **3. Python Casting**
**Content:**
- What is type casting? (Converting one data type to another).
- Implicit vs explicit casting.
- Functions for casting: `int()`, `float()`, `str()`, `bool()`, etc.
- Handling errors during casting.

**Examples:**
1. Convert a string to an integer using `int()`.
2. Convert an integer to a float using `float()`.
3. Convert a float to a string using `str()`.
4. Convert a non-zero number to a boolean using `bool()`.
5. Handle a casting error using `try` and `except`.

**Additional Examples:**
6. Convert a list of strings to a list of integers.
7. Convert a boolean to an integer (e.g., `int(True)`).
8. Use `eval()` to evaluate a string as a Python expression.
9. Convert a string to a list of characters.
10. Cast a tuple to a list and vice versa.


## **Python Strings**
Strings are sequences of characters.

### **Example 1: Creating Strings**
```python
text = "Hello, Python!"
print(text)
```

### **Example 2: String Indexing**
```python
word = "Python"
print(word[0], word[-1])  # First and last character
```

### **Example 3: String Slicing**
```python
word = "Python"
print(word[1:4])  # "yth"
```

### **Example 4: String Methods**
```python
sentence = "hello world"
print(sentence.upper(), sentence.capitalize())
```

### **Example 5: String Concatenation**
```python
first = "Hello"
second = "World"
result = first + " " + second
print(result)
```

---
### **4. Python Strings**
**Content:**
- What are strings? (Sequence of characters).
- String indexing and slicing.
- Common string methods (`upper()`, `lower()`, `strip()`, `replace()`, etc.).
- String formatting (f-strings, `format()`, `%` operator).

**Examples:**
1. Create a string and access its characters using indexing.
2. Use slicing to extract a substring.
3. Convert a string to uppercase using `upper()`.
4. Replace a substring using `replace()`.
5. Format a string using f-strings (e.g., `f"Hello, {name}!"`).


**Additional Examples:**
6. Check if a string starts or ends with a specific substring.
7. Split a string into a list using `split()`.
8. Join a list of strings into a single string using `join()`.
9. Use `strip()` to remove leading and trailing whitespace.
10. Count the occurrences of a substring using `count()`.

---


## **Python Booleans**
Booleans represent `True` or `False`.

### **Example 1: Boolean Values**
```python
print(True, False)
```

### **Example 2: Boolean Expressions**
```python
print(10 > 5)
print(5 == 5)
```

### **Example 3: Boolean with If Statement**
```python
x = 10
if x > 5:
    print("x is greater than 5")
```

### **Example 4: Converting Values to Boolean**
```python
print(bool(0), bool(1), bool("Python"), bool(""))
```

### **Example 5: Boolean Operators**
```python
a, b = True, False
print(a and b, a or b, not a)
```

---

### **5. Python Booleans**
**Content:**
- What are booleans? (`True` and `False` values).
- Boolean operations (`and`, `or`, `not`).
- Truthy and falsy values in Python.
- Comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`).

**Examples:**
1. Use comparison operators to compare two numbers.
2. Combine boolean expressions using `and` and `or`.
3. Use `not` to negate a boolean value.
4. Check if a value is truthy or falsy.
5. Use `bool()` to convert a value to a boolean.

**Additional Examples:**
6. Check if a list is empty using a boolean expression.
7. Use `any()` and `all()` with a list of booleans.
8. Compare strings using boolean operators.
9. Use boolean expressions in an `if` statement.
10. Demonstrate short-circuit evaluation with `and` and `or`.

---

## **Python Operators**
Operators perform operations on variables and values.

### **Types of Operators:**
1. Arithmetic (`+`, `-`, `*`, `/`, `%`, `**`, `//`)
2. Comparison (`==`, `!=`, `>`, `<`, `>=`, `<=`)
3. Logical (`and`, `or`, `not`)
4. Assignment (`=`, `+=`, `-=`, `*=`, `/=`)
5. Bitwise (`&`, `|`, `^`, `<<`, `>>`)
6. Membership (`in`, `not in`)

### **Example 1: Arithmetic Operators**
```python
x, y = 10, 3
print(x + y, x - y, x * y, x / y, x % y, x ** y, x // y)
```

### **Example 2: Comparison Operators**
```python
print(10 > 5, 10 == 10, 10 != 5)
```

### **Example 3: Logical Operators**
```python
print(True and False, True or False, not True)
```

### **Example 4: Assignment Operators**
```python
x = 5
x += 3  # x = x + 3
print(x)
```

### **Example 5: Membership Operators**
```python
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits, "mango" not in fruits)
```

---
### **6. Python Operators**
**Content:**
- Types of operators: Arithmetic, Comparison, Logical, Assignment, Bitwise, Membership, and Identity.
- Operator precedence and associativity.
- Special operators: `is`, `is not`, `in`, `not in`.

**Examples:**
1. Use arithmetic operators to perform calculations.
2. Compare two values using comparison operators.
3. Use logical operators to combine conditions.
4. Assign values to variables using assignment operators.
5. Use membership operators to check if a value exists in a sequence.

**Additional Examples:**
6. Use bitwise operators to perform binary operations.
7. Use the identity operator `is` to compare object IDs.
8. Use the ternary operator for conditional assignment.
9. Demonstrate operator precedence with a complex expression.
10. Use the `in` operator to check for substrings in a string.

---

### **Additional Examples for Each Section**

#### **Python Data Types**
11. Create a nested list and check its data type.
12. Use `collections.namedtuple` to create a custom data type.
13. Convert a dictionary to a list of tuples using `items()`.
14. Use `frozenset` to create an immutable set.
15. Check if a variable is an instance of multiple data types using `isinstance()`.

#### **Python Numbers**
11. Use the `decimal` module for precise decimal arithmetic.
12. Calculate the factorial of a number using the `math` module.
13. Generate random numbers using the `random` module.
14. Use the `cmath` module to work with complex numbers.
15. Calculate the greatest common divisor (GCD) using `math.gcd()`.

#### **Python Casting**
11. Convert a string to a datetime object using `datetime.strptime()`.
12. Convert a list of integers to a single string.
13. Use `ast.literal_eval()` to safely evaluate a string as a Python literal.
14. Convert a dictionary to a JSON string using `json.dumps()`.
15. Cast a string to a boolean using custom logic (e.g., `"True"` → `True`).

#### **Python Strings**
11. Use `find()` to locate the index of a substring.
12. Reverse a string using slicing.
13. Use `title()` to capitalize the first letter of each word.
14. Check if a string is alphanumeric using `isalnum()`.
15. Use `zfill()` to pad a numeric string with zeros.

#### **Python Booleans**
11. Use boolean indexing to filter a list.
12. Check if all elements in a list satisfy a condition using `all()`.
13. Use boolean values in a dictionary to control program flow.
14. Demonstrate the difference between `==` and `is`.
15. Use boolean expressions in list comprehensions.

#### **Python Operators**
11. Use the walrus operator `:=` for assignment within expressions.
12. Use the `operator` module for functional programming.
13. Demonstrate the use of `@` for matrix multiplication.
14. Use the `reduce()` function with the `operator` module.
15. Override operators for custom classes using magic methods (e.g., `__add__`).

### **1. Python Data Types**
**Content:**
- Overview of Python's built-in data types.
- Categories of data types: Numeric, Sequence, Mapping, Set, Boolean, and None.
- How to check the data type of a variable using `type()`.
- Mutable vs Immutable data types.

**Sample Codes:**
1. Check the data type of an integer, float, and string.
   ```python
   print(type(10))          # <class 'int'>
   print(type(3.14))        # <class 'float'>
   print(type("Hello"))     # <class 'str'>
   ```
2. Create a list and check its data type.
   ```python
   my_list = [1, 2, 3]
   print(type(my_list))     # <class 'list'>
   ```
3. Create a dictionary and check its data type.
   ```python
   my_dict = {"name": "John", "age": 30}
   print(type(my_dict))     # <class 'dict'>
   ```
4. Demonstrate the difference between mutable (list) and immutable (tuple) data types.
   ```python
   my_list = [1, 2, 3]
   my_list[0] = 10  # Mutable
   my_tuple = (1, 2, 3)
   # my_tuple[0] = 10  # Immutable (will raise an error)
   ```
5. Use `type()` to identify the data type of a boolean value.
   ```python
   print(type(True))        # <class 'bool'>
   ```

**Additional Examples:**
6. Create a set and check its data type.
   ```python
   my_set = {1, 2, 3}
   print(type(my_set))      # <class 'set'>
   ```
7. Check the data type of `None`.
   ```python
   print(type(None))        # <class 'NoneType'>
   ```
8. Create a complex number and check its data type.
   ```python
   my_complex = 3 + 4j
   print(type(my_complex))  # <class 'complex'>
   ```
9. Use `isinstance()` to verify if a variable is of a specific data type.
   ```python
   print(isinstance(10, int))  # True
   ```
10. Compare the memory usage of different data types using `sys.getsizeof()`.
    ```python
    import sys
    print(sys.getsizeof(10))    # Size of an integer
    print(sys.getsizeof("Hello"))  # Size of a string
    ```

---

### **2. Python Numbers**
**Content:**
- Types of numeric data types: `int`, `float`, and `complex`.
- Arithmetic operations (+, -, *, /, %, **, //).
- Type conversion between numeric types.
- Working with large numbers and scientific notation.

**Sample Codes:**
1. Perform basic arithmetic operations.
   ```python
   print(5 + 3 * 2)  # Output: 11
   ```
2. Convert a float to an integer using `int()`.
   ```python
   x = 3.14
   print(int(x))  # Output: 3
   ```
3. Use the modulus operator `%` to find the remainder.
   ```python
   print(10 % 3)  # Output: 1
   ```
4. Calculate the power of a number using `**`.
   ```python
   print(2 ** 3)  # Output: 8
   ```
5. Use floor division `//` to divide and discard the remainder.
   ```python
   print(10 // 3)  # Output: 3
   ```

**Additional Examples:**
6. Work with complex numbers.
   ```python
   z = 3 + 4j
   print(z.real)  # Output: 3.0
   print(z.imag)  # Output: 4.0
   ```
7. Use scientific notation to represent large numbers.
   ```python
   x = 1e6  # 1 million
   print(x)  # Output: 1000000.0
   ```
8. Round a float to a specific number of decimal places using `round()`.
   ```python
   x = 3.14159
   print(round(x, 2))  # Output: 3.14
   ```
9. Check if a number is even or odd using the modulus operator.
   ```python
   num = 7
   if num % 2 == 0:
       print("Even")
   else:
       print("Odd")
   ```
10. Use the `math` module to perform advanced mathematical operations.
    ```python
    import math
    print(math.sqrt(16))  # Output: 4.0
    ```

---

### **3. Python Casting**
**Content:**
- What is type casting? (Converting one data type to another).
- Implicit vs explicit casting.
- Functions for casting: `int()`, `float()`, `str()`, `bool()`, etc.
- Handling errors during casting.

**Sample Codes:**
1. Convert a string to an integer using `int()`.
   ```python
   x = "10"
   print(int(x))  # Output: 10
   ```
2. Convert an integer to a float using `float()`.
   ```python
   x = 10
   print(float(x))  # Output: 10.0
   ```
3. Convert a float to a string using `str()`.
   ```python
   x = 3.14
   print(str(x))  # Output: "3.14"
   ```
4. Convert a non-zero number to a boolean using `bool()`.
   ```python
   x = 5
   print(bool(x))  # Output: True
   ```
5. Handle a casting error using `try` and `except`.
   ```python
   try:
       x = int("abc")
   except ValueError:
       print("Invalid conversion!")
   ```

**Additional Examples:**
6. Convert a list of strings to a list of integers.
   ```python
   str_list = ["1", "2", "3"]
   int_list = [int(x) for x in str_list]
   print(int_list)  # Output: [1, 2, 3]
   ```
7. Convert a boolean to an integer.
   ```python
   x = True
   print(int(x))  # Output: 1
   ```
8. Use `eval()` to evaluate a string as a Python expression.
   ```python
   x = "10 + 5"
   print(eval(x))  # Output: 15
   ```
9. Convert a string to a list of characters.
   ```python
   x = "Hello"
   print(list(x))  # Output: ['H', 'e', 'l', 'l', 'o']
   ```
10. Cast a tuple to a list and vice versa.
    ```python
    my_tuple = (1, 2, 3)
    my_list = list(my_tuple)
    print(my_list)  # Output: [1, 2, 3]
    ```

---

### **4. Python Strings**
**Content:**
- What are strings? (Sequence of characters).
- String indexing and slicing.
- Common string methods (`upper()`, `lower()`, `strip()`, `replace()`, etc.).
- String formatting (f-strings, `format()`, `%` operator).

**Sample Codes:**
1. Create a string and access its characters using indexing.
   ```python
   s = "Hello"
   print(s[0])  # Output: 'H'
   ```
2. Use slicing to extract a substring.
   ```python
   s = "Hello, World!"
   print(s[0:5])  # Output: "Hello"
   ```
3. Convert a string to uppercase using `upper()`.
   ```python
   s = "hello"
   print(s.upper())  # Output: "HELLO"
   ```
4. Replace a substring using `replace()`.
   ```python
   s = "Hello, World!"
   print(s.replace("World", "Python"))  # Output: "Hello, Python!"
   ```
5. Format a string using f-strings.
   ```python
   name = "John"
   print(f"Hello, {name}!")  # Output: "Hello, John!"
   ```

**Additional Examples:**
6. Check if a string starts or ends with a specific substring.
   ```python
   s = "Hello, World!"
   print(s.startswith("Hello"))  # Output: True
   print(s.endswith("World!"))   # Output: True
   ```
7. Split a string into a list using `split()`.
   ```python
   s = "apple,banana,cherry"
   print(s.split(","))  # Output: ['apple', 'banana', 'cherry']
   ```
8. Join a list of strings into a single string using `join()`.
   ```python
   my_list = ["apple", "banana", "cherry"]
   print(", ".join(my_list))  # Output: "apple, banana, cherry"
   ```
9. Use `strip()` to remove leading and trailing whitespace.
   ```python
   s = "   Hello, World!   "
   print(s.strip())  # Output: "Hello, World!"
   ```
10. Count the occurrences of a substring using `count()`.
    ```python
    s = "Hello, World!"
    print(s.count("l"))  # Output: 3
    ```

---

### **5. Python Booleans**
**Content:**
- What are booleans? (`True` and `False` values).
- Boolean operations (`and`, `or`, `not`).
- Truthy and falsy values in Python.
- Comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`).

**Sample Codes:**
1. Use comparison operators to compare two numbers.
   ```python
   print(5 > 3)  # Output: True
   ```
2. Combine boolean expressions using `and` and `or`.
   ```python
   print(5 > 3 and 2 < 4)  # Output: True
   ```
3. Use `not` to negate a boolean value.
   ```python
   print(not True)  # Output: False
   ```
4. Check if a value is truthy or falsy.
   ```python
   x = 0
   print(bool(x))  # Output: False
   ```
5. Use `bool()` to convert a value to a boolean.
   ```python
   print(bool("Hello"))  # Output: True
   ```

**Additional Examples:**
6. Check if a list is empty using a boolean expression.
   ```python
   my_list = []
   print(bool(my_list))  # Output: False
   ```
7. Use `any()` and `all()` with a list of booleans.
   ```python
   print(any([False, True, False]))  # Output: True
   print(all([True, True, False]))   # Output: False
   ```
8. Compare strings using boolean operators.
   ```python
   print("apple" == "apple")  # Output: True
   ```
9. Use boolean expressions in an `if` statement.
   ```python
   x = 10
   if x > 5:
       print("x is greater than 5")
   ```
10. Demonstrate short-circuit evaluation with `and` and `or`.
    ```python
    def check():
        print("Checked!")
        return True
    print(False and check())  # Output: False (check() is not called)
    ```

---

### **6. Python Operators**
**Content:**
- Types of operators: Arithmetic, Comparison, Logical, Assignment, Bitwise, Membership, and Identity.
- Operator precedence and associativity.
- Special operators: `is`, `is not`, `in`, `not in`.

**Sample Codes:**
1. Use arithmetic operators to perform calculations.
   ```python
   print(5 + 3)  # Output: 8
   ```
2. Compare two values using comparison operators.
   ```python
   print(5 > 3)  # Output: True
   ```
3. Use logical operators to combine conditions.
   ```python
   print(5 > 3 and 2 < 4)  # Output: True
   ```
4. Assign values to variables using assignment operators.
   ```python
   x = 5
   x += 3
   print(x)  # Output: 8
   ```
5. Use membership operators to check if a value exists in a sequence.
   ```python
   print("a" in "apple")  # Output: True
   ```

**Additional Examples:**
6. Use bitwise operators to perform binary operations.
   ```python
   print(5 & 3)  # Output: 1
   ```
7. Use the identity operator `is` to compare object IDs.
   ```python
   x = [1, 2, 3]
   y = x
   print(x is y)  # Output: True
   ```
8. Use the ternary operator for conditional assignment.
   ```python
   x = 10
   result = "Even" if x % 2 == 0 else "Odd"
   print(result)  # Output: "Even"
   ```
9. Demonstrate operator precedence with a complex expression.
   ```python
   print(5 + 3 * 2)  # Output: 11
   ```
10. Use the `in` operator to check for substrings in a string.
    ```python
    print("apple" in "I love apples!")  # Output: True
    ```

---

This structure should provide a solid foundation for the second part of your Python course. Let me know if you'd like further assistance!



