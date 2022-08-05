from export_output import read_data
from export_output import print_data

def find_person():
    info = input("Введите имя для поиска: ")
    data = read_data()
    el = find_name(info, data)
    if len(el)>0:
        print ("Нашлись следующие данные:")
        key = ['Фамилия', "Имя", "Год рожд","Класс", "Статус","Место"]
        print_data(el,key)
            
    else:
        print("Данные не обнаружены")
    return

def find_name(info, data):
    if len(data) > 0:
        find =[]
        for row in data: 
            for x in row:
              if info in x:
                find.append(row)
                break
        return find
    else:
        return []

def find_in_cab(data):
    result =''
    schedule = read_data("cab_schedule.csv")
    num = input("Введите номер урока по расписанию _")
    for el in schedule:
        if el[0] == num:
            if el[2]==data[3]:
                result = "Ученик сейчас в кабинете на месте " + data[5] + " на уроке " + el[1]
            else:
                result = "Ученик сейчас не в кабинете"
    if result =='':result = "такого урока нет в расписании"
    return result
    


    