### Python courses



#### Third Part
Python Lists

Python Tuples

Python Sets

Python Dictionaries

Python If...Else

Here’s the structured content for the third part of your Python course:

---

## **Python Lists**
Lists are ordered, mutable collections that can store multiple items.

### **Example 1: Creating a List**
```python
fruits = ["apple", "banana", "cherry"]
print(fruits)
```

### **Example 2: Accessing List Elements**
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # First element
print(fruits[-1])  # Last element
```

### **Example 3: Modifying List Elements**
```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"
print(fruits)
```

### **Example 4: Adding Elements to a List**
```python
fruits = ["apple", "banana"]
fruits.append("cherry")  # Adds to the end
fruits.insert(1, "orange")  # Adds at index 1
print(fruits)
```

### **Example 5: Removing Elements from a List**
```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")  # Removes by value
fruits.pop(0)  # Removes by index
print(fruits)
```

---
### **1. Python Lists**
**Content:**
- What are lists? (Ordered, mutable collections of items).
- Creating and accessing list elements.
- Common list methods (`append()`, `remove()`, `insert()`, `pop()`, etc.).
- List slicing and indexing.
- List comprehensions for concise list creation.

**Examples:**
1. Create a list of numbers and access the first element.
2. Append an item to the end of a list using `append()`.
3. Remove an item from a list using `remove()`.
4. Use slicing to extract a sublist.
5. Create a list using a list comprehension (e.g., `[x**2 for x in range(5)]`).

**Additional Examples:**
6. Insert an item at a specific position using `insert()`.
7. Remove and return the last item using `pop()`.
8. Reverse a list using `reverse()`.
9. Sort a list using `sort()`.
10. Check if an item exists in a list using the `in` keyword.

## **Python Tuples**
Tuples are ordered, immutable collections.

### **Example 1: Creating a Tuple**
```python
numbers = (1, 2, 3, 4, 5)
print(numbers)
```

### **Example 2: Accessing Tuple Elements**
```python
numbers = (1, 2, 3, 4)
print(numbers[0], numbers[-1])
```

### **Example 3: Tuple Unpacking**
```python
a, b, c = (10, 20, 30)
print(a, b, c)
```

### **Example 4: Finding Elements in a Tuple**
```python
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)
```

### **Example 5: Tuple Length**
```python
numbers = (1, 2, 3, 4, 5)
print(len(numbers))
```

---

### **2. Python Tuples**
**Content:**
- What are tuples? (Ordered, immutable collections of items).
- Creating and accessing tuple elements.
- Differences between tuples and lists.
- Common tuple operations (concatenation, repetition, etc.).
- When to use tuples instead of lists.

**Examples:**
1. Create a tuple of mixed data types.
2. Access the second element of a tuple.
3. Concatenate two tuples.
4. Repeat a tuple using the `*` operator.
5. Convert a list to a tuple using `tuple()`.

**Additional Examples:**
6. Use tuple unpacking to assign values to variables.
7. Check if an item exists in a tuple using the `in` keyword.
8. Create a tuple with a single item (note the trailing comma).
9. Use tuples as keys in a dictionary.
10. Compare two tuples using comparison operators.

---

## **Python Sets**
Sets are unordered, unique collections.

### **Example 1: Creating a Set**
```python
numbers = {1, 2, 3, 4, 5}
print(numbers)
```

### **Example 2: Adding Elements to a Set**
```python
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)
```

### **Example 3: Removing Elements from a Set**
```python
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)
```

### **Example 4: Set Operations (Union, Intersection)**
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Union
print(set1 & set2)  # Intersection
```

### **Example 5: Checking Membership in a Set**
```python
numbers = {1, 2, 3, 4}
print(3 in numbers)
```

---

### **3. Python Sets**
**Content:**
- What are sets? (Unordered, mutable collections of unique items).
- Creating and accessing set elements.
- Common set methods (`add()`, `remove()`, `union()`, `intersection()`, etc.).
- Set operations (difference, symmetric difference, etc.).
- Frozen sets (immutable sets).

**Examples:**
1. Create a set of unique numbers.
2. Add an item to a set using `add()`.
3. Remove an item from a set using `remove()`.
4. Find the union of two sets using `union()`.
5. Find the intersection of two sets using `intersection()`.

**Additional Examples:**
6. Find the difference between two sets using `difference()`.
7. Find the symmetric difference between two sets using `symmetric_difference()`.
8. Check if a set is a subset of another set using `issubset()`.
9. Convert a list to a set to remove duplicates.
10. Use a frozen set to create an immutable set.


## **Python Dictionaries**
Dictionaries store key-value pairs.

### **Example 1: Creating a Dictionary**
```python
person = {"name": "Alice", "age": 25}
print(person)
```

### **Example 2: Accessing Values in a Dictionary**
```python
person = {"name": "Alice", "age": 25}
print(person["name"])
```

### **Example 3: Modifying Dictionary Values**
```python
person = {"name": "Alice", "age": 25}
person["age"] = 26
print(person)
```

### **Example 4: Adding and Removing Key-Value Pairs**
```python
person = {"name": "Alice", "age": 25}
person["city"] = "New York"
del person["age"]
print(person)
```

### **Example 5: Iterating Through a Dictionary**
```python
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(key, ":", value)
```

---

### **4. Python Dictionaries**
**Content:**
- What are dictionaries? (Unordered, mutable collections of key-value pairs).
- Creating and accessing dictionary elements.
- Common dictionary methods (`keys()`, `values()`, `items()`, `get()`, etc.).
- Adding, updating, and removing dictionary items.
- Dictionary comprehensions for concise dictionary creation.

**Examples:**
1. Create a dictionary with key-value pairs.
2. Access a value using its key.
3. Add a new key-value pair to a dictionary.
4. Update the value of an existing key.
5. Remove a key-value pair using `pop()`.

**Additional Examples:**
6. Get all keys from a dictionary using `keys()`.
7. Get all values from a dictionary using `values()`.
8. Get all key-value pairs using `items()`.
9. Use `get()` to safely access a value with a default.
10. Create a dictionary using a dictionary comprehension (e.g., `{x: x**2 for x in range(5)}`).

## **Python If...Else**
Conditional statements control program flow.

### **Example 1: Basic If Statement**
```python
x = 10
if x > 5:
    print("x is greater than 5")
```

### **Example 2: If-Else Statement**
```python
x = 10
if x > 10:
    print("Greater than 10")
else:
    print("10 or less")
```

### **Example 3: If-Elif-Else Statement**
```python
x = 10
if x > 10:
    print("Greater than 10")
elif x == 10:
    print("Equal to 10")
else:
    print("Less than 10")
```

### **Example 4: Nested If Statement**
```python
x = 10
if x > 5:
    if x < 20:
        print("x is between 5 and 20")
```

### **Example 5: Using Logical Operators**
```python
x = 10
y = 5
if x > 5 and y < 10:
    print("Both conditions are True")
```

---

### **5. Python If...Else**
**Content:**
- What are conditional statements? (Control flow based on conditions).
- Syntax of `if`, `elif`, and `else` statements.
- Nested `if` statements.
- Ternary conditional operator for concise conditions.
- Common use cases for conditional statements.

**Examples:**
1. Write a simple `if` statement to check a condition.
2. Use `elif` to check multiple conditions.
3. Use `else` to handle cases where no condition is met.
4. Write a nested `if` statement.
5. Use the ternary operator for a concise conditional assignment.

**Additional Examples:**
6. Check if a number is positive, negative, or zero using `if-elif-else`.
7. Use `and` and `or` in a conditional statement.
8. Check if a list is empty using an `if` statement.
9. Use `if-else` in a list comprehension.
10. Write a program to determine if a year is a leap year.

Certainly! Below is the structured outline for the third part of your Python course, including content and **5 Python sample codes** for each title. I've also added **5 more examples** for each section to ensure comprehensive coverage.

---

### **1. Python Lists**
**Content:**
- What are lists? (Ordered, mutable collections of items).
- Creating and accessing list elements.
- Common list methods (`append()`, `remove()`, `insert()`, `pop()`, etc.).
- List slicing and indexing.
- List comprehensions for concise list creation.

**Sample Codes:**
1. Create a list of numbers and access the first element.
   ```python
   my_list = [1, 2, 3, 4, 5]
   print(my_list[0])  # Output: 1
   ```
2. Append an item to the end of a list using `append()`.
   ```python
   my_list.append(6)
   print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
   ```
3. Remove an item from a list using `remove()`.
   ```python
   my_list.remove(3)
   print(my_list)  # Output: [1, 2, 4, 5, 6]
   ```
4. Use slicing to extract a sublist.
   ```python
   print(my_list[1:4])  # Output: [2, 4, 5]
   ```
5. Create a list using a list comprehension.
   ```python
   squares = [x**2 for x in range(5)]
   print(squares)  # Output: [0, 1, 4, 9, 16]
   ```

**Additional Examples:**
6. Insert an item at a specific position using `insert()`.
   ```python
   my_list.insert(2, 10)
   print(my_list)  # Output: [1, 2, 10, 4, 5, 6]
   ```
7. Remove and return the last item using `pop()`.
   ```python
   last_item = my_list.pop()
   print(last_item)  # Output: 6
   ```
8. Reverse a list using `reverse()`.
   ```python
   my_list.reverse()
   print(my_list)  # Output: [5, 4, 10, 2, 1]
   ```
9. Sort a list using `sort()`.
   ```python
   my_list.sort()
   print(my_list)  # Output: [1, 2, 4, 5, 10]
   ```
10. Check if an item exists in a list using the `in` keyword.
    ```python
    print(4 in my_list)  # Output: True
    ```

---

### **2. Python Tuples**
**Content:**
- What are tuples? (Ordered, immutable collections of items).
- Creating and accessing tuple elements.
- Differences between tuples and lists.
- Common tuple operations (concatenation, repetition, etc.).
- When to use tuples instead of lists.

**Sample Codes:**
1. Create a tuple of mixed data types.
   ```python
   my_tuple = (1, "apple", 3.14)
   print(my_tuple)  # Output: (1, "apple", 3.14)
   ```
2. Access the second element of a tuple.
   ```python
   print(my_tuple[1])  # Output: "apple"
   ```
3. Concatenate two tuples.
   ```python
   tuple1 = (1, 2, 3)
   tuple2 = (4, 5, 6)
   print(tuple1 + tuple2)  # Output: (1, 2, 3, 4, 5, 6)
   ```
4. Repeat a tuple using the `*` operator.
   ```python
   print(tuple1 * 2)  # Output: (1, 2, 3, 1, 2, 3)
   ```
5. Convert a list to a tuple using `tuple()`.
   ```python
   my_list = [1, 2, 3]
   my_tuple = tuple(my_list)
   print(my_tuple)  # Output: (1, 2, 3)
   ```

**Additional Examples:**
6. Use tuple unpacking to assign values to variables.
   ```python
   a, b, c = my_tuple
   print(a, b, c)  # Output: 1 "apple" 3.14
   ```
7. Check if an item exists in a tuple using the `in` keyword.
   ```python
   print("apple" in my_tuple)  # Output: True
   ```
8. Create a tuple with a single item (note the trailing comma).
   ```python
   single_tuple = (1,)
   print(single_tuple)  # Output: (1,)
   ```
9. Use tuples as keys in a dictionary.
   ```python
   my_dict = {(1, 2): "value"}
   print(my_dict[(1, 2)])  # Output: "value"
   ```
10. Compare two tuples using comparison operators.
    ```python
    print((1, 2, 3) < (1, 2, 4))  # Output: True
    ```

---

### **3. Python Sets**
**Content:**
- What are sets? (Unordered, mutable collections of unique items).
- Creating and accessing set elements.
- Common set methods (`add()`, `remove()`, `union()`, `intersection()`, etc.).
- Set operations (difference, symmetric difference, etc.).
- Frozen sets (immutable sets).

**Sample Codes:**
1. Create a set of unique numbers.
   ```python
   my_set = {1, 2, 3, 4, 5}
   print(my_set)  # Output: {1, 2, 3, 4, 5}
   ```
2. Add an item to a set using `add()`.
   ```python
   my_set.add(6)
   print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
   ```
3. Remove an item from a set using `remove()`.
   ```python
   my_set.remove(3)
   print(my_set)  # Output: {1, 2, 4, 5, 6}
   ```
4. Find the union of two sets using `union()`.
   ```python
   set1 = {1, 2, 3}
   set2 = {3, 4, 5}
   print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}
   ```
5. Find the intersection of two sets using `intersection()`.
   ```python
   print(set1.intersection(set2))  # Output: {3}
   ```

**Additional Examples:**
6. Find the difference between two sets using `difference()`.
   ```python
   print(set1.difference(set2))  # Output: {1, 2}
   ```
7. Find the symmetric difference between two sets using `symmetric_difference()`.
   ```python
   print(set1.symmetric_difference(set2))  # Output: {1, 2, 4, 5}
   ```
8. Check if a set is a subset of another set using `issubset()`.
   ```python
   print({1, 2}.issubset(set1))  # Output: True
   ```
9. Convert a list to a set to remove duplicates.
   ```python
   my_list = [1, 2, 2, 3, 3]
   my_set = set(my_list)
   print(my_set)  # Output: {1, 2, 3}
   ```
10. Use a frozen set to create an immutable set.
    ```python
    frozen_set = frozenset([1, 2, 3])
    print(frozen_set)  # Output: frozenset({1, 2, 3})
    ```

---

### **4. Python Dictionaries**
**Content:**
- What are dictionaries? (Unordered, mutable collections of key-value pairs).
- Creating and accessing dictionary elements.
- Common dictionary methods (`keys()`, `values()`, `items()`, `get()`, etc.).
- Adding, updating, and removing dictionary items.
- Dictionary comprehensions for concise dictionary creation.

**Sample Codes:**
1. Create a dictionary with key-value pairs.
   ```python
   my_dict = {"name": "John", "age": 30}
   print(my_dict)  # Output: {"name": "John", "age": 30}
   ```
2. Access a value using its key.
   ```python
   print(my_dict["name"])  # Output: "John"
   ```
3. Add a new key-value pair to a dictionary.
   ```python
   my_dict["city"] = "New York"
   print(my_dict)  # Output: {"name": "John", "age": 30, "city": "New York"}
   ```
4. Update the value of an existing key.
   ```python
   my_dict["age"] = 31
   print(my_dict)  # Output: {"name": "John", "age": 31, "city": "New York"}
   ```
5. Remove a key-value pair using `pop()`.
   ```python
   my_dict.pop("city")
   print(my_dict)  # Output: {"name": "John", "age": 31}
   ```

**Additional Examples:**
6. Get all keys from a dictionary using `keys()`.
   ```python
   print(my_dict.keys())  # Output: dict_keys(['name', 'age'])
   ```
7. Get all values from a dictionary using `values()`.
   ```python
   print(my_dict.values())  # Output: dict_values(['John', 31])
   ```
8. Get all key-value pairs using `items()`.
   ```python
   print(my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 31)])
   ```
9. Use `get()` to safely access a value with a default.
   ```python
   print(my_dict.get("city", "Unknown"))  # Output: "Unknown"
   ```
10. Create a dictionary using a dictionary comprehension.
    ```python
    squares = {x: x**2 for x in range(5)}
    print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    ```

---

### **5. Python If...Else**
**Content:**
- What are conditional statements? (Control flow based on conditions).
- Syntax of `if`, `elif`, and `else` statements.
- Nested `if` statements.
- Ternary conditional operator for concise conditions.
- Common use cases for conditional statements.

**Sample Codes:**
1. Write a simple `if` statement to check a condition.
   ```python
   x = 10
   if x > 5:
       print("x is greater than 5")
   ```
2. Use `elif` to check multiple conditions.
   ```python
   if x > 10:
       print("x is greater than 10")
   elif x == 10:
       print("x is equal to 10")
   else:
       print("x is less than 10")
   ```
3. Use `else` to handle cases where no condition is met.
   ```python
   if x < 5:
       print("x is less than 5")
   else:
       print("x is greater than or equal to 5")
   ```
4. Write a nested `if` statement.
   ```python
   if x > 5:
       if x < 15:
           print("x is between 5 and 15")
   ```
5. Use the ternary operator for a concise conditional assignment.
   ```python
   result = "Even" if x % 2 == 0 else "Odd"
   print(result)
   ```

**Additional Examples:**
6. Check if a number is positive, negative, or zero using `if-elif-else`.
   ```python
   num = -5
   if num > 0:
       print("Positive")
   elif num < 0:
       print("Negative")
   else:
       print("Zero")
   ```
7. Use `and` and `or` in a conditional statement.
   ```python
   if x > 5 and x < 15:
       print("x is between 5 and 15")
   ```
8. Check if a list is empty using an `if` statement.
   ```python
   my_list = []
   if not my_list:
       print("List is empty")
   ```
9. Use `if-else` in a list comprehension.
   ```python
   numbers = [1, 2, 3, 4, 5]
   even_numbers = [x for x in numbers if x % 2 == 0]
   print(even_numbers)  # Output: [2, 4]
   ```
10. Write a program to determine if a year is a leap year.
    ```python
    year = 2024
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap year")
    else:
        print("Not a leap year")
    ```

---

This structure should provide a solid foundation for the third part of your Python course. Let me know if you'd like further assistance!

