# module connection
import csv
import pandas as pd
from pandas import ExcelWriter

def csv_reader(file_obj, delim, *index):
    sm_list_new = []
    '''
    Read a file and iteration in list
    '''
    sm_reader = csv.reader(file_obj, delimiter = delim)
    for sm_line in sm_reader:
        sm_list_new.append([sm_line[0], sm_line[1]]) # Добавляем в новый список  занчения по индексу
    return sm_list_new

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
    Write to file
    '''

def write_to_file(filename, result): # Функция организовывает запись в файл
    with open(filename, 'w') as f:
        for line in result:
            f.write("{},\n".format(line)) # Пишем в файл результат

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

    df = pd.DataFrame(find_in_sm) # Получаем данные из find_in_sm
    df1 = pd.DataFrame(find_in_sccm) # Получаем данные из find_in_sccm
    writer = ExcelWriter('result_file.xlsx') # Создаем файл *.xlsx
    df.to_excel(writer, 'Find_in_sm', index = False) #Создаем лист, передаем данные
    df1.to_excel(writer, 'Find_in_sccm', index = False) #Создаем лист, передаем данные
    writer.save()# Записываем в файл