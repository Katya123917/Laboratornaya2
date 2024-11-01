# TODO Напишите функцию find_common_participants
def find_common_participants(group1,group2 , delimiter=','):
    participants1 = group1.split(delimiter)
    participants2 = group2.split(delimiter)
    common_participants = set(participants1) & set(participants2)
    return sorted(common_participants)
participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group)
common_participants.sort()
print("Общие участники:", common_participants)
# TODO Провеьте работу функции с разделителем отличным от запятой
participants_first_group1 = "Иванов;Петров;Сидоров"
participants_second_group2 = "Петров;Сидоров;Смирнов"
common_participants2 = find_common_participants(participants_first_group1, participants_second_group2, delimiter= ';')
print("Общие участники:", common_participants2)