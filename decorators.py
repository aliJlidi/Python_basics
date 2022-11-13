def announce(f):
    def wrapper():
        print('about to run a function ...')
        f()
        print('done ...')
    return wrapper


@announce
def hello():
    print("Hello, world!")


hello()