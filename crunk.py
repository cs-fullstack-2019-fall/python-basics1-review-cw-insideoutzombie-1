# python-basics1-review-cw

### Problem 1:
# Create a program that prints the user input until they enter 'q' to quit.
#
# userInput = input("Enter something man or hit 'q' to quit ")
#
# while (userInput != 'q'):
#     userInput = input("Keep trying bruh ")
#     print(userInput)

#
# ### Problem 3:
# Create a program that takes user input in a while loop.
# If they enter 1, print 1. If they enter 2, print 2. If they enter 3 print 3.
# If they enter ‘q’ or 0 (your choice), quit. Else, print “ERROR”.
#
# userInput = input("Enter '1', '2', '3', or '0' to quit ")
#
# while(userInput != '0'):
#     userInput = int(input("Enter '1', '2', '3', or '0' to quit "))
#     if(userInput == '1'):
#         print('1')
#     elif(userInput == '2'):
#         print('2')
#     elif(userInput == '3'):
#         print('3')


# ### Problem 4:
# Create a program that takes the user input until they enter 'q'.
# You should store all of their input and separate the input with a comma.
# Once they enter 'q', print all of the comma separated words they entered.

userInput = input("Enter something or hit 'q' to quit ")
words = ''

while (userInput != 'q'):
    words = words + "," + userInput
    userInput = input("Another word ")
print(words)
