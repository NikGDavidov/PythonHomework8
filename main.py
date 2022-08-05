
# Задача: Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы

import controller as c
def cabinetPlaces():#  заполняем места в кабинете
    col = 3
    row = 5
    var = 2
    places = []
    for x in range (1,col+1):
        for y in range (1,row+1):
            for z in range (1, var+1):
                places.append(str(x)+str(y)+str(z))
    return places
def write_data(data): # запись новых данных в файл
    with open('cabinetPlaces.csv', 'w') as file:
            for el in data:
                file.write(f"{el}\n")   
            file.write(f"\n")     
    my_file = open("students.csv", "a")#перед началом работы нужен хотя бы пустой файл
    my_file.write("")
    my_file.close()
      
    my_file1 = open("cab_schedule.csv", "a")#перед началом работы нужен хотя бы пустой файл
    my_file1.write("")
    my_file1.close()

         

write_data (cabinetPlaces())
c.start()