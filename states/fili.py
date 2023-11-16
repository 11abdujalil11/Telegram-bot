file = open(file='users.txt', mode='r')
list = file.read().split('\n')
users = []

for i in list:
    users.append(i.split(' '))
for i in users:
    print(i[1])