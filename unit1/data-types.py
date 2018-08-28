"""
Project:     Data Types Notes
Author:      Mr. Buckley
Last update: 8/25/2018
Description: Goes over comments, int, float, str, and type casting  
"""

# *** COMMENTS ***
# This is a comment (with a "#")
# Comments are only for the user's eyes, the program doesn't read them.
# Describe what sections of code do with a comment.
"""
This is a
multiline comment
"""

# *** DATA TYPE: INTEGER ***
# TODO: An integer number (no decimal)
integer = 5
print (integer)
print (type(integer))

# *** DATA TYPE: FLOAT ***
# TODO: A decimal number
decimal = 4.85
print (decimal)
print (type(decimal))

# *** DATA TYPE: STRING ***
# TODO: A string of characters enclosed in quotes
word = "these are my words"
print (word)
print (type(word))

# *** TYPE CASTING ***
# This converts one type to another

# TODO: Cast float to int
decimal = 55.55
dec_to_int = int(decimal)
print(dec_to_int)

# TODO: Cast int to string
number = "8"
print (int(number)+2)


# TODO: Cast number string to int
print ("give me add I'll add 1 to it")
number = float (input())
print (number + 1)

# TODO: Input demo (str to float)
