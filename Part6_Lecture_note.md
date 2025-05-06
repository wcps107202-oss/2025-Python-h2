
### Python courses


#### Sixth Part
Python Dates

Python Math

Python JSON

Python RegEx

Python PIP

Python Try...Except



Python String Formatting

Here’s the structured content for the sixth part of your Python course:

---

## **Python Dates**  
Python has a built-in `datetime` module to work with dates and times.

### **Example 1: Getting the Current Date and Time**
```python
import datetime

now = datetime.datetime.now()
print("Current date and time:", now)
```

### **Example 2: Formatting Dates**
```python
import datetime

now = datetime.datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted_date)
```

### **Example 3: Creating a Specific Date**
```python
import datetime

specific_date = datetime.datetime(2025, 3, 15)
print("Specific Date:", specific_date)
```

### **Example 4: Date Arithmetic**
```python
import datetime

today = datetime.date.today()
future_date = today + datetime.timedelta(days=10)
print("Date after 10 days:", future_date)
```

### **Example 5: Getting the Difference Between Dates**
```python
import datetime

date1 = datetime.date(2025, 3, 10)
date2 = datetime.date(2025, 3, 20)
difference = date2 - date1
print("Days difference:", difference.days)
```

---

## **Python Math**  
Python provides the `math` module for mathematical operations.

### **Example 1: Using Square Root and Power**
```python
import math

print(math.sqrt(16))
print(math.pow(2, 3))
```

### **Example 2: Trigonometric Functions**
```python
import math

print(math.sin(math.radians(30)))  # Convert degrees to radians
print(math.cos(math.radians(60)))
```

### **Example 3: Rounding Numbers**
```python
import math

print(math.ceil(4.3))  # Rounds up
print(math.floor(4.9))  # Rounds down
```

### **Example 4: Logarithmic Calculations**
```python
import math

print(math.log(10))   # Natural log
print(math.log10(100))  # Base-10 log
```

### **Example 5: Constants in Math Module**
```python
import math

print(math.pi)   # Pi constant
print(math.e)    # Euler's number
```

---

## **Python JSON**  
JSON (JavaScript Object Notation) is a popular format for data exchange.

### **Example 1: Converting Python Dictionary to JSON**
```python
import json

data = {"name": "Alice", "age": 25}
json_data = json.dumps(data)
print(json_data)
```

### **Example 2: Converting JSON to Python Dictionary**
```python
import json

json_data = '{"name": "Alice", "age": 25}'
data = json.loads(json_data)
print(data["name"])
```

### **Example 3: Writing JSON to a File**
```python
import json

data = {"name": "Bob", "age": 30}

with open("data.json", "w") as file:
    json.dump(data, file)
```

### **Example 4: Reading JSON from a File**
```python
import json

with open("data.json", "r") as file:
    data = json.load(file)
    print(data)
```

### **Example 5: Pretty-Printing JSON**
```python
import json

data = {"name": "Charlie", "age": 35, "city": "New York"}
print(json.dumps(data, indent=4, sort_keys=True))
```

---

## **Python RegEx**  
Regular expressions (`re` module) are used for pattern matching in strings.

### **Example 1: Checking if a String Contains a Pattern**
```python
import re

text = "The rain in Spain"
match = re.search("rain", text)
print(match is not None)  # Returns True if found
```

### **Example 2: Finding All Occurrences**
```python
import re

text = "hello 123, world 456"
matches = re.findall("\d+", text)  # Find all numbers
print(matches)
```

### **Example 3: Replacing a Pattern**
```python
import re

text = "hello world"
new_text = re.sub("world", "Python", text)
print(new_text)
```

### **Example 4: Splitting a String with a Pattern**
```python
import re

text = "apple,banana;cherry orange"
split_text = re.split("[,; ]", text)  # Split by comma, semicolon, or space
print(split_text)
```

### **Example 5: Extracting Email Addresses**
```python
import re

text = "Contact us at info@example.com or support@example.org"
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
print(emails)
```

---

## **Python PIP**  
PIP is the package manager for Python.

### **Example 1: Checking Installed PIP Version**
```sh
pip --version
```

### **Example 2: Installing a Package**
```sh
pip install requests
```

### **Example 3: Listing Installed Packages**
```sh
pip list
```

### **Example 4: Uninstalling a Package**
```sh
pip uninstall requests
```

### **Example 5: Upgrading a Package**
```sh
pip install --upgrade numpy
```

---

## **Python Try...Except**  
Used for handling exceptions (errors).

### **Example 1: Handling a Division by Zero Error**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### **Example 2: Handling Multiple Exceptions**
```python
try:
    x = int("hello")
except (ValueError, TypeError) as e:
    print("Error:", e)
```

### **Example 3: Using `finally`**
```python
try:
    print(1 / 1)
finally:
    print("This always executes")
```

### **Example 4: Using `else` with `try`**
```python
try:
    num = int("10")
except ValueError:
    print("Conversion error")
else:
    print("Conversion successful:", num)
```

### **Example 5: Raising an Exception**
```python
try:
    age = -1
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print(e)
```

---

## **Python String Formatting**  
Python offers different ways to format strings.

### **Example 1: Using `format()` Method**
```python
name = "Alice"
age = 25
print("My name is {} and I am {} years old".format(name, age))
```

### **Example 2: Using f-Strings (Python 3.6+)**
```python
name = "Bob"
age = 30
print(f"My name is {name} and I am {age} years old")
```

### **Example 3: Formatting Numbers**
```python
number = 123.456
print(f"Formatted number: {number:.2f}")  # Two decimal places
```

### **Example 4: Aligning Text**
```python
print(f"{'Left':<10} {'Center':^10} {'Right':>10}")
```

### **Example 5: Using Dictionaries in Formatting**
```python
data = {"name": "Charlie", "age": 35}
print("My name is {name} and I am {age} years old".format(**data))
```

### **1. Python Dates**
**Content:**
- Working with dates and times in Python.
- The `datetime` module.
- Creating, formatting, and manipulating dates.
- Time zones and daylight saving time.
- Common date operations (comparison, arithmetic, etc.).

**Examples:**
1. Get the current date and time using `datetime.now()`.
2. Create a specific date using `datetime.date()`.
3. Format a date as a string using `strftime()`.
4. Calculate the difference between two dates.
5. Extract the day, month, and year from a date.

**Additional Examples:**
6. Use `timedelta` to add or subtract days from a date.
7. Parse a string into a date using `strptime()`.
8. Compare two dates to see which is earlier.
9. Get the day of the week for a specific date.
10. Convert a date to a timestamp and vice versa.

---

### **2. Python Math**
**Content:**
- The `math` module and its functions.
- Common mathematical operations (square root, factorial, trigonometric functions, etc.).
- Constants like `pi` and `e`.
- Working with complex numbers using the `cmath` module.
- Random number generation with the `random` module.

**Examples:**
1. Calculate the square root of a number using `math.sqrt()`.
2. Compute the factorial of a number using `math.factorial()`.
3. Use `math.sin()`, `math.cos()`, and `math.tan()` for trigonometric calculations.
4. Generate a random number between 1 and 10 using `random.randint()`.
5. Calculate the value of `pi` using `math.pi`.

**Additional Examples:**
6. Use `math.log()` to calculate the natural logarithm of a number.
7. Round a number to the nearest integer using `math.round()`.
8. Calculate the greatest common divisor (GCD) using `math.gcd()`.
9. Use `cmath` to perform operations with complex numbers.
10. Shuffle a list using `random.shuffle()`.

---

### **3. Python JSON**
**Content:**
- What is JSON? (JavaScript Object Notation).
- The `json` module.
- Encoding Python objects to JSON (`json.dumps()`).
- Decoding JSON to Python objects (`json.loads()`).
- Working with JSON files.

**Examples:**
1. Convert a Python dictionary to a JSON string using `json.dumps()`.
2. Convert a JSON string to a Python dictionary using `json.loads()`.
3. Write a Python dictionary to a JSON file using `json.dump()`.
4. Read a JSON file into a Python dictionary using `json.load()`.
5. Pretty-print a JSON string with indentation.

**Additional Examples:**
6. Convert a list of dictionaries to a JSON array.
7. Handle non-serializable objects using a custom encoder.
8. Parse a JSON string with nested objects.
9. Validate JSON data using the `jsonschema` library.
10. Use `json.dumps()` with the `sort_keys` parameter to sort keys.

---

### **4. Python RegEx**
**Content:**
- What are regular expressions? (Pattern matching in strings).
- The `re` module.
- Common regex patterns (matching, searching, replacing).
- Groups and capturing matches.
- Flags for case-insensitive matching, multiline, etc.

**Examples:**
1. Use `re.search()` to find a pattern in a string.
2. Use `re.match()` to match a pattern at the beginning of a string.
3. Use `re.findall()` to find all occurrences of a pattern.
4. Use `re.sub()` to replace a pattern with a string.
5. Use groups to extract parts of a matched pattern.

**Additional Examples:**
6. Use `re.split()` to split a string by a pattern.
7. Match an email address using a regex pattern.
8. Use `re.IGNORECASE` for case-insensitive matching.
9. Match a multiline string using `re.MULTILINE`.
10. Use `re.compile()` to precompile a regex pattern.

---

### **5. Python PIP**
**Content:**
- What is PIP? (Python Package Installer).
- Installing, upgrading, and uninstalling packages.
- Listing installed packages.
- Using `requirements.txt` for dependency management.
- Virtual environments and `venv`.

**Examples:**
1. Install a package using `pip install`.
2. Upgrade a package using `pip install --upgrade`.
3. Uninstall a package using `pip uninstall`.
4. List installed packages using `pip list`.
5. Create a `requirements.txt` file and install dependencies.

**Additional Examples:**
6. Use `pip freeze` to generate a `requirements.txt` file.
7. Install a specific version of a package.
8. Use a virtual environment with `venv`.
9. Install packages from a `requirements.txt` file.
10. Use `pip show` to display information about an installed package.

---

### **6. Python Try...Except**
**Content:**
- What is exception handling? (Handling errors gracefully).
- The `try`, `except`, `else`, and `finally` blocks.
- Common built-in exceptions (`ValueError`, `TypeError`, `IndexError`, etc.).
- Raising exceptions with `raise`.
- Custom exceptions.

**Examples:**
1. Use `try` and `except` to handle a `ZeroDivisionError`.
2. Handle multiple exceptions in a single `try` block.
3. Use `else` to execute code when no exception occurs.
4. Use `finally` to execute cleanup code.
5. Raise a custom exception using `raise`.

**Additional Examples:**
6. Handle a `FileNotFoundError` when opening a file.
7. Use `try` and `except` to validate user input.
8. Create a custom exception class.
9. Use `try` and `except` to handle a `KeyError` in a dictionary.
10. Use `try` and `except` to handle a `TypeError`.

---

### **7. Python String Formatting**
**Content:**
- String formatting methods (`%`, `str.format()`, f-strings).
- Formatting numbers, dates, and strings.
- Alignment, padding, and precision.
- Common use cases for string formatting.

**Examples:**
1. Use the `%` operator to format a string.
2. Use `str.format()` to insert variables into a string.
3. Use f-strings for concise string formatting.
4. Format a floating-point number with precision.
5. Align text using formatting options.

**Additional Examples:**
6. Use f-strings to format a date.
7. Format a number with commas as thousand separators.
8. Use `str.format()` to format a table of data.
9. Use f-strings to embed expressions in a string.
10. Format a string with padding and alignment.

---

### **Additional Examples for Each Section**

#### **Python Dates**
11. Calculate the number of days between two dates.
12. Use `pytz` to work with time zones.
13. Get the current time in UTC.
14. Format a date in ISO format.
15. Calculate the age of a person given their birthdate.

#### **Python Math**
11. Calculate the hypotenuse of a right triangle using `math.hypot()`.
12. Use `math.ceil()` and `math.floor()` to round numbers.
13. Calculate the exponential value using `math.exp()`.
14. Use `math.degrees()` and `math.radians()` for angle conversion.
15. Generate a random float between 0 and 1 using `random.random()`.

#### **Python JSON**
11. Convert a JSON array to a Python list.
12. Handle JSON decoding errors using `try` and `except`.
13. Use `json.dumps()` with the `indent` parameter for pretty printing.
14. Merge two JSON objects.
15. Use `json.JSONEncoder` to create a custom JSON encoder.

#### **Python RegEx**
11. Match a phone number using a regex pattern.
12. Use `re.finditer()` to iterate over matches.
13. Match a URL using a regex pattern.
14. Use `re.sub()` with a function to replace matches.
15. Match a date in `YYYY-MM-DD` format using a regex pattern.

#### **Python PIP**
11. Install a package from a GitHub repository.
12. Use `pip cache` to manage the pip cache.
13. Install a package in a specific directory.
14. Use `pip check` to verify installed packages.
15. Install a package in editable mode for development.

#### **Python Try...Except**
11. Use `try` and `except` to handle a `ValueError`.
12. Handle a `KeyboardInterrupt` exception.
13. Use `try` and `except` to handle a `IndexError`.
14. Use `try` and `except` to handle a `AttributeError`.
15. Use `try` and `except` to handle a `ImportError`.

#### **Python String Formatting**
11. Use f-strings to format a multiline string.
12. Format a number as a percentage.
13. Use `str.format()` to format a dictionary.
14. Use f-strings to format a complex number.
15. Format a string with dynamic width and precision.


Certainly! Below is the structured outline for the sixth part of your Python course, including content and **5 Python sample codes** for each title. I've also added **5 more examples** for each section to ensure comprehensive coverage.

---

### **1. Python Dates**
**Content:**
- Working with dates and times in Python.
- The `datetime` module.
- Creating, formatting, and manipulating dates.
- Time zones and daylight saving time.
- Common date operations (comparison, arithmetic, etc.).

**Sample Codes:**
1. Get the current date and time using `datetime.now()`.
   ```python
   from datetime import datetime
   now = datetime.now()
   print(now)  # Output: Current date and time
   ```
2. Create a specific date using `datetime.date()`.
   ```python
   from datetime import date
   my_date = date(2023, 10, 5)
   print(my_date)  # Output: 2023-10-05
   ```
3. Format a date as a string using `strftime()`.
   ```python
   formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
   print(formatted_date)  # Output: Formatted date string
   ```
4. Calculate the difference between two dates.
   ```python
   date1 = date(2023, 10, 5)
   date2 = date(2023, 10, 10)
   delta = date2 - date1
   print(delta.days)  # Output: 5
   ```
5. Extract the day, month, and year from a date.
   ```python
   print(my_date.day, my_date.month, my_date.year)  # Output: 5 10 2023
   ```

**Additional Examples:**
6. Use `timedelta` to add or subtract days from a date.
   ```python
   from datetime import timedelta
   new_date = my_date + timedelta(days=7)
   print(new_date)  # Output: 2023-10-12
   ```
7. Parse a string into a date using `strptime()`.
   ```python
   date_str = "2023-10-05"
   parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
   print(parsed_date)  # Output: 2023-10-05 00:00:00
   ```
8. Compare two dates to see which is earlier.
   ```python
   date1 = date(2023, 10, 5)
   date2 = date(2023, 10, 10)
   print(date1 < date2)  # Output: True
   ```
9. Get the day of the week for a specific date.
   ```python
   print(my_date.weekday())  # Output: 3 (0 = Monday, 6 = Sunday)
   ```
10. Convert a date to a timestamp and vice versa.
    ```python
    timestamp = datetime.timestamp(now)
    print(timestamp)  # Output: Timestamp in seconds
    print(datetime.fromtimestamp(timestamp))  # Output: Converted back to datetime
    ```

---

### **2. Python Math**
**Content:**
- The `math` module and its functions.
- Common mathematical operations (square root, factorial, trigonometric functions, etc.).
- Constants like `pi` and `e`.
- Working with complex numbers using the `cmath` module.
- Random number generation with the `random` module.

**Sample Codes:**
1. Calculate the square root of a number using `math.sqrt()`.
   ```python
   import math
   print(math.sqrt(16))  # Output: 4.0
   ```
2. Compute the factorial of a number using `math.factorial()`.
   ```python
   print(math.factorial(5))  # Output: 120
   ```
3. Use `math.sin()`, `math.cos()`, and `math.tan()` for trigonometric calculations.
   ```python
   angle = math.radians(45)  # Convert degrees to radians
   print(math.sin(angle))  # Output: 0.7071
   ```
4. Generate a random number between 1 and 10 using `random.randint()`.
   ```python
   import random
   print(random.randint(1, 10))  # Output: Random number between 1 and 10
   ```
5. Calculate the value of `pi` using `math.pi`.
   ```python
   print(math.pi)  # Output: 3.141592653589793
   ```

**Additional Examples:**
6. Use `math.log()` to calculate the natural logarithm of a number.
   ```python
   print(math.log(10))  # Output: 2.302585092994046
   ```
7. Round a number to the nearest integer using `math.round()`.
   ```python
   print(round(3.14159, 2))  # Output: 3.14
   ```
8. Calculate the greatest common divisor (GCD) using `math.gcd()`.
   ```python
   print(math.gcd(12, 18))  # Output: 6
   ```
9. Use `cmath` to perform operations with complex numbers.
   ```python
   import cmath
   z = 3 + 4j
   print(cmath.phase(z))  # Output: Phase angle in radians
   ```
10. Shuffle a list using `random.shuffle()`.
    ```python
    my_list = [1, 2, 3, 4, 5]
    random.shuffle(my_list)
    print(my_list)  # Output: Shuffled list
    ```

---

### **3. Python JSON**
**Content:**
- What is JSON? (JavaScript Object Notation).
- The `json` module.
- Encoding Python objects to JSON (`json.dumps()`).
- Decoding JSON to Python objects (`json.loads()`).
- Working with JSON files.

**Sample Codes:**
1. Convert a Python dictionary to a JSON string using `json.dumps()`.
   ```python
   import json
   my_dict = {"name": "John", "age": 30}
   json_str = json.dumps(my_dict)
   print(json_str)  # Output: {"name": "John", "age": 30}
   ```
2. Convert a JSON string to a Python dictionary using `json.loads()`.
   ```python
   json_str = '{"name": "John", "age": 30}'
   my_dict = json.loads(json_str)
   print(my_dict)  # Output: {'name': 'John', 'age': 30}
   ```
3. Write a Python dictionary to a JSON file using `json.dump()`.
   ```python
   with open("data.json", "w") as file:
       json.dump(my_dict, file)
   ```
4. Read a JSON file into a Python dictionary using `json.load()`.
   ```python
   with open("data.json", "r") as file:
       data = json.load(file)
   print(data)  # Output: {'name': 'John', 'age': 30}
   ```
5. Pretty-print a JSON string with indentation.
   ```python
   print(json.dumps(my_dict, indent=4))
   ```

**Additional Examples:**
6. Convert a list of dictionaries to a JSON array.
   ```python
   my_list = [{"name": "John"}, {"name": "Jane"}]
   json_str = json.dumps(my_list)
   print(json_str)  # Output: [{"name": "John"}, {"name": "Jane"}]
   ```
7. Handle non-serializable objects using a custom encoder.
   ```python
   class Person:
       def __init__(self, name):
           self.name = name

   def encode_person(obj):
       if isinstance(obj, Person):
           return {"name": obj.name}
       raise TypeError("Object not serializable")

   person = Person("John")
   print(json.dumps(person, default=encode_person))  # Output: {"name": "John"}
   ```
8. Parse a JSON string with nested objects.
   ```python
   json_str = '{"name": "John", "address": {"city": "New York"}}'
   my_dict = json.loads(json_str)
   print(my_dict["address"]["city"])  # Output: New York
   ```
9. Validate JSON data using the `jsonschema` library.
   ```python
   from jsonschema import validate
   schema = {"type": "object", "properties": {"name": {"type": "string"}}}
   validate({"name": "John"}, schema)  # No error if valid
   ```
10. Use `json.dumps()` with the `sort_keys` parameter to sort keys.
    ```python
    print(json.dumps(my_dict, sort_keys=True))  # Output: Sorted JSON string
    ```

---

### **4. Python RegEx**
**Content:**
- What are regular expressions? (Pattern matching in strings).
- The `re` module.
- Common regex patterns (matching, searching, replacing).
- Groups and capturing matches.
- Flags for case-insensitive matching, multiline, etc.

**Sample Codes:**
1. Use `re.search()` to find a pattern in a string.
   ```python
   import re
   result = re.search(r"\d+", "I have 2 apples")
   print(result.group())  # Output: 2
   ```
2. Use `re.match()` to match a pattern at the beginning of a string.
   ```python
   result = re.match(r"\d+", "2 apples")
   print(result.group())  # Output: 2
   ```
3. Use `re.findall()` to find all occurrences of a pattern.
   ```python
   results = re.findall(r"\d+", "I have 2 apples and 3 bananas")
   print(results)  # Output: ['2', '3']
   ```
4. Use `re.sub()` to replace a pattern with a string.
   ```python
   new_text = re.sub(r"\d+", "X", "I have 2 apples")
   print(new_text)  # Output: I have X apples
   ```
5. Use groups to extract parts of a matched pattern.
   ```python
   result = re.search(r"(\d+) (\w+)", "2 apples")
   print(result.group(1), result.group(2))  # Output: 2 apples
   ```

**Additional Examples:**
6. Use `re.split()` to split a string by a pattern.
   ```python
   parts = re.split(r"\s+", "I have 2 apples")
   print(parts)  # Output: ['I', 'have', '2', 'apples']
   ```
7. Match an email address using a regex pattern.
   ```python
   email = "john.doe@example.com"
   result = re.match(r"[^@]+@[^@]+\.[^@]+", email)
   print(result.group())  # Output: john.doe@example.com
   ```
8. Use `re.IGNORECASE` for case-insensitive matching.
   ```python
   result = re.search(r"apple", "I have an Apple", re.IGNORECASE)
   print(result.group())  # Output: Apple
   ```
9. Match a multiline string using `re.MULTILINE`.
   ```python
   text = "Line 1\nLine 2\nLine 3"
   results = re.findall(r"^Line", text, re.MULTILINE)
   print(results)  # Output: ['Line', 'Line', 'Line']
   ```
10. Use `re.compile()` to precompile a regex pattern.
    ```python
    pattern = re.compile(r"\d+")
    print(pattern.findall("I have 2 apples"))  # Output: ['2']
    ```

---

### **5. Python PIP**
**Content:**
- What is PIP? (Python Package Installer).
- Installing, upgrading, and uninstalling packages.
- Listing installed packages.
- Using `requirements.txt` for dependency management.
- Virtual environments and `venv`.

**Sample Codes:**
1. Install a package using `pip install`.
   ```bash
   pip install numpy
   ```
2. Upgrade a package using `pip install --upgrade`.
   ```bash
   pip install --upgrade numpy
   ```
3. Uninstall a package using `pip uninstall`.
   ```bash
   pip uninstall numpy
   ```
4. List installed packages using `pip list`.
   ```bash
   pip list
   ```
5. Create a `requirements.txt` file and install dependencies.
   ```bash
   pip freeze > requirements.txt
   pip install -r requirements.txt
   ```

**Additional Examples:**
6. Use `pip freeze` to generate a `requirements.txt` file.
   ```bash
   pip freeze > requirements.txt
   ```
7. Install a specific version of a package.
   ```bash
   pip install numpy==1.21.0
   ```
8. Use a virtual environment with `venv`.
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```
9. Install packages from a `requirements.txt` file.
   ```bash
   pip install -r requirements.txt
   ```
10. Use `pip show` to display information about an installed package.
    ```bash
    pip show numpy
    ```

---

### **6. Python Try...Except**
**Content:**
- What is exception handling? (Handling errors gracefully).
- The `try`, `except`, `else`, and `finally` blocks.
- Common built-in exceptions (`ValueError`, `TypeError`, `IndexError`, etc.).
- Raising exceptions with `raise`.
- Custom exceptions.

**Sample Codes:**
1. Use `try` and `except` to handle a `ZeroDivisionError`.
   ```python
   try:
       result = 10 / 0
   except ZeroDivisionError:
       print("Cannot divide by zero!")
   ```
2. Handle multiple exceptions in a single `try` block.
   ```python
   try:
       result = int("abc")
   except (ValueError, TypeError):
       print("Invalid input!")
   ```
3. Use `else` to execute code when no exception occurs.
   ```python
   try:
       result = 10 / 2
   except ZeroDivisionError:
       print("Cannot divide by zero!")
   else:
       print("Result:", result)
   ```
4. Use `finally` to execute cleanup code.
   ```python
   try:
       result = 10 / 2
   except ZeroDivisionError:
       print("Cannot divide by zero!")
   finally:
       print("Execution complete!")
   ```
5. Raise a custom exception using `raise`.
   ```python
   try:
       raise ValueError("Invalid value!")
   except ValueError as e:
       print(e)  # Output: Invalid value!
   ```

**Additional Examples:**
6. Handle a `FileNotFoundError` when opening a file.
   ```python
   try:
       with open("nonexistent.txt", "r") as file:
           content = file.read()
   except FileNotFoundError:
       print("File not found!")
   ```
7. Use `try` and `except` to validate user input.
   ```python
   try:
       age = int(input("Enter your age: "))
   except ValueError:
       print("Invalid input! Please enter a number.")
   ```
8. Create a custom exception class.
   ```python
   class MyError(Exception):
       pass

   try:
       raise MyError("Something went wrong!")
   except MyError as e:
       print(e)  # Output: Something went wrong!
   ```
9. Use `try` and `except` to handle a `KeyError` in a dictionary.
   ```python
   my_dict = {"name": "John"}
   try:
       print(my_dict["age"])
   except KeyError:
       print("Key not found!")
   ```
10. Use `try` and `except` to handle a `TypeError`.
    ```python
    try:
        result = "10" + 5
    except TypeError:
        print("Cannot add string and integer!")
    ```

---

### **7. Python String Formatting**
**Content:**
- String formatting methods (`%`, `str.format()`, f-strings).
- Formatting numbers, dates, and strings.
- Alignment, padding, and precision.
- Common use cases for string formatting.

**Sample Codes:**
1. Use the `%` operator to format a string.
   ```python
   name = "John"
   age = 30
   print("Name: %s, Age: %d" % (name, age))  # Output: Name: John, Age: 30
   ```
2. Use `str.format()` to insert variables into a string.
   ```python
   print("Name: {}, Age: {}".format(name, age))  # Output: Name: John, Age: 30
   ```
3. Use f-strings for concise string formatting.
   ```python
   print(f"Name: {name}, Age: {age}")  # Output: Name: John, Age: 30
   ```
4. Format a floating-point number with precision.
   ```python
   pi = 3.14159
   print(f"Pi: {pi:.2f}")  # Output: Pi: 3.14
   ```
5. Align text using formatting options.
   ```python
   print(f"{'Name':<10} {name}")  # Output: Name       John
   ```

**Additional Examples:**
6. Use f-strings to format a date.
   ```python
   from datetime import datetime
   now = datetime.now()
   print(f"Today is {now:%Y-%m-%d}")  # Output: Today is 2023-10-05
   ```
7. Format a number with commas as thousand separators.
   ```python
   number = 1000000
   print(f"{number:,}")  # Output: 1,000,000
   ```
8. Use `str.format()` to format a table of data.
   ```python
   data = [("John", 30), ("Jane", 25)]
   for name, age in data:
       print("{:<10} {:>5}".format(name, age))  # Output: John         30
   ```
9. Use f-strings to embed expressions in a string.
   ```python
   x = 10
   y = 20
   print(f"The sum of {x} and {y} is {x + y}")  # Output: The sum of 10 and 20 is 30
   ```
10. Format a string with dynamic width and precision.
    ```python
    width = 10
    precision = 2
    print(f"{pi:{width}.{precision}f}")  # Output:      3.14
    ```





---

This structured content provides clear explanations and hands-on examples for each topic. Let me know if you need modifications or additional topics! 🚀
