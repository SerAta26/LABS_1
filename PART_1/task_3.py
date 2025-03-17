list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

half_team = len(list_players) // 2

team_1 = list_players[:half_team]
team_2 = list_players[half_team:]

print(team_1)
print(team_2)