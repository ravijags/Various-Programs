# A function can return another function
def display():
    def message():
        return 'How are you?'
    return message
# call the display function and it returns the message function
fun=display()
print(fun())

        