## Python Decorator
# say want to add a delay without using time.sleep module in all
import time
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function


def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

decorated_function = delay_decorator(say_hello)
decorated_function()