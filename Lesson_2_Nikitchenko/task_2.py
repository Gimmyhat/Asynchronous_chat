'''
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON 
с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. 
Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), 
количество (quantity), цена (price), покупатель (buyer), дата (date). Функция должна 
предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать 
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее 
значений каждого параметра.
'''

import json


def write_order_to_json(data: dict):
    with open('orders.json', 'w') as f:
        json.dump(data, f, indent=4)


data = {'orders':
    [
        {
            'item': 'good1',
            'quantity': 5,
            'price': 100,
            'buyer': 'Tom Johns',
            'date': '2022-20-10'
        },
        {
            'item': 'good2',
            'quantity': 1,
            'price': 150,
            'buyer': 'Tom Johns',
            'date': '2022-20-11'
        },
    ]
}

write_order_to_json(data)