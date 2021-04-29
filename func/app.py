

# def func(function):
#     function('hello world')

# func(foo)

def foo(a):
    print(a)

a = foo
b = a
c = a

print( b == c )

print(a.__name__)