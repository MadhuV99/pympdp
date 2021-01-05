# simple_add_n.py
import functools
import time

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

cache = dict() 

@debug   
def fibonacci(n): 

    if n in cache: 
        return cache[n]   
    if n in (0, 1):
        return n
    else:
        nex_num = fibonacci(n-1) + fibonacci(n-2)
        cache[n] = nex_num
        # time.sleep(1)
        return nex_num

def main():
    print(fibonacci(5))
     
if __name__ == '__main__':     
    main()