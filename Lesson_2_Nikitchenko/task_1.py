'''
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий 
выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий
 новый «отчетный» файл в формате CSV. 
Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, 
их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью 
регулярных выражений извлечь значения параметров «Изготовитель системы», «Название ОС», 
«Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий 
список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
os_type_list. В этой же функции создать главный список для хранения данных отчета — например,
main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», 
«Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить
в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции 
реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных 
данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv(). ###
'''

import csv
import re
from chardet import detect


def encoding_convert(file: str):
    """Конвертация"""
    with open(file, 'rb') as f_obj:
        content_bytes = f_obj.read()
    detected = detect(content_bytes)
    encoding = detected['encoding']
    content_text = content_bytes.decode(encoding)
    with open(file, 'w', encoding='utf-8') as f_obj:
        f_obj.write(content_text)


def get_data(file: str, point: str):
    encoding_convert(file)
    with open(file, encoding='utf-8') as f:
        for line in f:
            if el := re.search(fr'(?<={point}:)\s+[-\w\d\s]+$', line):
                return el.group().strip()


def write_to_csv(file: str, lst: list):
    with open(file, 'w', encoding='utf-8') as f:
        f_writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in lst:
            f_writer.writerow(row)


os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
columns = ['Изготовитель системы',
           'Название ОС', 'Код продукта', 'Тип системы']
main_data = [columns]

for col, lst in enumerate((os_prod_list, os_name_list, os_code_list, os_type_list)):
    for i in range(1, 4):
        lst.append(get_data(f'info_{i}.txt', columns[col]))
    main_data.append(lst)

write_to_csv('out.csv', main_data)
