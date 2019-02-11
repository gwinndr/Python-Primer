# Machine Learning Mini-Course - Clarkson University
# Spring 2019
# Author: Damon Gwinn

# Python Primer

# ASSUMPTIONS:
#   CS141 or equivalent - At least partway through

# The purpose of this primer is to get you comfortable with Python. Just about every modern
#   ML framework uses Python (Tensorflow, Scikit-Learn, etc.) so it is essential that you
#   get comfortable with this language.

# I put SELF-EVAL assignments where you should fill in the code.

###### COMMENTS ######

# You probably figured this out, but a '#' symbol denotes a line comment. It works exactly the
#   same as a C++ '//'

"""
    You can also use triple quotes to comment multi-line.

    I would avoid doing this, the triple quotes are typically only used for
    documenting code and could throw people off (editors tend to color these differently as well).
"""

###### MAIN ######

# These are imports
# Imports are packaged python library code
# Imports are referred to as 'modules' but don't let the fancy name fool you,
#   these are really just python files. (import sys means get sys.py)
import sys

# Let's define a main function as in C++.
# Python does not call this automatically. See the bottom of this file for more details.
def main(argc, argv):
    # Let's first print a 'hello world'
    # There's an easy way to do this with 'print'
    print("Hello from PythonPrimer!")

    # Python is dynamically typed. All this means is that python automatically
    #   assigns types to variables
    x = 5
    y = "hello"
    pi = 3.14159265354

    # str() converts stuff to strings
    print() # New line
    print("The variable x is " + str(x))
    print("Alternative way to say that x is %d" % x) # %d means 'digit' and the '%' populates it

    # SELF-EVAL:
    #   Print out y in the two print formats. %s denotes strings
    #   Print out pi in one of the two print formats.
    #     Precision should be only three decimal points (hint: %.3f)

    # Python automatically assigns variable types and allows you to mix and match
    # See how 'x' is an integer type. I'm going to just make it a string now. Python doesn't care.
    print()
    print("The type of x is " + str(type(x)))
    x = "5"
    print("The type of x is now " + str(type(x)))

    # SELF-EVAL:
    #   What do you think the type of x is now? Why?
    x = type(type(x))
    print("Finally, x is " + str(x))

    # Finally here's how you check if something is a certain type:
    if(isinstance(pi, float)):
        print("pi got caught as a float!")

    # Now for some helpful structures

    ##### LISTS ####
    # A 'list' works the same as a C++ vector. It is a resizable array of stuff
    #   Note that all items in a list do not need to be the same type
    print()
    li = list() # These are equivalents
    li = []
    li = [1, 2, 3, 4, 5]
    print("li: " + str(li))
    print("li[0]: " + str(li[0]))
    li.append(6)
    print("li.append(6): " + str(li))

    # Extend can be a nice method too. It puts all elements of one list onto the back of another
    li2 = [7,8,9]
    li.extend(li2)
    print("li.extend(): " + str(li))

    # Here's a fun one
    li3 = [1, "2", 3.0]
    print("li3: " + str(li3))

    # This will crash with a nice error message about indexing out of bounds
    # li3[100000]

    # SELF-EVAL:
    #   Create a list of lists, x, and print it out
    #   Append x with the number of lists inside using the len() function
    # EX: x -> [ [1,2], [3,4], [5,6], 3 ]

    ##### DICTS #####
    # This is the equivalent of a map in C++
    # It maps elements called 'keys' to different elements
    print()
    di = dict()
    di = {} # Same thing
    di["2"] = 2.0
    di["3"] = 3.0
    print("di is " + str(di))

    # What essentially happened is di["2"] = 2.0 first searches for a key of "2".
    #   Upon not finding it, it creates the key and sets it to map to the number 2.0
    # The 'indexing' operator [] works differently on dicts

    # Here's how to find a key
    di_2 = di.get("2")
    print("di_2 is " + str(di_2))
    di_5 = di.get("5") # This will return a special None type that literally means nothing
    if(di_5 is None):
        print("di_5 was nothing...")
    if(di_5 == None):
        print("Alternative way to say di_5 was nothing...")

    # SELF-EVAL:
    #   Make a dictionary of dictionaries representing a phon
    #   This should match a city dict to a person dict which maps to a phone number
    # EXAMPLE:
    #   potsdam_dict = city_dict["Potsdam"]
    #   potsdam_dict["John Doe"] gives a number of "123-456-7890"
    sample_dict = { "John Doe": "hello1",
                    "Jane Doe": "hello2" }

    ##### LOOPS #####
    # For loops work differently in python
    # For loops work on lists, these are called foreach loops
    print()

    # Lets go through from 0->5 and print out the numbers
    # First create an iteration range (works similar to a list)
    # You'll notice that '5' is not included
    inds = range(0, 5)
    print("inds: " + str(inds))
    for i in inds:
        print(i)
    print()

    # Lets iterate through li and put the double of these numbers in li_double
    li = [1,2,3,4,5]
    li_double = []
    for x in li:
        li_double.append(x * 2)
    print("li: " + str(li))
    print("li_double: " + str(li_double))

    # The above is good, but can be cumbersome to write (it's also slower)
    # List comprehension is a great way to make the above more concise
    # This will be useful when preparing training and test data as we'll see later
    li_double = [x * 2 for x in li]
    li_evens = [x for x in li
                if x % 2 == 0]
    print("li_double: " + str(li_double))
    print("li_evens: " + str(li_evens))

    # What do you think this will do?
    # It will double the SIZE of the list effectively, copying the list twice
    # It is equivalent to 'li.extend(li)'
    li_double2 = li * 2
    print("li_double2: " + str(li_double2))
    li.extend(li)
    print("li: " + str(li))

    # SELF-EVAL:
    #   Create a list of odd numbers in the range of 0 to 100 using for loops
    #   Do the same thing except using list comprehension

    ###### WHILE LOOPS ######
    # These are your average while loops, nothing special
    # They will keep evaluating until the condition is met
    print()
    x = 0
    print("while:")
    while(x < 6):
        print(x)
        x += 1

    # Hope this gave you a nice introduction to python
    # There's a lot I didn't cover, but this should give you a solid
    #   foundation to build off

    # SELF-EVAL
    #   Create a file 'PythonPrimerImport.py' in the same directory as PythonPrimer.py
    #   Have this file import PythonPrimer.py
    #   Call PythonPrimer.main with command line arguments
    # Hint:
    #   import PythonPrimer


# Python does not call the 'main function' in the way C++ does.
# In fact Python treats main the same as any other function.
#
# The one thing python does do to help us out is set a special '__name__' variable.
# This variable helps us differentiate between an imported file and a file run by calling
#   calling python on the command line.
#
# In our case, assuming you ran this file directly from the command line, this variable
#   is set to '__main__'. If you try importing this file from another python file,
#   you will see the else block run
#
# This is a very common python idiom. The reason for it, is when you import a python file
#   the file is actually run with __name__ set differently (feel free to experiment with this).
# What this means is that any code outside of this little if-else block is actually run.
if __name__ == "__main__":
    # The sys module has a neat little attribute called 'argv'.
    # This allows us to grab the command line arguments
    argc = len(sys.argv)
    main(argc, sys.argv)
else:
    # This is for instructional purposes, don't actually print that a file was imported
    print("PythonPrimer.py has been imported.")
