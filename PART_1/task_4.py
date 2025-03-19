users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

unic_set = {
    'Общее количество': 0,
    'Уникальные посещения': 0
}

unic_set['Общее количество='] = len(users)
unic_set['Уникальные посещения'] = len(set(users))

print(unic_set)
