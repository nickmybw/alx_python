Python - Data Structures: Lists, Tuples
Python

Read or watch:

3.1.3. Lists
Data structures (until 5.3. Tuples and Sequences included)
Learn to Program 6 : Lists
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why Python programming is awesome
What are lists and how to use them
What are the differences and similarities between strings and lists
What are the most common methods of lists and how to use them
How to use lists as stacks and queues
What are list comprehensions and how to use them
What are tuples and how to use them
When to use tuples versus lists
What is a sequence
What is tuple packing
What is sequence unpacking
What is the del statement and how to use it
Requirements
Python Scripts
Recommended editor: Visual studio code
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7.*)
The length of your files will be tested using wc
Quiz questions
Great! You've completed the quiz successfully! Keep going! (Show quiz)
Tasks
0. Can you C me now?
mandatory
Write a function that removes all characters c and C from a string.

Prototype: def no_c(my_string):
The function should return the new string
You are not allowed to import any module
You are not allowed to use str.replace()
guillaume@ubuntu:~/$ cat 0-main.py
# !/usr/bin/env python3
no_c = __import__('0-no_c').no_c

print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

guillaume@ubuntu:~/$ ./0-main.py
Holberton Shool
hiago
 is fun!
guillaume@ubuntu:~/$
Repo:

GitHub repository: alx_python
Directory: python-data_structures
File: 0-no_c.py
  
0/10 pts

1. Lists of lists = Matrix
mandatory
Write a function that prints a matrix of integers.

Prototype: def print_matrix_integer(matrix=[[]]):
Format: see example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers
guillaume@ubuntu:~/$ cat 1-main.py
# !/usr/bin/python3
print_matrix_integer = __import__('1-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

guillaume@ubuntu:~/$ ./1-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/$
Repo:

GitHub repository: alx_python
Directory: python-data_structures
File: 1-print_matrix_integer.py
