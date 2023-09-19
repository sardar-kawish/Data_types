


# 1. **capitalize()**: Converts the first character to uppercase.

string = "hello, world"
result = string.capitalize()
print(result)  # Output: "Hello, world"

# 2. **casefold()**: Converts a string into lowercase, but more aggressively than `lower()`.

string = "HELLO, WoRLD"
result = string.casefold()
print(result)  # Output: "hello, world"

# 3. **center()**: Returns a centered string with a specified width.

string = "Python"
result = string.center(10, "*")
print(result)  # Output: "**Python**"

# 4. **count()**: Returns the number of times a specified value occurs in a string.

string = "Python is awesome, and Python is fun."
count = string.count("Python")
print(count)  # Output: 2


# 5. **encode()**: Returns an encoded version of the string.

string = "hello"
encoded = string.encode(encoding='utf-8')
print(encoded)  # Output: b'hello'


# 6. **endswith()**: Returns `True` if the string ends with the specified value.

string = "Hello, world!"
result = string.endswith("world!")
print(result)  # Output: True


# 7. **expandtabs()**: Sets the tab size of the string.

string = "Python\tis\tfun"
result = string.expandtabs(4)
print(result)  # Output: "Python  is  fun"


# 8. **find()**: Searches the string for a specified value and returns the position of where it was found.

string = "Hello, world!"
position = string.find("world")
print(position)  # Output: 7


# 9. **format()**: Formats specified values in a string.

name = "Alice"
age = 30
result = "My name is {} and I am {} years old.".format(name, age)
print(result)  # Output: "My name is Alice and I am 30 years old."

# 10. **format_map()**: Formats specified values in a string (similar to `format()`).

person = {'name': 'Bob', 'age': 25}
result = "My name is {name} and I am {age} years old.".format_map(person)
print(result)  # Output: "My name is Bob and I am 25 years old."
 
# 11. **index()**: Searches the string for a specified value and returns the position of where it was found. Similar to `find()` but raises an error if the value is not found.

string = "Hello, world!"
position = string.index("world")
print(position)  # Output: 7

# 12. **isalnum()**: Returns `True` if all characters in the string are alphanumeric (letters or digits).

string = "Python123"
result = string.isalnum()
print(result)  # Output: True

# 13. **isalpha()**: Returns `True` if all characters in the string are alphabetic (letters).

string = "Python"
result = string.isalpha()
print(result)  # Output: True
 
# 14. **isascii()**: Returns `True` if all characters in the string are ASCII characters.

string = "Hello"
result = string.isascii()
print(result)  # Output: True


# 15. **isdecimal()**: Returns `True` if all characters in the string are decimal (0-9) characters.

string = "12345"
result = string.isdecimal()
print(result)  # Output: True

# 16. **isdigit()**: Returns `True` if all characters in the string are digits.

string = "12345"
result = string.isdigit()
print(result)  # Output: True

# 17. **isidentifier()**: Returns `True` if the string is a valid Python identifier.

identifier = "my_variable"
result = identifier.isidentifier()
print(result)  # Output: True


# 18. **islower()**: Returns `True` if all characters in the string are lowercase.

string = "hello"
result = string.islower()
print(result)  # Output: True

# 19. **isnumeric()**: Returns `True` if all characters in the string are numeric.

string = "12345"
result = string.isnumeric()
print(result)  # Output: True

# 20. **isprintable()**: Returns `True` if all characters in the string are printable.

string = "Hello, world!"
result = string.isprintable()
print(result)  # Output: True

# 21. **isspace()**: Returns `True` if all characters in the string are whitespace characters.

string = " \t  \n"
result = string.isspace()
print(result)  # Output: True

# 22. **istitle()**: Returns `True` if the string follows the rules of a title.

string = "This Is a Title"
result = string.istitle()
print(result)  # Output: True

# 23. **isupper()**: Returns `True` if all characters in the string are uppercase.

string = "HELLO"
result = string.isupper()
print(result)  # Output: True

# 24. **join()**: Converts the elements of an iterable into a string.

words = ["Hello", "World"]
result = " ".join(words)
print(result)  # Output: "Hello World"

# 25. **ljust()**: Returns a left-justified version of the string.

string = "Python"
result = string.ljust(10, "*")
print(result)  # Output: "Python****"

# 26. **lower()**: Converts a string into lowercase.

string = "Hello, World!"
result = string.lower()
print(result)  # Output: "hello, world!"

# 27. **lstrip()**: Returns a left-trimmed version of the string.

string = " Hello, World!"
result = string.lstrip()
print(result)  # Output: "Hello, World!"

# 28. **maketrans()**: Returns a translation table to be used in translations (usually used with `translate()`).

from string import maketrans
string = "Hello"
translation = maketrans("H", "J")
result = string.translate(translation)
print(result)  # Output: "Jello"

# 29. **partition()**: Returns a tuple where the string is parted into three parts based on a specified separator.

string = "Hello, World!"
parts = string.partition(", ")
print(parts)  # Output: ('Hello', ', ', 'World!')

# 30. **replace()**: Returns a string where a specified value is replaced with another specified value.

string = "Hello, World!"
result = string.replace("World", "Python")
print(result)  # Output: "Hello, Python!"

# 31. **rfind()**: Searches the string for a specified value and returns the last position where it was found.

string = "Hello, World, World!"
position = string.rfind("World")
print(position)  # Output: 13

# 32. **rindex()**: Searches the string for a specified value and returns the last position where it was found.

string = "Hello, World, World!"
position = string.rindex("World")
print(position)  # Output: 13

# 33. **rjust()**: Returns a right-justified version of the string.

string = "Python"
result = string.rjust(10, "*")
print(result)  # Output: "****Python"

# 34. **rpartition()**: Returns a tuple where the string is parted into three parts based on a specified separator, starting from the right.

string = "Hello, World!"
parts = string.rpartition(", ")
print(parts)  # Output: ('Hello, World', '!', '')

# 35. **rsplit()**: Splits the string at the specified separator, starting from the right, and returns a list.

string = "apple, banana, cherry"
result = string.rsplit(", ")
print(result)  # Output: ['apple', 'banana', 'cherry']

# 36. **rstrip()**: Returns a right-trimmed version of the string.

string = "Hello, World!"
result = string.rstrip()
print(result)  # Output: "Hello, World!"

# 37. **split()**: Splits the string at the specified separator and returns a list.

string = "apple, banana, cherry"
result = string.split(", ")
print

(result)  # Output: ['apple', 'banana', 'cherry']

# 38. **splitlines()**: Splits the string at line breaks and returns a list.

string = "Line 1\nLine 2\nLine 3"
result = string.splitlines()
print(result)  # Output: ['Line 1', 'Line 2', 'Line 3']

# 39. **startswith()**: Returns `True` if the string starts with the specified value.

string = "Hello, World!"
result = string.startswith("Hello")
print(result)  # Output: True

# 40. **strip()**: Returns a trimmed version of the string (both left and right).

string = " Hello, World!"
result = string.strip()
print(result)  # Output: "Hello, World!"

# 41. **swapcase()**: Swaps cases - lower case becomes upper case and vice versa.

string = "Hello, World!"
result = string.swapcase()
print(result)  # Output: "hELLO, wORLD!"

# 42. **title()**: Converts the first character of each word to uppercase.

string = "hello world"
result = string.title()
print(result)  # Output: "Hello World"

# 43. **translate()**: Returns a translated string using a translation table (often created with `maketrans()`).

from string import maketrans
string = "Hello"
translation = maketrans("H", "J")
result = string.translate(translation)
print(result)  # Output: "Jello"

# 44. **upper()**: Converts a string into uppercase.

string = "Hello, World!"
result = string.upper()
print(result)  # Output: "HELLO, WORLD!"

# 45. **zfill()**: Fills the string with a specified number of '0' values at the beginning to make it a specified width.

number = "42"
result = number.zfill(5)
print(result)  # Output: "00042"
