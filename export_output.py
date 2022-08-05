from dataclasses import dataclass
import pandas as pd

def read_data(file_name='students.csv'):
   
    # with open(file_name, 'r') as file:
    #     data = []
    #     for line in file:
    #         el = listSplit 
    #         if el in line:
    #             flag = 1
    #             data.append(line.strip().split(el)) #получаем список списков
    # return data
    listSplit = [',',';', ':']
    with open(file_name, 'r') as file:
        data = []
        temp = []
        for line in file:
            flag=0
            for el in listSplit: 
               if el in line:#если в строке есть разделитель
                flag = 1
                data.append(line.strip().split(el)) #получаем список списков

           
            if line != '' and flag == 0: 
                if line != '\n':        
                    temp.append(line.strip()) 
                else:
                    data.append(temp) #при пустой строке с \n записываем список в список списков
                    temp= []
    return data
def output_data(dt):
    if len(dt) > 0:
        print("_"*88)
        print("Фамилия".center(15), "Имя".center(15), "Телефон".center(15), "Описание".center(40))
        print("_"*88)
        for el in dt:
            print(el[0].center(15), el[1].center(15), el[2].center(15),el[3].center(40,'.'))
    else:
        print("Справочник пока не содержит данных")
    print('_'*88)
    print()

def print_data(data,key):
    # dframe = pd.DataFrame(data) 
    # print(dframe) 
    
    rows_cnt = len(data)
    cols_cnt = len(data[0])
 
    val = [[0]*rows_cnt for _ in range(cols_cnt)]
    for i in range(rows_cnt):
        for j in range(cols_cnt):
           val[j][i] = data[i][j]
    
    
    print_dict = dict(zip(key, val))
    df = pd.DataFrame(print_dict)
    print(df)


    
 