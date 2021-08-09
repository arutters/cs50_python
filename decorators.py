# a decorator is a function that takes a function of input
#  and returns a modified version of that function as output

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello,world")
hello()

    