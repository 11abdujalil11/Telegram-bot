async def w_users(state):
    file = open('user.txt', mode='a', encoding='UTF-8')
    async with state.proxy() as data:
        file.write(f"{data['fullname_ru']} {data['email_ru']} {data['phone_ru']}\n")

    file.close()


def r_users():
    file = open(file='user.txt', mode='r', encoding='UTF-8')
    count = len(file.readlines())
    file.close()
    return count


def r_message_users():
    file = open(file='user.txt', mode='r', encoding='UTF-8')
    list = file.readlines()
    file.close()
    return list


def w_user_id(user_id):
    file = open(file='user.txt', mode='a', encoding='UTF-8')
    file.write(str(user_id) + '\n')
    file.close()


def r_users_id():
    file = open(file='user.txt', mode='r', encoding='UTF-8')
    users_id = file.read().split('\n')
    file.close()
    return users_id
