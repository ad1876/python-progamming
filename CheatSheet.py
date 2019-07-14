
# import is used to make speciality functions available
# These are called modules

import random
import sys
import os


# region BASICS ---------
# Hello world is just one line of code
# print() outputs data to the screen

print('Hello World!')

'''
This is a multi-line comment
'''

# A variable is a place to store values
# Its name is like a label for that value

name = "Adnan Begovic"
print(name)

# A variable name can contain letters, numbers, or _
# But can't start with a number

# There are 5 data types Numbers, Strings, Lists, Tuple, Dictionary
# You can store any of them in the same variable
name = 15
print(name)
# endregion ------

# region ARITHMETIC ---------
# The arithmetic operators: + - * / % ** //
# ** Exponential calculation
# // Floor Division
print("5 + 2 =", 5 + 2)  # 7
print("5 - 2 =", 5 - 2)  # 3
print("5 * 2 =", 5 * 2)  # 10
print("5 / 2 =", 5 / 2)  # 2.5
print("5 % 2 =", 5 % 2)  # 1
print("5 ** 2 =", 5 ** 2)  # 25
print("5 // 2 =", 5 // 2)  # 2
# Order of Operation state * and / is performed before + and -
print('1 + 2 - 3 * 2 =', 1 + 2 - 3 * 2)  # -3
print("(1 + 2 - 3 ) * 2 = ", (1 + 2 - 3) * 2)  # 0
# endregion

# region STRINGS ---------

# A string is a string of characters surrounded by " or '
# If you must use a " or ' between the same quote escape it with \
quote = "\"If you can't find something to live for, u best find something to die for!\""
print(quote)
# A multi-line quote
multi_line_quote = ''' Just like everyone else!'''
print(quote + multi_line_quote)

# To embed a string in output use %s
quote = "If you can't find something to live for, u best find something to die for!"
print("%s%s%s%s" % ("\"This is a quote by Adnan: ", quote, multi_line_quote, "\""))

# To keep from printing newlines use end=""
print("Hej jag heter Adnan", end="")
print(" Begovic.")

# You can print strings multiple times with *
print("Adnan Begovic\n" * 5)

# endregion

# region LISTS ---------
# A list allows you to create a list of values and manipulate them
# Each value has an index with the first one starting at 0
grocery_list = ["Juice", "Tomatoes", "Potatoes", "Bananas"]
print('The last item is: ' + grocery_list[3])

# You can change the value stored in a list box
grocery_list[0] = "Apple Juice"
print(grocery_list)

# You can get a subset of the list with [min:up to but not including max]
print(grocery_list[1:3])

# You can put any data type in a list including a list
other_events = ['Wash Car', 'Pick up Kids', "Cash Check"]
to_do_list = [other_events, grocery_list]
print(to_do_list)

# Get the second item in te second list (Boxes inside of boxes)
print(to_do_list[1][1])

# You add values using append
grocery_list.append("Paprika")
print(grocery_list)

# Insert item at given index
grocery_list.insert(1, "Apples")
print(grocery_list)

# Remove item from list
grocery_list.remove("Apple Juice")
print(grocery_list)

# Sorts items in list
grocery_list.sort()

# Reverse items in list
grocery_list.reverse()

# del deletes an item at a specified index
del grocery_list[2]

# We can combine a list with a +
to_do_list = other_events + grocery_list
print(to_do_list)

# Get length of a list
print(len(to_do_list))

# Get the max item in list
print(max(to_do_list))

# Get the min item in list
print(min(to_do_list))

# endregion

# region TUPLES ---------
# Values in tuples can't change like lists
pi_tuple = (9, 3, 5, 3, 2, 6)
print(pi_tuple)

# Convert a tuple into a list
ConvertTuple_List = list(pi_tuple)
print(ConvertTuple_List)

# Convert a list into a tuple
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print(grocery_list)
ConvertList_Tuple = tuple(grocery_list)
print(ConvertList_Tuple)

# Tuples also have len(tuple), min(tuple) and max(tuple)
abc_tuple = ('a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4')
print(len(abc_tuple))
print(min(abc_tuple))
print(max(abc_tuple))

# endregion

# region DICTIONARY or MAP ---------
# Made up of values with a unique key for each value
# Similar to lists, but you can't join dicts with a +
football_players = {
    'Forward': 'Zlatan Ibrahimovic',
    'Defender': 'Marcelo',
    'GoalKeeper': 'Buffon',
    'CenterForward': 'Messi',
    'RightForward': 'Cristiano'
}
print(football_players['Forward'])

# Delete an entry
del football_players['Defender']
print(football_players)

# Replace a value
football_players['GoalKeeper'] = 'Casillias'

# Print the number of items in a dictionary
print(len(football_players))

# Get the value for the passed key
print(football_players.get("Forward"))

# Get a list of dictionary keys
print(football_players.keys())

# Get a list of dictionary values
print(football_players.values())
# endregion

# region CONDITIONALS ---------
# The if, else, and elif statements are used to perform different actions based on conditions
# Comparision Operators: ==, !=, >, <, >=, <=

# The if statement will execute a block of code if a condition is met
# Whitespace is used to group blocks of code in Python
# Use the same number of proceeding spaces for blocks of code
age = 30
if age > 16:
    print('You are old enough to drive')

# Use an if statement if you want to execute different code regardless
# of whether the condition was met or not
if age > 16:
    print("You are old enough to drive")
else:
    print("You are not old enough to drive")

# If you want to check for multiple conditions use elif
# If the first matches it won't check other conditions

if age >= 21:
    print('You are old enough to drive a tractor trailer')
elif age >= 16:
    print('You are old enough to drive a car')
else:
    print('You are not old enough to drive')

# You can combine conditions with logical operators
# Logical Operators: and, or, not

if (age >= 1) and (age <= 18):
    print('A: Congratulations, you get a BD-Party!')
elif(age == 21) or (age >= 65):
    print('B: Congratulations, you get a BD-Party!')
elif not (age == 30):
    print("C: You don't get a birthday party!")
else:
    print("D: You get a birthday party yeah")

# endregion

# region FOR LOOPS ---------
# Allows you to perform an action a set number of times
# Range performs the action 10 times 0 - 9

for x in range(0, 10):
    print(x, " ", end="")

# You can use loops to cycle through lists
footballStars_list = ['Zlatan', 'Cristiano', 'Ronaldinho', 'Messi', 'Neymar']
for stars in footballStars_list:
    print(stars)

# You can also define a list of numbers to cycle through
for x in [3, 4, 5, 6]:
    print(x, "", end="")

# You can double up for loops to cycle through lists
num_list = [[1, 2, 3, 4, 5], [10, 20, 30, 40, 50], [100, 200, 300, 400, 500]]

for x in range(0, 3):
    for y in range(0, 5):
        print(num_list[x][y], " ", end=" ")

# endregion

# region WHILE LOOPS --------
'''While loops are used when you don't know ahead of time how many times 
   you will have to loop '''
randomNumber = random.randrange(0, 10)
while randomNumber != 12:
    print(randomNumber, end=" ")
    randomNumber = random.randrange(0, 100)

# An iterator for a while loop is defined before the loop
i = 0
while i <= 20:
    if i % 2 == 0:
        print(i)
    elif i == 9:
        # Forces the loop to end all together
        break
    else:
        # Shorthand for i = i + 1
        i += 1
        # Skips to the next iteration of the loop
        continue
    i += 1

# endregion

# region FUNCTIONS --------
# Functions allow you to reuse and write readable code
# Type def(define), function name and parameters it receives
# return is used to return something to the caller of the function


def add_numbers(f_num, s_num):
    sum_num = f_num + s_num
    return sum_num


print(add_numbers(3, 4))

# Can't get the value of sum_num because it was created in a function
# It is said to be out of scope
# print(sum_num)

# If you define a variable outside of the function it works every place
# new_num = 0


def sub_numbers(f_num, s_num):
    new_num = f_num - s_num
    return new_num


print(sub_numbers(4, 2))


# endregion

# region USER INPUT --------

print("What is your name ?")
# Stores everything you type until you hit ENTER
name = sys.stdin.readline()
print("Hello", name)

# endregion

# region STRINGS --------
# A string is a series of characters surrounded by ' or ""
long_string = "Hej jag heter Adnan Begovic och jag bor i Trelleborg"

# Retrieve the first 3 characters
print(long_string[0:3])  # Hej

# Get the last 10 characters
print(long_string[-10:])  # Trelleborg

# Retrieve characters between index 24-27
print(long_string[14:27])  # Adnan Begovic

# Concatenate part of a string to another
print(long_string[:3] + " Världen!")  # Hej Världen!

# String formatting %c = character, %s = string, %d = integer, %f = float
print("Bokstaven %c är första tecknet i mitt förnamn \'%s\'."
      " Jag är %d år gammal och jag %f m lång." % ('A','Adnan', 25, 1.84))

# Capitalizes the first letter
first_name = 'adnan'
print(first_name.capitalize())

# Returns the index of the start of the string
# case sensitive
print(long_string.find("Adnan"))

# Returns true if all characters are letters without any space or special chars e.g. " " % '
print(long_string.isalpha())

# Remove white space from front and end
front_back_whitespace = "            Adnan    Begovic            "
print(front_back_whitespace.strip())

# Split a string into a list based on the delimiter you provide
quote_list = long_string.split(" ")
print(quote_list)


# endregion

# region FILE Objects I/O ----------

# Overwrite or create a file for writing in binary mode('wb')
notes_file = open("notes.txt", "wb")  # note! open-commands needs to be closed.
# different_filemodes = ['w = write', 'r = read', 'a = append', 'r+ = readAndWrite', 'wb = write-binary mode']
# Get the file mode used
print(notes_file.mode)
# Get the file name
print(notes_file.name)
# Write text to a file with a newline
notes_file.write(bytes("Write me to the file\n", 'UTF-8'))
#  It is important to explicitly close the file that we have opened.
notes_file.close()


# Opens a file for reading and writing
notes_file = open('notes.txt', 'rb+')
# Write text with swedish chars to a file with a newline
notes_file.write(bytes('Svenska tecken som t.ex. \"öäå\" hanteras med bytes & UTF-8!\n', 'UTF-8'))
# It is important to explicitly close the file that we have opened.
notes_file.close()


# Opens a file for reading and writing with utf-8 encoding
notes_file = open('notes.txt', 'r+', encoding='utf-8')
text = notes_file.read()
notes_file.close()
print(text)

# Delete the file
os.remove('notes.txt')

# Context Manager ---------------------------------------
# When dealing with File objects in Python, it is recommended to use an context manager,
# since u don't have to worry about closing a file, this is done automatically.

# Open a file for reading and writing with context manger
# Note! that 'rb+' can't be used if the file doesn't exits. If that's the case use 'wb' instead.
with open('notes.txt', 'rb+') as text:
    # Specify encoding with bytes for special chars.
    text.write(bytes('My name: \"Adnan\" does not contain any swedish chars like e.g: Ö Ä Å!\n', 'utf-8'))

# Open and encode a file for reading
# Print file- name, file- mode and encoded notes.
with open('notes.txt', 'r+', encoding='utf-8') as text:
    print(text.name)
    print(text.mode)
    notes = text.read()
    print(notes)

# Set the number of chars to read from a file and print current char-position.
with open('notes.txt', 'r', encoding='utf-8') as text:
    number_of_chars = 73
    notes = text.read(number_of_chars)  # read number of chars in file.
    print(notes)
    print(text.tell())  # tell func. determines current char-position in file.
    print(text.seek(0))  # seek func. starts at given char-position in file

# This code snippet can be used to read a large text file with iteration
with open('notes.txt', 'r', encoding='utf-8') as text:
    size_to_read = 10
    notes = text.read(size_to_read)
    while len(notes) > 0:
        print(notes, end='*')
        # print(text.tell(), end='')
        notes = text.read(size_to_read)

# Open and write a to-do list that will be read with other commands like: readline(), readlines().
with open('todo_list.txt', 'wb+') as text:
    text.write(bytes('1. Jobba.\n2. Träna.\n3. Äta.\n4. Sova.\n', 'utf-8'))

with open('todo_list.txt', 'r', encoding='utf-8') as text:
    content = text.readline()
    # content = text.readlines()
    print(content)

# Make a copy of a file, by reading file A.txt and write to file B.txt with encoding.
# To be able to execute the following code snippet a file A.txt needs to be created.
with open('A.txt', 'r', encoding='utf-8') as rf:
    with open('B.txt', 'wb') as wf:
        content = rf.read()
        write_content = wf.write(bytes(content, 'utf-8'))

# Make a copy of a file, by reading file todo_list.txt and write to file B.txt with encoding.
# To be able to execute the following code snippet a file A.txt needs to be created.
with open('todo_list.txt', 'r', encoding='utf-8') as rf:
    with open('B.txt', 'wb') as wf:
        for char in rf:
            wf.write(bytes(char, 'utf-8'))


# Make a copy of picture: The picture needs to be placed in root directory first.
# Use bytes when dealing with images.
with open('Capture.PNG', 'rb') as read_image:
    with open('copy_Capture.PNG', 'wb') as write_image:
        rf = read_image.read()
        write_image.write(bytes(rf))

# remove something from OS
os.remove('Capture.PNG')
os.remove('copy_Capture.PNG')
os.remove('A.txt')
os.remove('B.txt')
os.remove('notes.txt')
os.remove('todo_list.txt')

# endregion_-----

# region CLASSES AND OBJECTS -------------
# The concept of OOP allows us to model real world things using code
# Every object has attributes (color, height, weight) which are object variables
# Every object has abilities (walk, talk, eat) which are object functions

class Animal:
    # None signifies the lack of a value
    # You can make a variable private by starting it with __
    __name = None
    __height = None
    __weight = None
    __sound = None

    # The constructor is called to set up or initialize an object
    # self allows an object to refer to itself inside of the class
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def set_height(self, height):
        self.__height = height

    def set_weight(self, height):
        self.__height = height

    def set_sound(self, sound):
        self.__sound = sound

    def get_name(self):
        return self.__name

    def get_height(self):
        return str(self.__height)

    def get_weight(self):
        return str(self.__weight)

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}".format(self.__name, self.__height, self.__weight, self.__sound)

# How to create a Animal object
cat = Animal('Whiskers', 33, 10, 'Meow')

print(cat.toString())

# You can't access this value directly because it is private
#print(cat.__name)

# endregion

# region INHERITANCE -------------
# You can inherit all of the variables and methods from another class.


class Dog(Animal):
    __owner = None

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        self.__animal_type = None

        # How to call the super class constructor
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print ("Dog")

    # We can overwrite functions in the super class
    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}. His owner is {}".format(self.get_name(), self.get_height(), self.get_weight(), self.get_sound(), self.__owner)

    # You don't have to require attributes to be sent
    # This allows for method overloading
    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound)
        else:
            print(self.get_sound() * how_many)

spot = Dog("Spot", 53, 27, "Ruff", "Derek")

print(spot.toString())

# Polymorphism allows use to refer to objects as their super class
# and the correct functions are called automatically

class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(spot)

spot.multiple_sounds(4)
# endregion









