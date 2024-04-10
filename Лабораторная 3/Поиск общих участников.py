# TODO Напишите функцию find_common_participant
def find_common_participants(list1, list2, x=','):
    list1 = set(list1.split(x))
    list2 = set(list2.split(x))
    list3 = []
#    for i in list1:
#       if i in list2:
#            list3.append(i)
#   return sorted(list3)
    result = list1.intersection(list2)
    return sorted(result)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
