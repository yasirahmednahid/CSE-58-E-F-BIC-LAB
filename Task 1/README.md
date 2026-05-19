### **1. Python Input / Output**

Input is used to get data from the user, and output is used to display it to the screen.

```python
# Input: Getting data from the user (always returns a string)
name = input("Enter your name: ")

# Output: Displaying data to the screen
print("Hello,", name)

```

**You Do 1:** Write a short script that asks the user for their favorite color, and then prints `"Your favorite color is [color]!"`

---

### **2. Python Variables & Data Types**

Variables store data values. Python automatically assigns a data type (like integers, floats, or strings) when you create the variable.

```python
# Variables and Numbers (int and float)
age = 25
height = 5.9

# Strings and formatted strings (f-strings)
name = "Alice"
greeting = f"Hello, my name is {name} and I am {age} years old."

print(greeting)
print("Type of age:", type(age))

```

**You Do 2:** Create two variables: one for a movie title (string) and one for its release year (integer). Use an f-string to print them together in a sentence.

---

### **3. Python Operators**

Operators are used to perform operations on variables and values (Arithmetic, Comparison, Logical, etc.).

```python
a = 10
b = 3

# Arithmetic
addition = a + b      # 13
modulo = a % b        # 1 (Remainder of division)

# Comparison (Returns True or False)
is_greater = a > b    # True

# Logical
check_both = (a > 5) and (b < 5)  # True

print(f"Modulo: {modulo}, Is Greater: {is_greater}")

```

**You Do 3:** Create two variables holding numbers. Multiply them together. Print `True` if their product is greater than 50, and `False` otherwise, using comparison operators.

---

### **4. Python Lists**

Lists are ordered, changeable collections that allow duplicate values.

```python
fruits = ["apple", "banana", "cherry"]

# Adding an item
fruits.append("orange")

# Modifying an item
fruits[1] = "blueberry"

# Accessing an item
print(fruits[0])  # Output: apple
print(fruits)     # Output: ['apple', 'blueberry', 'cherry', 'orange']

```

**You Do 4:** Create a list of three of your favorite animals. Append a fourth animal to the end, then replace the second animal in the list with "Dragon". Print the final list.

---

### **5. Python Dictionaries**

Dictionaries store data values in **key:value** pairs. They are ordered and changeable.

```python
student = {
    "name": "John",
    "age": 22,
    "major": "Physics"
}

# Accessing a value using its key
print(student["name"])  # Output: John

# Adding a new key-value pair
student["graduated"] = False

# Modifying an existing value
student["age"] = 23

print(student)

```

**You Do 5:** Create a dictionary representing a car with keys for "brand" and "model". Then, add a new key "year" with an integer value, and print the dictionary.

---

### **6. Python If...Else**

Conditional statements execute different blocks of code based on whether a condition is True or False.

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C or lower")

```

**You Do 6:** Create a variable called `temperature`. Write an if/elif/else block that prints "It is hot" if the temperature is above 30, "It is nice" if it's between 20 and 30, and "It is cold" if it is below 20.

---

### **7. Python For Loops & Range**

A `for` loop is used for iterating over a sequence (like a list). The `range()` function is often used to repeat an action a specific number of times.

```python
# Iterating through a list
animals = ["cat", "dog", "bird"]
for animal in animals:
    print(animal)

# Using range(start, stop) to count
for i in range(2, 6):
    print(i, end=" ")  # Output: 2 3 4 5
print()

```

**You Do 7:** Use a `for` loop and the `range()` function to print the multiples of 5, starting from 5 and ending at 25 (inclusive).

---

### **8. Python Functions**

A function is a block of code which only runs when it is called. You can pass data (parameters) into it and return data back.

```python
# Defining a function
def add_numbers(num1, num2):
    result = num1 + num2
    return result

# Calling the function and storing the result
total = add_numbers(5, 7)
print("The total is:", total)

```

**You Do 8:** Write a function called `greet_user` that takes one parameter (`name`). Inside the function, return the string `"Welcome, [name]!"`. Call the function with your own name and print the result.
