# class Dog:
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def uf(self):
#         print(f'{self.name}: Гафкает')


# dog1 = Dog('Jack', 10)
# dog2 = Dog('Recks', 3)

# dog1.uf()
# dog2.uf()


# num = 1
# num = int(1)
# print(num)

class user:

    def __init__(self, login, password, mail):
        self.login = login
        self.password = password
        self.mail = mail

    def sendMessage(self, message):
        print(f'send mail to {self.mail} with message {message}')
    
    def changePassword(self, old_password, new_password):
        if old_password == self.password:
            self.password = new_password
        else:
            print('error')


user1 = user('mario', 'qwerty', 'mario@mail.ru')
user2 = user('luigi', 'qwerty', 'luigi@gmail.com')

# user2.sendMessage('Hello world')

# print( user1.password )

# user1.changePassword('qwrty', 'coolnewpassword123')

# print( user1.password )

persons = [user1, user2]
print(persons[1].login)
