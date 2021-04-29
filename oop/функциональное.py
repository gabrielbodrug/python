
a = input('a: ')

def culc(a, b, action):
    if action == '+':
        return int(a) + int(b)
    elif action == '-':
        return int(a) - int(b)
    elif action == '*':
        return int(a) * int(b)
    elif action == '/':
        return int(a) / int(b)
        
b = input('b: ')
action = input('action: ')

answer = culc(a, b, action)
print(answer)
