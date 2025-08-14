# Passing a function as a parameter to another function
#functions can be passed as parameters to other functions
def display(fun):
    return 'Hello '+fun
def message():
    return 'How are you?'
    
#call the display function and pass the message function as a parameter
print(display(message()))