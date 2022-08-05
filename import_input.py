

from export_output import read_data
# проверка занято ли место
def checkBeforeWrite(checkData, data, index):
    result = True
    for line in checkData:
       if line[index] == data :result = False
    return result


def input_data(): # ввод новых данных
    data = []
  
    data.append (input("Введите фамилию ученика: "))
    data.append(input ("Введите имя ученика : "))
    data.append(input("Введите год рождения: "))
    clas =input("Класс (например, 4А): ")
    data.append(clas)
    data.append(input ("Статус по оценкам от 2-х до 5-x: "))
    checkData = read_data("students.csv")
    checkData1 = []
    checkData1.append (list(filter(lambda x:x[3]==clas,checkData)))# создаем список учеников данного класса для последующей проверки не занято ли место.
    # print (checkData)
    # print (checkData1)
    listPlaces = read_data("cabinetPlaces.csv")
    while True:
        place = input ("Введите место в классе (например 121 - для 1 ряд 2 парта, место слева: ")   
        if checkBeforeWrite(checkData1[0],place,5) :
            if place in listPlaces[0]:
                data.append(place)
                break
            else: print("Такого места не в кабинете, выберете другое")
        else:
            print('Это место в классе занято, выберете другое')
    return data

def write_data(data,file_name = "students.csv"): # запись новых данных в файл
    with open(file_name, 'a') as file:
        #  for el in data:
        #         file.write(f"{el},") 
        #  file.write(f"\n")
         file.write(','.join(data)) # записываем данные через разделитель spr
         file.write(f"\n")
         
def input_data_Cab(): # ввод новых данных кабинета
    data = []
    checkData = read_data("cab_schedule.csv")
    while True:
        num =  (input("Введите номер урока: "))
        if checkBeforeWrite(checkData,num,0) :   
            data.append(num)
            break
         
        else:
            print('Это время занято, выберете другое')

    data.append(input ("Введите наименование предмета : "))
    data.append(input("Введите номер класса (например, 4A): "))
    return data

# def write_data_Cab(data): # запись новых данных в файл
#     with open('cab_schedule.csv', 'a+') as file:
#          for el in data:
#                 file.write(f"{el},") 
#          file.write(f"\n")
