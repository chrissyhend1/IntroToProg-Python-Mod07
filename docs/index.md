Chrissy Henderson  
November 27, 2020  
IT FDN 110 A Au 20: Foundations Of Programming: Python  
Assignment 07  
https://github.com/chrissyhend1/IntroToProg-Python-Mod07  
# Demonstrating Pickling and Error Handling  

## Introduction
Pickling is a way to convert data to and from binary objects to make the data "sterile". This data is not entirely secure, however, and should not be treated as such, but it does make the data more difficult to read using the naked eye. This process also makes files smaller therefor making them easier to transfer over a network or store in memory. This pickling process is unique to Python and cannot be used with other programming languages.  
Errors are an expected issue when running any kind of code in Python. Error handling can be used to present custom messages when certain errors are encountered and give a user a more descriptive and more simplified reason why the code failed. Multiple "try-except" blocks can be used to catch multiple different errors and present different messages to the users. 

## Pickling in Python  
There are four main ways to pickle and unpickle data including "dump", "dumps", "load", and "loads". In this example, we will first need to import the pickle program, set up a file name, and set up a new line of dictionary data to work with (Figure 1).

![Figure 1](https://github.com/chrissyhend1/IntroToProg-Python-Mod07/blob/main/docs/Fig1.PNG "Figure1")  
Figure 1. Importing pickle into Python and setting up the file name and list of dictionary data.

The second step is to create two lines that will open files in two different modes. We want to be able to open a file in "write" mode which usually involves adding a "w" at the end of the open string. However, because we will be working in binary, we will need to open the file in "wb" mode with the "b" standing for binary. The second line is similar but will involve putting "rb" at the end of the line to open and read the file in binary mode (Figure 2).

![Figure 2](https://github.com/chrissyhend1/IntroToProg-Python-Mod07/blob/main/docs/Fig2.PNG "Figure2")  
Figure 2. Opening the file in binary write mode and binary read mode respectively

"Dumps" and "loads" works with each other in that they pickle and unpickle strings of data as indicated by the "s" at the end of the words (Figure 3). This is a simple process, but these two functions rely on each other. A user will not be able to work with strings that have been pickled like they can with unpickled strings. This data needs to be unpickled first. "Dump" and "load" are very similar in that they involve pickling and unpickling data but the process it done to and from text file outside of python (Figure 4 & 5). 

![Figure 3](https://github.com/chrissyhend1/IntroToProg-Python-Mod07/blob/main/docs/Fig3.PNG "Figure3")  
Figure 3. Pickling and unpickling a string of data

![Figure 4](https://github.com/chrissyhend1/IntroToProg-Python-Mod07/blob/main/docs/Fig4.PNG "Figure4")  
Figure 4. Pickling data and saving it to a file in "wb"mode  

![Figure 5](https://github.com/chrissyhend1/IntroToProg-Python-Mod07/blob/main/docs/Fig5.PNG "Figure5")  
Figure 5. Unpickling data from a file where the file is in "rb" mode

As you can see from the text file, the code successfully pickled the data into a text file (Figure 6).

![Figure 6](https://github.com/chrissyhend1/IntroToProg-Python-Mod07/blob/main/docs/Fig6.PNG "Figure6")  
Figure 6. The pickled text file

The code successfully ran in Windows command shell because it pickled and unpickled that data without any errors and stopped at the input step I programmed in (Figure 7).

![Figure 7](https://github.com/chrissyhend1/IntroToProg-Python-Mod07/blob/main/docs/Fig7.PNG "Figure7")  
Figure 7. Code successfully ran in Windows command shell

## Error Handling in Python
Error handling is a very useful technique in Python to help users better understand why the error is occuring and simplifying the messaging presented to the user. This is done in what is called a "try-except" block. The program will "try" the code, and if the program encounters an error, then the program will cycle through the "except" portion of the code. In this exercise, I explore several different errors that are built into Python as well as how to create a custom error.
The first error we will be looking at is the ZeroDivisionError. This is a built in error that occurs when a number is attempting to be divided by 0. For example, we will "try" to set "x" to be equal to 10 divided by 0 (Figure 8).

![Figure 8](https://github.com/chrissyhend1/IntroToProg-Python-Mod07/blob/main/docs/Fig8.PNG "Figure8")  
Figure 8. Setting up "x" to equal 10 divided by 0 in the try portion of the program

After this is tried by the program, the program will hit an error and therefor run through the except portion. When it hits the correct except portion (which in this case is for the ZeroDivisionError), the program will run through the code displayed in Figure 9. First, the program will save the error as the variable "e". Then the program will print the custom message that zero cannot be the denominator and then follow this up with the built-in Python error information that had been saved as "e". The third print line will print the Python error, the documentation for said error, the type of the error, and separate these each by a new line (Figure 10 & 11).


![Figure 9](https://github.com/chrissyhend1/IntroToProg-Python-Mod07/blob/main/docs/Fig9.PNG "Figure9")  
Figure 9. The except code block for the error ZeroDivisionError

![Figure 10](https://github.com/chrissyhend1/IntroToProg-Python-Mod07/blob/main/docs/Fig10.PNG "Figure10")  
Figure 10. The output in PyCharm IDE from the program after a ZeroDivisionError has occured

![Figure 11](https://github.com/chrissyhend1/IntroToProg-Python-Mod07/blob/main/docs/Fig11.PNG "Figure11")  
Figure 11. The error message as seen in the Windows command shell

The second error I have set up is a custom error. As long as the error is set up as an exception before running the "try-except" block, the program will be able to run this custom error (Figure 12).

![Figure 12](https://github.com/chrissyhend1/IntroToProg-Python-Mod07/blob/main/docs/Fig12.PNG "Figure12")  
Figure 12. The class code block used to define the custom "BigNumber" error

This custom error is set up to run if x is greater than 10. To do this, I made it so when x was created, it would equal 20 and therefor trigger the error. Python would not normally hit an error for this process, so I needed to add a line that would "raise" the exception if this certain requirement was met. Additionally, this piece needs to be in the "try" portion of the block or else it will not error out (Figure 13).

![Figure 13](https://github.com/chrissyhend1/IntroToProg-Python-Mod07/blob/main/docs/Fig13.PNG "Figure13")  
Figure 13. The try portion of the program that will raise the BigNumber error if x is greater than 10

When the exception "BigNumber" is triggered, the "try-except" block will stop at the "except BigNumber" line, store the error as "e", and print out the error that was defined in the custom exception creation earlier (Figure 9). When printing out the "doc" amd "type" as done for the previous error, Python will only print what I defined in the description of the error myself (Figure 14 & 15).

![Figure 14](https://github.com/chrissyhend1/IntroToProg-Python-Mod07/blob/main/docs/Fig14.PNG "Figure14")  
Figure 14. The except code block for the BigNumber error

![Figure 15](https://github.com/chrissyhend1/IntroToProg-Python-Mod07/blob/main/docs/Fig15.PNG "Figure15")  
Figure 15. The output in PyCharm IDE from the program after the custom error BigNumber has occured

The next error we will explore is an all encompassing error. If an error occurs in the "try" portion and does not fall into any of the other exceptions, this error will be thrown. I have fixed the previous statements to not cause errors before reaching this line as well. In this case, I told the program to try to convert the letter "a" to an integer which is not possible (Figure 16). Since this error does not fit the other three errors that I defined, it called the last one on the list. The except block will print that the error is non-specific and then proceed to print out the built-in error information (Figure 17 & 18).

![Figure 16](https://github.com/chrissyhend1/IntroToProg-Python-Mod07/blob/main/docs/Fig16.PNG "Figure16")  
Figure 16. The try portion of the code that will cause an error if "a" is converted to an integer

![Figure 17](https://github.com/chrissyhend1/IntroToProg-Python-Mod07/blob/main/docs/Fig17.PNG "Figure17")  
Figure 17. The except code block for the non-specific error

![Figure 18](https://github.com/chrissyhend1/IntroToProg-Python-Mod07/blob/main/docs/Fig18.PNG "Figure18")  
Figure 18. The output in PyCharm IDE from the program after a ValueError has occured

The final error that I will demonstrate is the "FileNotFoundError" error. This error will be thrown if a file is opened in the program, but it does not exist. In this example, I told the program to open a file that does not exist (Figure 19). If this error is raised, the program will print the message that the file must exist before running the script and then proceed to print out the built in Python error information (Figure 20 & 21).

![Figure 19](https://github.com/chrissyhend1/IntroToProg-Python-Mod07/blob/main/docs/Fig19.PNG "Figure19")  
Figure 19. The try portion of the code that will raise a FileNotFoundError if there is an attempt to open a nonexistent file

![Figure 20](https://github.com/chrissyhend1/IntroToProg-Python-Mod07/blob/main/docs/Fig20.PNG "Figure20")  
Figure 20. The except code block for the FileNotFoundError

![Figure 21](https://github.com/chrissyhend1/IntroToProg-Python-Mod07/blob/main/docs/Fig21.PNG "Figure21")  
Figure 21. The output in PyCharm IDE from the program after a FileNotFound has occured  

## Summary  
Pickling can be a great method for adding a little data security to your data and also saving some space in either memory or in transfering data over a network. Additionally error handling can be an amazing tool for simplifying built-in Python errors and presenting them to users or creating your own error messages if certain specific guidelines need to be followed.
