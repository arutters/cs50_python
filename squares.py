# in place of doing it this way you can use the code print(f"the square of {i} is {functions.square(i)}"")
# imports the "square" function from 'functions' file

# # # Example 1 (Import only cube from functions)
# from functions import cube
# for i in range(10):
#     print(f"The cube of {i} is {cube(i)}")


# # # Example 2 (Import only square from functions)
# from functions import square

# for i in range(10):
#     print(f"The square of {i} is {square(i)}")

# # # Example 3
import functions

for i in range(10):
    print(f"The square of {i} is {functions.square(i)}")

for i in range(10):
    print(f"The cube of {i} is {functions.cube(i)}")