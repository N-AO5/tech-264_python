def print_every_number(*args):  # *args takes all the arguments and creates a tuple
    print(type(args))
    for num in args:
        print(num)
        print_every_number('1', '2', '3')