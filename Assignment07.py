# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: This is a functional script to demonstrate pickling and error
#              handling.
# ChangeLog (Who,When,What):
# Chrissy Henderson, 11.25.2020, Created script to complete assignment 7
# ---------------------------------------------------------------------------- #

# Pickling Demonstration------------------------------------------------------ #

# Data ----------------------------------------------------------------------- #
import pickle  # need to import the pickle module into the program

strFile = "File.txt"  # name of a file to write data to
data = {'Apple': 3, 'Banana': 8, 'Orange': 5}  # a list of dictionary data

outfile = open(strFile, "wb")  # opening the file in binary format for writing
readfile = open(strFile, "rb")  # opening the file in binary format for reading

# Processing ------------------------------------------------------------------ #
pickled_obj = pickle.dumps(data)  # pickles a data string
unpickled_obj = pickle.loads(pickled_obj)  # unpickles a data string

pickle.dump(data, outfile)  # pickles data and then writes it or "dumps" it to a file
outfile.close()  # closes the file

lstTable = pickle.load(readfile)  # loads in a pickled file
readfile.close()  # closes the file

input("Press Enter to Continue")





# -------------------------------------------------------------------------------#
# Error Handling Demonstration------------------------------------------------- #

# Presentation ---------------------------------------------------------------- #
class BigNumber(Exception):
    """ This number is way too big and should be lowered to less than 10 """
    # this is where a more detailed custom error message would go
    def __str__(self):
        return 'This number was too big!'


# Processing ------------------------------------------------------------------ #
try:
    x = 10/0
    if x > 10:
        raise BigNumber  # raise a custom error if the resulting integer is higher than 10
    y = int("a")  # causes an error that is not specifically called out
    f = open('OtherFile.txt', 'r+')  # the read plus option gives an error if file does not exist
except ZeroDivisionError as e:
    print("Zero cannot be used as the denominator!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except FileNotFoundError as e:
    print("Text file must exist before running this script!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except BigNumber as e:
    print(e)  # prints the error message we defined in the class earlier
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')

input()
