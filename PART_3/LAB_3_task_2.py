def find_common_participants(g1, g2, sep_=','):
    g1 = g1.split(sep_)
    g2 = g2.split(sep_)
    common_participants = sorted(list(set(g1).intersection(g2)))

    return common_participants

participants_g1 = "Иванов|Петров|Сидоров"
participants_g2 = "Петров|Сидоров|Смирнов"
participants_find = find_common_participants(participants_g1, participants_g2, sep_='|')
print(participants_find)

# TODO Проверьте работу функции с разделителем отличным от запятой

participants_g1 = "Иванов,Петров,Сидоров"
participants_g2 = "Петров,Сидоров,Смирнов"
participants_find = find_common_participants(participants_g1, participants_g2)
print(participants_find)