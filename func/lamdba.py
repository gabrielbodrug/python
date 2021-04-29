"""
Синтаксис
"""

# def foo(x):
#     return x 

# foo(123)

# a = 1
# a = 'one'

# foo = lambda x: x 
# foo = 1

# foo(123)

"""
Примеры использования
"""

"""
Функция, которая не храниться в памяти
"""



# print((lambda x: x + 1)(10))

# def plusOne(x):
#     return x + 1

# if plusOne(int(input(': '))) == 11:
#     print('ты ввел число 10 а я прибавил к нему один ! и получил 11')

"""
Функция, аргумент
"""

def foo(num, func):
    a = func(num)
    return a


IsNumberEven = foo(10, lambda x: x ** 2)

print(IsNumberEven)

