list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Определяем индекс середины списка
middle_index = len(list_players) // 2

# Разделяем список на две команды
first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

# Выводим команды
print(first_team)
print(second_team)