data = ['aaaaaaaaaaaaaaaaaaaaaa', 'orange', 'white', 'guble', 'mario', 'luigi', 'egor', 'tuts', 'python']


string =  ''.join(data) 

answer = {}

for i in string:
    try:
        answer[i] += 1
    except KeyError:
        answer[i] = 1

print(answer)