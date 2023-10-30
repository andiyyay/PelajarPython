# outside function
def outer():
    message = 'local'
    # nested function
    def inner():
        # declare nonlacal variable
        nonlocal message
        message = 'nonlocal'
        print ("inner:", message)
    inner()
    print("outer:", message)
outer()
