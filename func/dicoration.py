# def some_decorator(f):
#     def wraps(*args):
#         print(f"Calling function '{f.__name__}'")
#         return f(args)
#     return wraps

# @some_decorator
# def decorated_function(x):
#     print(f"With argument '{x}'")

# decorated_function('Cock')

def square_decorator(function):
    def square(*args):
        return function(*args) ** 2
    return square

@square_decorator
def sum(a, b):
    return a + b

print(sum(10, 2))