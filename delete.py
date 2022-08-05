from export_output import read_data
from import_input import write_data
def delete (listDel, file_name ='students.csv'):
    data = read_data(file_name)
    newData =[]
    for el in data:
        if not el in listDel:
            newData.append(el)
 # print(newData)
    f = open(file_name, 'w')
    f.close()
    for line in newData:
        write_data(line,file_name)




   

