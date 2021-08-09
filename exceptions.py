import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)

# try is used to 'handle the exception gracefully' 
# it prevents the user from recieving a clunky error message if something was input that doesnt work
# good if you are expecting to run into errors and handle it nicely when it goes wrong as opposed to having the whole prgram crash
try:
    result = x / y

# below is the exception where the error code is input and then replaced with another string printed
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")
# 

