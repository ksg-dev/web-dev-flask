# def add(n1, n2):
#     return n1 + n2
#
# def subtract(n1, n2):
#     return n1 - n2
#
# def multiply(n1, n2):
#     return n1 * n2
#
# def divide(n1, n2):
#     return n1 / n2

# Functions are First-class objects,
# can be passed around as arguments e.g int/string/float

# example to use outputs from simple functions above
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
#
#
# result = calculate(multiply, 2,3)
# print(result)

# Nested functions - can only call inner function within outer function
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     nested_function()
#
# outer_function()

# Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

inner_function = outer_function()
inner_function()