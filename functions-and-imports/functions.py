""" base """

# from random import randint

# users = [{
#     "name": 'mario',
#     "web-site": "http://mario.it.com",
#     "mail": "mail@mario.it"
# },
# {
#     "name": 'luigi',
#     "web-site": "http://luigi.it.com",
#     "mail": "mail@luigi.it"
# },
# {
#     "name": 'yoshi',
#     "web-site": "http://yoshi.it.com",
#     "mail": "mail@yoshi.it"
# }]

# def addUid(person):
#     person['uid'] = randint(1, 10000000)
#     return person

# for i in users:
#     i = addUid(i)
#     print(i)

"""cool"""

# def createCheck(items):
#     fullPrice = 0
#     for item in items:
#         print(f'{item["name"]} - {item["price"]}$\n')
#         fullPrice += item["price"]
#     print(f'Full Price - {fullPrice}$')
        

# def byItem(packet ,item):
#     packet.append(item)
#     return packet

# item1 = {"name": 'apple', "price": 20}
# item2 = {"name": 'coca', "price": 100}
# item3 = {"name": 'candy', "price": 37}

# BackPack = []

# BackPack = byItem(BackPack, item1)
# BackPack = byItem(BackPack, item2)
# BackPack = byItem(BackPack, item3)

# createCheck(BackPack)

"""Dis"""

# data = ['apple', 'orange', 'white', 'guble', 'mario', 'luigi', 'egor', 'tuts', 'python']

# def foo(*somethig):
#     print(somethig)


# foo(*data)