# variable rules
# 1. variable name can contain only letters, numbers, & underscores. (name cannot start with a number)
# 2. spaces are not allowed in a variable name (use underscore instead)
# 3. do not use python keywords
# 4. variable name should be short and descriptive
# 5. camel case is okay

# EX: 2.1
message = 'Hello from py3'
print(message)

# EX: 2.2
message ="Introduction to python"
print(message)

# EX: 2.3 concatenation of Strings
first_name = "chandan"
last_name = "thakur"
full_name = first_name + " " + last_name
message ="Hello, " +full_name.title()+ "!"
print(message)

# EX: 2.4 some String methods
name = 'chandan thakur'
print(name.title())
print(name.upper())
print(name.lower())

# EX: 2.5   EX: 2.6
quote = "A person who never made a mistake never tried anything new."
author_f_name = "Albert"
author_l_name = "Einstein"
author_full_name = author_f_name + " "+ author_l_name
print(author_full_name +' once said, "' + quote + '"')

# EX: 2.7 Escape characters
message = "\nnew line space"
print(message)
message = "\ttab"
print(message)
message = "\nLanguages: \n\tJava \n\tPython \n\tJavaScript \n\tAngular JS"
print(message)

# Striping whitespace
message = " Python "
print("\n1"+message + "1")
print("2"+message.rstrip() +"2")
print("3"+message.lstrip()+"3")
print(message.strip())

# Numbers and operations
# basic operations: + - * /
x = 5 + 5 - 3 * 10 / 6
print(x)
y = x ** 2
print (y)
# in python 2 if you divide 3/2 you will get 1; to avoid this make one of the numbers a float (3.0 or 2.0)

# EX: 2.8
a = 5 + 3
b = 11 - 3
c = 40 / 5
d = 4 * 2
print(a)
print(b)
print(c)
print(d)


# EX: 2.9 combine String and number
favorite_num = 7
message = "My favorite number is  " + str(favorite_num) + " or " + str(favorite_num*3)
print(message)
# without the str() method, you will get a typeError: can't convert 'int' object to str implicitly
