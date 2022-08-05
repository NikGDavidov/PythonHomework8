from import_input import input_data
from import_input import write_data

from controllerCab import startC

from export_output import read_data
from export_output import output_data
from export_output import print_data


from find_name import find_name
from find_name import find_person
from find_name import find_in_cab
from delete import delete


def start():
  flag = 1
  while flag ==1:
    print( "Выберите действие: \n\
           1 - вывод данных о всех учениках;\n\
           2 - поиск ученика по имени;\n\
           3 - добавление данных ученика;\n\
           4 - удаление данных ученика;\n\
           5 - просмотр или изменение данных кабинета;\n\
           6 - поиск ученика по кабинету;\n\
           9 - выход из программы")

    mode = input("             : ")
    if mode == '9':
        print ("Всего доброго!") 
        flag = 0
        break
    if mode == '1':
        key = ['Фамилия', "Имя", "Год рожд","Класс", "Статус","Место"]
        data = read_data()
        if len(data)>0 : print_data(read_data(),key)
        else :
            print("Данные пока не заведены. Можете добавить данные выбрав опцию 3.")

    if mode== '3':
       
        write_data(input_data())
    
    if mode == '5':
        startC()
   
    if mode == '2':
        find_person()

    if mode =="4":
        info = input("Введите имя для удаления: ")
        data = read_data()
        el = find_name(info, data)
        if len(el)>0:
            print ("Нашлись следующие данные для удаления:")
            key = ['Фамилия', "Имя", "Год рожд","Класс", "Статус","Место"]
            print_data(el,key)
            st = input("Введите через пробел индексы строк, которые вы хотите удалить (индекс верхней строчки = 0). ")
            indexDel =st.split()
            listDel =[]
            for i in indexDel:
                x = int(i)
                if x>=0 and x< len(el): listDel.append(el[x])
            delete(listDel)
        else:
            print("Данные не обнаружены.")
    
    if mode == '6': # ищем, находится ли сейчас ученик на уроке в кабинете
        info = input("Введите имя для поиска: ")
        data = read_data()
        el = find_name(info, data)
        if len(el)>0:
            print ("Нашлись следующие данные :")
            key = ['Фамилия', "Имя", "Год рожд","Класс", "Статус","Место"]
            print_data(el,key)
            i = int(input("Введите индекс строки с данными нужного ученика (индекс верхней строчки = 0). "))
            print(find_in_cab(el[i]))
        else:
            print("Данные не обнаружены.")

    input("Нажмите enter для продолжения.")