# decorator_ex2.py
from decorators import do_twice

@do_twice
def say_whee():
    print("Whee!")

@do_twice
def greet(name):
    print(f"Hello {name}")

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

def main():
    # say_whee()
    # greet("hi There!") 
    # hi_adam = return_greeting("Adam")
    # print(hi_adam)  

    print(say_whee)
    print(say_whee.__name__)
    help(say_whee)

if __name__ == '__main__':
    main() 
     
