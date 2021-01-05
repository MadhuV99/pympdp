# decorator_ex1.py
def my_decorator(func):
    print("Initializing the function my_deorator() .")
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
# say_whee = my_decorator(say_whee)

def main():
    for i in range(3):
        say_whee()
        print('-' * 60)

if __name__ == '__main__':
    # main()    
    pass