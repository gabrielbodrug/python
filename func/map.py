"""
Зачем надо
"""

# numbers = [1, 2, 3, 4, 5]
# squared = []

# for num in numbers:
#     squared.append(num ** 2)

# print(squared)

"""
Пример
"""

# def square(number):
#       return number ** 2

# numbers = [1, 2, 3, 4, 5]

# # map(function, list)

# squared = map(square, [1, 2, 3, 4, 5])

# print(list(squared))



numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))
