# module connection
import csv
import pandas as pd
from pandas import ExcelWriter

def csv_reader(file_obj, delim, *index):
    list_new = []
    '''
    Read a file and iteration in list
    '''
    reader = csv.reader(file_obj, delimiter = delim)
    for line in reader:
        list_new.append([line[0], line[1]]) # Добавляем в новый список  занчения по индексу
    return list_new

def look_at_list(main_list, slave_list):
    not_found = []
    '''
    Looking for unique objects
    '''
    for main_found_object in main_list:
       if main_found_object not in slave_list: # Применяем итерацию по принципу "Если нет, то..."
           not_found.append(main_found_object)
    return not_found
'''
Write in file
'''
def write_to_file(filename, result): # Функция организовывает запись в файл
    with open(filename, 'w') as f:
        for line in result:
            f.write("{},\n".format(line)) # Пишем в файл результат

'''
Create a new sheets in excel file, and insert data.
'''
def new_sheet(sheet_name, find_in):
    df = pd.DataFrame(find_in) # Получаем данные из find_in_sm
    df.to_excel(writer, sheet_name, header=None, index = False) #Создаем лист, передаем данные

if __name__ == "__main__":
    '''
    Open file
    '''
    with open('sm.csv') as sm_obj:
        sm = csv_reader(sm_obj, ',')
    with open('sccm.csv') as sccm_obj:
       sccm = csv_reader(sccm_obj, ';')
    '''
    Find in file
    '''
    find_in_sccm = look_at_list(sccm, sm)
    find_in_sm = look_at_list(sm, sccm)
    '''
    Write in file result
    '''
    write_to_file('Result_find_in_sm.txt', find_in_sm)
    write_to_file('Result_find_in_sccm.txt', find_in_sccm)

    '''
    Create new file excel 
    '''
    writer = ExcelWriter('some_file.xlsx')  # Создаем файл *.xlsx
    sm_sheet = new_sheet('in_sm', find_in_sm)
    sccm_sheet = new_sheet('in_sccm', find_in_sccm)
    writer.save()