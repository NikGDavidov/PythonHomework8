from import_input import write_data
from import_input import input_data_Cab

from export_output import read_data
from export_output import print_data

from find_name import find_name

from delete import delete

def startC():
  flag = 1
  while flag ==1:
    print( "Выберите действие: \n\
           1 - вывод расписания работы кабинета;\n\
           2 - вывод всех мест в кабинете;\n\
           3 - добавление расписания;\n\
           4 - удаление расписания;\n\
           9 - выход в основное меню")

    mode = input("             : ")
    if mode == '9':

        flag = 0
        break
    if mode == '1':
        key = ["Урок №","Предмет", "Класс"]
        data = read_data ('cab_schedule.csv')
        if len(data)>0:
            print_data(read_data ('cab_schedule.csv'),key)
        else: print("Расписание пока отсутсвует. Добавьте его через пункт 3 меню")
    
    if mode == '2':
        data1 =[]
        data = read_data('cabinetPlaces.csv')
        for el in data[0]:  
            data1.append(list(el))

        key = ['ряд','место','вариант']
        print_data(data1,key)

    if mode== '3':
        write_data(input_data_Cab(),'cab_schedule.csv')

    if mode == '4':
#         f = open('file.txt').read()
# f = f.replace('YOUR_STRING\n','')

        info = input("Введите номер урока или название предмета для удаления: ")
        data = read_data('cab_schedule.csv')
        # data1 =[]
        # for line in data:
        #     line[2]=''


        el = find_name(info, data)
        if len(el)>0:
            print ("Нашлись следующие данные для удаления:")
            key = ["Урок №","Предмет", "Класс"]
            print_data(el,key)
            st = input("Введите через пробел индексы строк, которые вы хотите удалить (индекс верхней строчки = 0). ")
            indexDel =st.split()
            listDel =[]
            for i in indexDel:
                x = int(i)
                if x>=0 and x< len(el): listDel.append(el[x])
            delete(listDel,'cab_schedule.csv')
        else:
            print("Данные не обнаружены.")
    
    input("Нажмите enter для продолжения.")
    