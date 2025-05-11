def find_common_participants(group1_str, group2_str, delimiter=','):

    group1 = group1_str.split(delimiter)
    group2 = group2_str.split(delimiter)

    common = set(group1) & set(group2)

    return sorted(common)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(
    participants_first_group,
    participants_second_group,
    delimiter='|'
)

print("Общие участники:", common_participants)