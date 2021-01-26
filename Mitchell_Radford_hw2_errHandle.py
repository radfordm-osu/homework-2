####################################################
#                 HW 3
#    Leap Year Tester + Error Handling
#
#            INSTRUCTIONS:
#   1) Double-click the file to open
#                   OR
#      Run by name/filepath in Command Prompt
#
#   2) Input the year you would like to test for
#
#   3) Press ENTER to end the program
#
#   NOTE: This will ONLY accept a number. Input will be taken until a number input
#
#
###################################################

# Prompt user input
print("Welcome to the LEAP YEAR TESTER\n")
yearNum = 0;
year = ""
while (1):
    try:
        year = input("Input a year:  ")
        yearNum = int(year)
    except ValueError:
        print("'"+ year + "' is not a number!\n")
    else:
        break;

# The year is not a multiple of 100 but is a multiple of 4
if (yearNum % 4 == 0 and yearNum % 100 != 0):
    print(year + " is a leap year\n")
# The year is both divisible by 4 and 400
elif (yearNum % 4 == 0 and yearNum % 400 == 0):
    print(year + " is a leap year\n")
# Neither of the prior cases
else:
    print(year + " is not a leap year\n")

input("Press ENTER to exit:  ");
